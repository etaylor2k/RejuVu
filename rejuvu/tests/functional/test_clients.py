from rejuvu.tests import *

class TestClientsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='clients', action='index'))
        # Test response...
