#!/usr/bin/env python
# encoding: utf-8
"""
test_models.py
"""
from datetime import date, datetime
import hashlib
import unittest

import sqlalchemy as sa

from rejuvu import model
from rejuvu.model.meta import Session

MODEL_CLASSES = (
    model.User,
    model.UserActivation,
)


# ---- Utility Functions ----

def clean_db():
    for model_class in MODEL_CLASSES:
        for rec in Session.query(model_class):
            Session.delete(rec)
        Session.commit()


# ---- Test Cases ----

class UserTests(unittest.TestCase):
    def setUp(self):
        user = model.User(
            user_name = u'test1',
            email_address = u'test1@example.com',
            display_name = u'Test One',
            password = u'myPassword9!',
            activated = True,
        )
        Session.add(user)
        Session.commit()
    
    def tearDown(self):
        # Empty out the tables
        clean_db()
    
    def test_add_user(self):
        u = Session.query(model.User).filter_by(user_name=u'test1').one()
        self.failUnlessEqual(u.email_address, u'test1@example.com')
        self.failUnlessEqual(u.display_name, u'Test One')
        self.failUnlessEqual(u.password, hashlib.sha512(u'myPassword9!').hexdigest())
        self.failUnlessEqual(u.activated, True),
        self.failUnless(u.id > 0)
        self.failUnless(u.created <= datetime.now())
    
    def test_duplicate_user_name(self):
        user = model.User(
            user_name = u'test1',
            email_address = u'test1@example2.com',
            display_name = u'Test One Again',
            password = u'myPassword8!',
            activated = True,
        )
        Session.add(user)
        self.failUnlessRaises(sa.exc.IntegrityError, Session.commit)
        Session.rollback()
    
    def test_validate_password(self):
        u = Session.query(model.User).filter_by(user_name=u'test1').one()
        self.failUnlessEqual(u.validate_password(u'myPassword9!'), True)
    
class UserActivationTests(unittest.TestCase):
    def setUp(self):
        user = model.User(
            user_name = u'test1',
            email_address = u'test1@example.com',
            display_name = u'Test One',
            password = u'myPassword9!',
            activated = True,
        )
        Session.add(user)
        
        act = model.UserActivation()
        act.key = u'testkey'
        Session.add(act)
        
        act.user = user
        
        Session.commit()
    
    def tearDown(self):
        # Empty out the tables
        clean_db()
    
    def test_user_activation(self):
        u = Session.query(model.User).filter_by(user_name=u'test1').one()
        self.failUnlessEqual(u.activation.key, u'testkey')
