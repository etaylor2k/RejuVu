from sqlalchemy import Column
from sqlalchemy.types import String, Text
from sqlalchemy.dialects.postgresql import *

from rejuvu.model.meta import Base

__author__ = "Endris Taylor"

class Clients(Base):
    __tablename__ = "clients"

    client_id = Column('client_id', INTEGER, primary_key=True)
    name =Column('name', VARCHAR(255))

    def __init__(self, name =''):
    # Constructor
        self.name = name

    def __repr__(self):
    # Representaion
        return "<Clients('%s')>" %self.name
