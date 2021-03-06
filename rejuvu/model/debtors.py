from sqlalchemy import Column, ForeignKey
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
    placed = Column('placed', FLOAT)
    collected = Column('collected', FLOAT)

    client = Column(INTEGER, ForeignKey('clients.client_id'))
    clients = relation('Clients')


    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "<Debtors('%s')>" %self.username