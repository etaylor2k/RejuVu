import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from rejuvu.lib import helpers as h
from rejuvu.lib.base import BaseController, render
from rejuvu.model import Users, UserLevels, Debtors, UserDebtors
from rejuvu.model.meta import Session

log = logging.getLogger(__name__)

class ReportsController(BaseController):

    def index(self):
    # The default page for the report tab

        c.user = h.user()
        c.user_level = Session.query(UserLevels).filter(UserLevels.ulid==c.user.level).first()

        return render('/report/report.mako')
