import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rejuvu.lib.base import BaseController, render
from rejuvu.lib import helpers as h
from rejuvu.model import Users, UserLevels, Debtors, UserDebtors, Clients
from rejuvu.model.meta import Session

from rejuvu.model.forms.build import NewClientForm

import tw.forms

log = logging.getLogger(__name__)

new_client_form = NewClientForm(
    'new_client',
    # action=url(),
    # method="post",
)


class State(object):
    """A container for passing state to validators.
    """

class ClientsController(BaseController):

    def index(self):
        # The default page for the client tab

        c.user = h.user()
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()

        # Debtors should not have access to this menu
        if (c.user_level.name == 'Debtor'):
            # Alert the user
            h.flash_alert(u"Debtors do not have access to this menu.")

            # Redirect the user to the
            return render('/')
        
        return render('/client/client.mako')

    def new(self):
        # This subroutine will render the new form to create a client

        # double check that user's level
        c.user = h.user()
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()
    
        if request.method == 'POST':
            state = State()
            state.session = Session
            try:
                params = new_client_form.validate(request.params, state=state)
            except tw.forms.core.Invalid, e:
                c.form_error = e.error_dict or {}
            else:
                # If the client passes all of the scrutiny

                clientname = params['client_name']
                client =Clients(name = clientname)
                Session.add(client)
                Session.commit()
                h.flash_ok(u"Client %s Created" %(clientname))
                return render('/home.mako')

        c.new_client_form = new_client_form
        return render('/client/new.mako')
<<<<<<< HEAD
=======

    def create(self):
        # This subrotuine will create the client

        # This will get the parameter from the form
        clientname =request.params['name']

        # query the database for a client with that name
        client =Session.query(Clients).filter(Clients.name ==clientname).first()

        if client == None:
            # There was not a client in the database with that name

            new_client = Clients(name = clientname) # create the new object
            Session.add(new_client) # add the new object to the session
            Session.commit() # commit the addition

            h.flash_ok(u"The client '%s' was created" %(clientname))

        else:
            # There is a client in the database with that name
            h.flash_alert(u"The client '%s' is already on file." %(clientname))


        c.user =h.user()
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()
        return render('/home.mako')

>>>>>>> d81c52a691f6ce33cf473aa0559af6d8523ae322
