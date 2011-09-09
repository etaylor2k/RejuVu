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
                pass

        c.new_client_form = new_client_form
        return render('/client/new.mako')

    def create(self):
        # This subroutine will create a new client for the user

        name = request.params['client_name'] # gets the

        c.user = h.user()
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()

        if name == None:
        # The user did not enter anything
            return render('/client/client.mako')
        
        onFile = Session.query(Clients).filter(Clients.name ==name).first()

        if onFile is not None:
        # This is a unique client
            client =Clients(name)
            Session.add(client)
            Session.commit()
            h.flash_ok(u"Client %s Created" %(name))

        else:
        # The client already exists
            h.flash_alert(u"Client %s already exists" %(name))
        
        return render('/home.mako')

