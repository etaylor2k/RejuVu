from datetime import datetime
import hashlib
import logging
from urllib import quote

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

import tw.forms

from rejuvu.lib.base import BaseController, render
from rejuvu.lib import helpers as h
from rejuvu.model import Users, UserLevels, Clients
from rejuvu.model.forms.build import RegisterUserForm
from rejuvu.model.meta import Session

# This will import the geocoder got google earth and to test addresses
from pygeocoder import *

CAME_FROM_EXCLUDE = (
    '/account/activation',
)

CAME_FROM_REGISTER =('/account/register',)

log = logging.getLogger(__name__)

register_user_form = RegisterUserForm(
    'register_account',
    # action=url(),
    # method="post",
)

class State(object):
    """A container for passing state to validators.
    """


class AccountController(BaseController):

    def login(self):
        identity = request.environ.get('repoze.who.identity')
        if identity is not None:
            came_from = request.params.get('came_from', None)
            if not came_from or came_from in CAME_FROM_EXCLUDE:
                redirect(url('/'))
            else:
                redirect(url(str(came_from)))
        
        return render('/account/login.mako')
    
    def register(self, userlevel =''):
        # This is the subroutine/ method for registering users/ DEBTORS

        if request.method == 'POST':
            # If we have came from the register form

            state = State()
            state.session = Session
            try:
                params = register_user_form.validate(request.params, state=state)
            except tw.forms.core.Invalid, e:
                c.form_error = e.error_dict or {}
            else:
                # Create the new account in database
                if userlevel =="":
                    userlevel =4 # Default to Debtors
                users = Users(
                    username = params['user_name'],
                    email = params['email_address'],
                    displayname = params['display_name'],
                    password = params['password'],
                    activated = False,
                    level =1
                )
                Session.add(users)
                
                http_server = request.environ.get('HTTP_ORIGIN')
                if not http_server:
                    http_server = 'http://' + request.environ['HTTP_HOST']
                
                activation_url = "%s%s?u=%s&key=%s" %(
                    http_server,
                    url(controller='account', action='activation'),
                    quote(user.username),
                    quote(activation.key)
                )
                
                from turbomail import Message
                message = Message("noreply@rejuvu.com", user.email, "Welcome to RejuVu")
                message.plain = "Your RejuVu account is ready to use. Your username is '%s'.  Activate your account at %s" %(user.username, activation_url)
                message.send()
                Session.commit()
                h.flash_info(u"A confirmation email has been sent to %s containing a link to activate your account." %(user.email_address,))
                redirect(url('/'))
        
        c.register_user_form = register_user_form

        # Get the clients that the DEBTORS can register for
        c.clients = Session.query(Clients).all()

        return render('/account/register.mako')

    def activation(self):
        success = False
        
        username = request.params.get('u')
        if username:
            user = Session.query(User).filter_by(username=username).first()
            if user is not None:
                key = request.params.get('key')
                if key and user.activation:
                    if user.activation.key == key:
                        Session.delete(user.activation)
                        user.activated = True
                        Session.commit()
                        success = True
        
        if success:
            h.flash_ok(u"Your account has been activated.  You may now login with username '%s'" %(users.username))
        else:
            h.flash_alert(u"Activation failed. The specified username or key may not be correct.")
        
        redirect("/account/login")

    def index(self):
    # This function is called after the  login has been visited
        c.user = h.user()

        if c.user is None:

            h.flash_alert(u"Login Failed. Please try again.")
            return render('/account/login.mako')

        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()
        return render('home.mako')
    
    def forgot(self):
        # render the forgot password screen
        return render('/account/forgot.mako')

    def doReset(self):
        # This is the form where the user will go once they have submitted their email address for thier password to be reset
        # This will e-mail a randomly generated password to the user
        email = request.params['user_email']

        # This will return the users object 
        u = Session.query(Users).filter_by(email=email)
        for user in u:
            temp_password = h.gen_pwd()
            from turbomail import Message
            message = Message("noreply@rejuvu.com", user.email, "Password Reset")
            message.plain = "Your new RejuVu password is '%s'. Your username is '%s'." %(temp_password, user.username)
            message.send()
            user.set_password(temp_password)
            Session.commit()
            h.flash_info(u"An email has been sent to %s containing a new password for your account." %(user.email,))
            redirect(url('/'))
        else:
            h.flash_info("Error - Sorry no such account exists or registered")

        return render('/index.mako')

    def  updatePassword(self):
        # This subroutine will update the password for the user

        user = h.user() # gets the users object

        # getsthe old, new, and the retyped new passowrd
        new_pwd = request.params['pwd_new']
        old_pwd = request.params['pwd_old']
        new_pwd_re = request.params['pwd_new_re']

        # test to see if they've entered the correct old passwrd
        if (new_pwd =='') and (old_pwd =='') and (new_pwd_re ==''):
        # If nothing was entered, user just pressed the button
            pass
        elif user.validate_password(old_pwd):

            # test to see if they've netered the new password in correctly
            if new_pwd == new_pwd_re:
            # update the user with the new password
                user.set_password(new_pwd)
                Session.commit()
                h.flash_ok(u"Your password has changed.")
            else:
             h.flash_alert(u"Password change failed.")
        else:
            h.flash_alert(u"Password change failed.")

        c.user = user
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()
        return render("/home.mako")

    def updateUserInfo(self):
            # This subroutine will update the users inforamtion

            error =False
            changed =False

            # get the parameters from the form
            new_name = request.params['name']
            new_username = request.params['username']
            new_userlevel = request.params['userlevel']
            new_email = request.params['email']
            new_address = request.params['address']
            new_city = request.params['city']
            new_state = request.params['state']
            new_zip = request.params['zip']

            c.user =h.user() # get the user object
            usernames = Session.query(Users.username)
            emails = Session.query(Users.email)
            g =Geocoder()
        
            # gets the users level
            c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()

            if c.user_level.name != new_userlevel:
                # test to see if the users level has been changed, ERROR if so
                error = True
                h.flash_alert(u"User Level change is prohibited.")

            if (c.user.username != new_username) and (error ==False):
                # Test to see if the user name has changed

                if not new_username in usernames:
                # test to see if the username is unique
                    c.user.username = new_username
                    Session.commit()
                    changed =True

                else:
                # The use name is not unique
                    h.flash_alert(u"Username already taken.")

             # Test to see if the address changed
            if (new_address != '') and (new_city !='') and (new_state != '') and (new_zip != '') and (error ==False) and (g.geocode(new_address+ ' ' + new_city +', '+ new_state+' '+ new_zip).valid_address !=False):
                 # There are not any empty address fields and the address is valid
                 # Check to see if there are any changes

                 if (c.user.address != new_address):
                     # address change
                     c.user.address =new_address
                     Session.commit()
                     if changed != True: changed =True

                 if (c.user.city != new_city):
                     # new city
                     c.user.city =new_city
                     Session.commit()
                     if changed != True: changed =True

                 if (c.user.state != new_state):
                     # new state
                     c.user.state =new_state
                     Session.commit()
                     if changed != True: changed =True

                 if (c.user.zip != new_zip):
                     # new zip code
                     c.user.zip =new_zip
                     Session.commit()
                     if changed != True: changed =True

            elif (c.user.address == new_address) and (c.user.state == new_state) and (c.user.city == new_city) and (c.user.zp ==new_zip):
                # If everything in the form address wise has not been changed then there is nothing that needs to be done
                pass

            else:
                # The address was bad
                error = True
                h.flash_alert(u"Improper Address.")

            if changed ==True and error ==False:
                h.flash_ok(u"Your user account is updated.")
                
            return render('/home.mako')

