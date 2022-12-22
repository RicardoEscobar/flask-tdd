"""System test"""
import unittest
from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    """TestHome"""

    def test_home(self):
        """First test"""
        with self.app() as test_client:
            response = test_client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), {
                             'message': 'Hello, world!'})


if __name__ == '__main__':
    unittest.main()
