# encoding: utf-8

'''validators
'''
import formencode.validators

__author__ = 'Chris Miles'
__copyright__ = '(c) Chris Miles 2009. All rights reserved.'
__id__ = '$Id$'
__url__ = '$URL$'


# ---- Imports ----

# - Python modules -
import re

import formencode
from formencode.compound import All, Any

# note: avoid tw.forms.validators -> use formencode directly so that
#   these validators can be used outside of a ToscaWidgets environment.
# import tw.forms

from rejuvu.model import Users, USERNAME_SIZE, Clients


USERNAME_MIN_LENGTH=4


# ---- Custom Validators ----

# - Unique username validator -
class UniqueUsername(formencode.FancyValidator):
    """Validate that the value is a unique username (i.e. the username
    does not already exist in the database).
    
    Requires an object to be passed in as ``state`` that contains a
    ``session`` attribute pointing to a SQLAlchemy Session object.
    The validator uses the Session object to access the database.
    """
    
    messages = {
        'username_taken': 'Username already taken',
    }
    
    def validate_python(self, value, state):
        """``state`` should be an object containing a ``session``
        attribute, referencing an SQLAlchemy Session object
        that can be used to access the database.
        """
        if state is not None and hasattr(state, 'session'):
            acct = state.session.query(Users).filter_by(username=value).first()
            if acct is not None:
                raise formencode.Invalid(self.message("username_taken", state), value, state)
        
        else:
            # This means a Session object wasn't passed in as the "state".
            raise ValueError("state object needs session attribute", value, state)


# - Unique email validator -
class UniqueEmail(formencode.FancyValidator):
    """Validate that the value is a unique email (i.e. the email
    address does not already exist in the database).
    
    Requires an object to be passed in as ``state`` that contains a
    ``session`` attribute pointing to a SQLAlchemy Session object.
    The validator uses the Session object to access the database.
    """
    
    messages = {
        'email_taken': 'Email address already taken',
    }
    
    def validate_python(self, value, state):
        """``state`` should be an object containing a ``session``
        attribute, referencing an SQLAlchemy Session object
        that can be used to access the database.
        """
        if state is not None and hasattr(state, 'session'):
            acct = state.session.query(Users).filter_by(email=value).first()
            if acct is not None:
                raise formencode.Invalid(self.message("email_taken", state), value, state)
        
        else:
            # This means a Session object wasn't passed in as the "state".
            raise ValueError("state object needs session attribute", value, state)

class UniqueClient(formencode.FancyValidator):
    """Validate that the value is a unique client Name (i.e. the client
    does not already exist in the database).

    Requires an object to be passed in as ``state`` that contains a
    ``session`` attribute pointing to a SQLAlchemy Session object.
    The validator uses the Session object to access the database.
    """

    messages = {
        'client_taken': 'Client already taken',
    }

    def validate_python(self, value, state):
        """``state`` should be an object containing a ``session``
        attribute, referencing an SQLAlchemy Session object
        that can be used to access the database.
        """
        if state is not None and hasattr(state, 'session'):

            # This will get the list of all of the Clients
            clients =[]
            cli = state.session.query(Clients).all()
            
            for index in range(len(cli)):
                # turn all of the elements into lower case
                clients.append(cli[index].name.lower())

            if value.lower() in clients:
                raise formencode.Invalid(self.message("client_taken", state), value, state)
        else:
            # This means a Session object wasn't passed in as the "state".
            raise ValueError("state object needs session attribute", value, state)

# - Valid username validator -
class ValidUsername(formencode.FancyValidator):
    """Validate that the value meets the requirements for a username.
    
    The attributes ``reserved_usernames`` and ``username_re`` can be
    overridden by passing new values as keyword arguments to the
    constructor.
    """
    reserved_usernames = (
        'admin',
        'root',
        'administrator',
        'functest',
        'functest1',
        'functest2',
        'functest3',
        'functest4',
        'functest5',
        'functest6',
        'functest7',
        'functest8',
        'functest9',
    )
    username_re = re.compile(r'^[a-z][a-z0-9.-]+$')
    
    messages = {
        'bad_length': 'Username must be %d-%d characters long' %(USERNAME_MIN_LENGTH, USERNAME_SIZE),
        'invalid_username': 'Invalid username',
    }
    
    def validate_python(self, value, state):
        if len(value) < USERNAME_MIN_LENGTH or len(value) > USERNAME_SIZE:
            raise formencode.Invalid(self.message('bad_length', state), value, state)
        inx = self.username_re.match(value)
        if inx is None:
            raise formencode.Invalid(self.message('invalid_username', state), value, state)
        if '..' in value or '--' in value:
            raise formencode.Invalid(self.message('invalid_username', state), value, state)
        if value in self.reserved_usernames:
            raise formencode.Invalid(self.message('invalid_username', state), value, state)
    


# - Good password validator -
class SecurePassword(formencode.FancyValidator):
    """Validate that value meets certain requirements that help make it
    a more "secure" password.
    
    The attribute ``password_re`` can be overridden by passing new values
    as keyword arguments to the constructor.
    """
    password_re = re.compile(r'[0-9,./;:\'"\\|\[\]{}!@#$%^&*()_=+-]')
    
    messages = {
        'too_short': 'Password must be at least 4 characters long',
        'insecure': 'Password must contain at least one number or punctuation character',
    }
    
    def _to_python(self, value, state):
        # _to_python gets run before validate_python.  Here we
        # strip whitespace off the password, because leading and
        # trailing whitespace in a password is too elite.
        return value.strip()
    
    def validate_python(self, value, state):
        if len(value) < 4:
            raise formencode.Invalid(self.message('too_short', state), value, state)
        # Ensure password contains at least one digit or non a-z character
        inx = self.password_re.search(value)
        if inx is None:
            raise formencode.Invalid(self.message('insecure', state), value, state)
    


# ---- Validator Containers ----

class UserValidators(object):
    user_name = All(
        formencode.validators.String(not_empty=True),
        ValidUsername(),
        UniqueUsername(),
    )
    
    display_name = formencode.validators.String(
        not_empty=True,
        max=255,
        # messages={
        #     'empty':'Please enter your name.'
        # }
    )
    
    email_address = All(
        # formencode.validators.Email(resolve_domain=True),
        formencode.validators.Email(not_empty=True),
        formencode.validators.String(max=255),
        UniqueEmail(),
    )
    
    password = All(
        formencode.validators.String(not_empty=True),
        SecurePassword()
    )

    client_name = All(
        formencode.validators.String(not_empty=True),
        UniqueClient()
    )
    
    activated = formencode.validators.StringBool()

