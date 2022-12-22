from unittest import TestCase
from app.app import app


class BaseTest(TestCase):
    """BaseTest class"""

    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client
        return super().setUp()
