from rejuvu import model
from rejuvu.model.meta import Session
from rejuvu.tests import *
from rejuvu.tests.test_models import clean_db

class TestHomeController(TestController):
    def tearDown(self):
        # Empty out the tables
        clean_db()
    
    def test_index_anonymous(self):
        response = self.app.get(url(controller='home', action='index'), status=200)
        
        # Test response...
        assert 'Home' in response.body
        assert 'Register' in response.body
    
    def test_index_authenticated(self):
        # Create a user to authenticate as
        user = model.User(
            user_name = u'test1',
            email_address = u'test1@example.com',
            display_name = u'Test One',
            password = u'myPassword9!',
            activated = True,
        )
        Session.add(user)
        Session.commit()
        
        environ = {'REMOTE_USER': 'test1'}
        
        response = self.app.get(url(controller='home', action='index'), extra_environ=environ, status=200)
        
        # Test response...
        assert 'Test One' in response.body
        assert 'Logout' in response.body
    
