from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from users import Users
from debtors import Debtors


__author__ = "Endris Taylor"

class UserDebtors(Base):
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
        return "<UserDebtors('%s')>" %self.user_debtor_id
