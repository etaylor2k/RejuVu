from datetime import datetime
import hashlib
import logging
from urllib import quote

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

import tw.forms

from rejuvu.lib.base import BaseController, render
from rejuvu.lib import helpers as h
from rejuvu.model import Users
#from rejuvu.model import UserActivation
from rejuvu.model.forms.build import RegisterUserForm
from rejuvu.model.meta import Session

CAME_FROM_EXCLUDE = (
    '/account/activation',
)

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
    
    def register(self):
        if request.method == 'POST':
            state = State()
            state.session = Session
            try:
                params = register_user_form.validate(request.params, state=state)
            except tw.forms.core.Invalid, e:
                c.form_error = e.error_dict or {}
            else:
                # Create the new account in database
                users = Users(
                    username = params['user_name'],
                    email = params['email_address'],
                    displayname = params['display_name'],
                    password = params['password'],
                    activated = False,
                )
                Session.add(users)
                activation = UserActivation()
                activation.user = user
                key_seed = "%s%s%s" %(user.username, user.email_address, datetime.now().ctime())
                activation.key = hashlib.sha512(key_seed).hexdigest()   # psuedo-random hashed key
                Session.add(activation)
                
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
                message = Message("from@example.com", user.email, "Welcome to RejuVu")
                message.plain = "Your RejuVu account is ready to use. Your username is '%s'.  Activate your account at %s" %(user.username, activation_url)
                message.send()
                Session.commit()
                h.flash_info(u"A confirmation email has been sent to %s containing a link to activate your account." %(user.email_address,))
                redirect(url('/'))
        
        c.register_user_form = register_user_form
        
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
