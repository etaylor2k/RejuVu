"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password
# from webhelpers.html import literal
# from webhelpers.html.tags import *

from pylons import url, request, response

from webflash import Flash

# WebFlash is used to flash messages to the user. Flashed messages
#   will survive redirects and will only be displayed once.
#   Use the flash_ok(), flash_info() & flash_alert() convenience
#   functions to flash messages.

from rejuvu.model.meta import Session
from rejuvu.model import UserLevels

flash = Flash(
    get_response=lambda: response,
    get_request=lambda: request
)

def flash_ok(message):
    flash(message, status='ok')

def flash_info(message):
    flash(message, status='info')

def flash_alert(message):
    flash(message, status='alert')


def user():
    """Return the currently logged-in user object
    or None if not logged in.
    """
    identity = request.environ.get('repoze.who.identity')
    if identity is not None:
        # Get some data associated with the user. (Eg. the user object that was assigned in UserModelPlugin.)
        user = identity.get('user')
    else:
        user = None
    return user

def userLevel():
    """This subroutine will return the user's level object. Since that is needed in a few places
    creating a helper function for this saves us from having to do a SQL call every time """

    thisuser = user() # get the current user
    userlevel = Session.query(UserLevels).filter(UserLevels.ulid==thisuser.level).first()

    if userlevel is None:
        userlevel = None

    return userlevel

