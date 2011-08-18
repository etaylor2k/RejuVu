from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from debtors import Debtors

__author__ = "Endris Taylor"

class Transactions(Base):
    __tablename__ ="transactions"

    #Class attributes reporesenting columns from the users table
    trans_id = Column('trans_id', INTEGER, primary_key=True)
    amount = Column('amount', MONEY)
    date = Column('date', TIMESTAMP, default=datetime.now)

    debtor = Column(INTEGER, ForeignKey('debtors.debtorid'))
    debtors = relation('Debtors')


    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "<Transactions('%s')>" %self.trans_id