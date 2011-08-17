from sqlalchemy import Column
from sqlalchemy.types inport String, Text
from sqlalchemy.dialects.postgresql import *

from rejuvu.model.meta import Base

__author__ = "Endris Taylor"
class UserLevel(Base):
    __tablename__ = "user_levels"

    ulid = Column('ulid', INTEGER, primary_key=True)
    name =Column('name', VARCHAR(255))

    def __init__(self, name =''):
    # Constructor
        self.name = name

    def __repr__(self):
    # Representaion
        return "<UserLevel('%s')" %self.name
