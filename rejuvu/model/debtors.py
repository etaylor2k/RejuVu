from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from user_levels import UserLevels

from datetime import datetime
import hashlib

__author__ = "Endris Taylor"

class Debtors(Base):
    __tablename__ ="debtors"

    #Class attributes reporesenting columns from the users table
    uid = Column('debtorid', INTEGER, primary_key=True)
    ref_num = Column('ref_num', VARCHAR(255))
    principle = Column('princible', MONEY)
    interest = Column('interest', MONEY)
    commission = Column('commission', MONEY)
    collected_principle = Column('collected_princible', MONEY)
    collected_interest = Column('collected_interest', MONEY)
    collected_commission = Column('collected_commission', MONEY)

    client = Column(INTEGER, ForeignKey('clients.client_id'))
    clients = relation('Clients')


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

