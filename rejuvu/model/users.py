from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from user_levels import UserLevels

from datetime import datetime
import hashlib

__author__ = "Endris Taylor"

class Users(Base):
    __tablename__ ="users"

    #Class attributes reporesenting columns from the users table
    uid = Column('uid', INTEGER, primary_key=True)
    email = Column('email', VARCHAR(255))
    username = Column('username', VARCHAR(25))

    level = Column(INTEGER, ForeignKey('user_levels.ulid'))
    user_levels = relation('UserLevels')
    
    password = Column('password', VARCHAR(128))
    name = Column('name', VARCHAR(255))
    address = Column('address', VARCHAR(255))
    city = Column('city', VARCHAR(255))
    state = Column('state', VARCHAR(100))
    zip = Column('zip', VARCHAR(10))
    created = Column('created', TIMESTAMP, default=datetime.now)
    activated = Column('activated', BOOLEAN)
    key = Column('key', VARCHAR(64))

    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            if key == 'password':
                # Hash password
                self.set_password(value)
            else:
                setattr(self, key, value)

    def __repr__(self):
        return "<Users('%s')>" %self.username


    def validate_password(self, password):
        """The given password is hashed and compared against the one
        stored in the database.  Returns True if they are equal, else
        False.

        This method is called by repoze.who.plugins.sa.SQLAlchemyAuthenticatorPlugin
        """
        hashed_password = self._hash_password(password)
        return self.password == hashed_password and self.activated

    def set_password(self, raw_pass):
        """Set a new password for the account.  The raw password
        will be stored in hashed form and will not be reversible.
        """
        self.password = self._hash_password(raw_pass)

    def _hash_password(self, raw_pass):
        return hashlib.sha512(raw_pass).hexdigest()

