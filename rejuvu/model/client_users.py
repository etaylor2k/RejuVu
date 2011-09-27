from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relation

from rejuvu.model.meta import Base
from users import Users
from clients imports Clients


class ClientAdmins(Base):
    __tablename__ ='client_admins'

    #Class attributes representing the columns

    #Primary Key
    client_user_id = Column('client_user_id', INTEGER, primary_key=True)

    # client foreign key
    client = Column(INTEGER, ForeignKey('clients.client_id'))
    clients = relation('Clients')

    # user foreign key
    user = Column(INTEGER, ForeignKey('users.uid'))
    users = relation('Users')

    def __init__(self, ):
        for key,value in kwargs.items():
            setattr(self, key, int(value))

    def __repr__(self):
        return "<ClientAdmins('%s')>" %self.client_admin_id


  