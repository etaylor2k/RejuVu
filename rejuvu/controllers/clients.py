import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rejuvu.lib.base import BaseController, render
from rejuvu.lib import helpers as h
from rejuvu.model import Users, UserLevels, Debtors, UserDebtors
from rejuvu.model.meta import Session

log = logging.getLogger(__name__)

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

        if (c.user_level.name != "Super User"):
            h.flash_alert(u"You do not have access to this function.")
            return render ('/')

        return render('/client/new.mako')

    def create(self):

        return 'hello'

