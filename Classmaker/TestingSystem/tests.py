# tests.py

from django.test import TestCase, Client
from django.urls import reverse

class TestingViewTestCase(TestCase):
    def test_testing_view_with_params(self):
        client = Client()
        url = reverse('testing')
        response = client.get(url, {'test_id': '2117369', 'success': 'removeRandom'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test ID: 2117369')
        self.assertContains(response, 'Success: removeRandom')