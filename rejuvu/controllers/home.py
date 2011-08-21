import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect

from rejuvu.lib.base import BaseController, render
from rejuvu.lib import helpers as h

log = logging.getLogger(__name__)

class HomeController(BaseController):
    def index(self):
        # WebFlash is used to flash messages to the user. Flashed messages
        #   will survive redirects and will only be displayed once.
        # h.flash_alert("Flash an Alert!")
        # h.flash_info("Flash an Info")
        # h.flash_ok("Flash an OK")

        c.user =h.user() # checks for the identity of the user if there

        if c.user is None:
            return render('/account/login.mako')
        
        return render('/home.mako')

    
