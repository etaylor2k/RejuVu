from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from users import Users
from debtors import Debtors


__author__ = "Endris Taylor"

class Debtors(Base):
    __tablename__ ="user_debtors"

    #Class attributes reporesenting columns from the users table
    user_debtor_id = Column('ser_debtor_id', INTEGER, primary_key=True)

    user = Column(INTEGER, ForeignKey('users.uid'))
    users = relation('Users')

    debtor = Column(INTEGER, ForeignKey('debtors.debtorid'))
    debtors = relation('Debtors')


    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "<Debtors('%s')>" %self.username


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

