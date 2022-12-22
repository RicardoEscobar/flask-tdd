"""System test"""
import unittest
from unittest import TestCase
import json
from app.app import app


class TestHome(TestCase):
    """TestHome"""

    def test_home(self):
        """First test"""
        with app.test_client() as test_client:
            response = test_client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), {
                             'message': 'Hello, world!'})


if __name__ == '__main__':
    unittest.main()
