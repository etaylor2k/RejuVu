from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from clients import Clients

__author__ = "Endris Taylor"

class Debtors(Base):
    __tablename__ ="debtors"

    #Class attributes reporesenting columns from the users table
    debtorid = Column('debtorid', INTEGER, primary_key=True)
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