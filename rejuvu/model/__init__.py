"""The application's model objects"""
from datetime import datetime
import hashlib
import logging
import os

import sqlalchemy as sa
from sqlalchemy import orm

from rejuvu.model import meta
from user_level import UserLevel
from user import User

USERNAME_SIZE=16

log = logging.getLogger(__name__)

def init_model(engine, auto_schema_update=False):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine

## Non-reflected tables may be defined and mapped at module level
"""user_table = sa.Table('user', meta.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_name', sa.Unicode(USERNAME_SIZE), unique=True),
    sa.Column('email_address', sa.Unicode(255)),
    sa.Column('display_name', sa.Unicode(255)),
    sa.Column('password', sa.String(128)),          # room for SHA-512 hashed passwords (hexdigest)
    sa.Column('created', sa.DateTime, default=datetime.now),
    sa.Column('activated', sa.Boolean, nullable=False, default=False),
)
user_activation_table = sa.Table('user_activation', meta.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
    sa.Column('key', sa.Unicode(128), nullable=False),
    sa.Column('created', sa.DateTime, default=datetime.now),
)


# ---- ORM Mapped Classes ----

class User(object):
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            if key == 'password':
                # Hash password
                self.set_password(value)
            else:
                setattr(self, key, value)
    
    def validate_password(self, password):
        # The given password is hashed and compared against the one
        # stored in the database.  Returns True if they are equal, else
        # False.
        
        # This method is called by repoze.who.plugins.sa.SQLAlchemyAuthenticatorPlugin
        
        hashed_password = self._hash_password(password)
        return self.password == hashed_password and self.activated
    
    def set_password(self, raw_pass):
        # Set a new password for the account.  The raw password
        # will be stored in hashed form and will not be reversible.
        
        self.password = self._hash_password(raw_pass)
    
    def _hash_password(self, raw_pass):
        return hashlib.sha512(raw_pass).hexdigest()
    

class UserActivation(object):
    pass

orm.mapper(User, user_table,
    properties = dict(
        activation = sa.orm.relation(UserActivation, backref='user', uselist=False, cascade="all, delete, delete-orphan"),
    )
)
orm.mapper(UserActivation, user_activation_table)"""


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
