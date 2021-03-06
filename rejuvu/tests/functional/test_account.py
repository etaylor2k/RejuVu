from rejuvu.tests import *

class TestAccountController(TestController):
    def test_login(self):
        response = self.app.get(url(controller='account', action='login'), status=200)
        
        # Test response...
        assert 'Username:' in response.body
        assert 'Password:' in response.body
    
    def test_register(self):
        response = self.app.get(url(controller='account', action='register'), status=200)
        
        assert '<form id="register_account"' in response.body
    
