"""The application's model objects"""
from datetime import datetime
import hashlib
import logging
import os

import sqlalchemy as sa
from sqlalchemy import orm

from rejuvu.model import meta
from user_levels import UserLevels
from users import Users
from debtors import Debtors
from clients import Clients
from user_debtors import UserDebtors
from transactions import Transactions


USERNAME_SIZE=16

log = logging.getLogger(__name__)

def init_model(engine, auto_schema_update=False):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine
