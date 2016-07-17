from django.test import TestCase

from mainapp.models import Server

# Create your tests here.
class ServerModelTests(TestCase):
    def test_is_empty(self):
        saved_servers = Server.get_all()
        self.assertEqual(saved_servers.count(), 0)
