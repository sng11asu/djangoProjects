from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.

class Moviestestcase(APITestCase):
    def test_collection(self):
        test_collection = {"title": "coll4", "description": "description 4", "movies": [77,78]}
        response = self.client.post('/collections/', test_collection)
        self.assertEqual(response.status_code, "200")

    def test_putcollection(self):
        test_collection = {"title": "coll4", "description": "description 4", "movies": [77,78]}
        response = self.client.put('/collection/7879847a-dac1-4e60-ae0d-6766ba1e6ce5/', )
        self.assertEqual(response.status_code, "200")

    def test_resetcounter(self):
        response = self.client.post('/request-count/reset/', {})
        self.assertEqual(response.status_code, "200")
