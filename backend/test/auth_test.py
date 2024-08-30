# test_auth.py

import unittest
from auth import Auth
from user import User
from unittest.mock import patch
import json


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()
        self.user = User("testuser", "password")

    def test_login_success(self):
        with patch("builtins.input", side_effect=["testuser", "password"]):
            self.assertTrue(self.auth.login())

    def test_login_failure(self):
        with patch("builtins.input", side_effect=["testuser", "wrongpassword"]):
            self.assertFalse(self.auth.login())

    def test_register_success(self):
        with patch("builtins.input", side_effect=["newuser", "password"]):
            self.assertTrue(self.auth.register())

    def test_register_failure(self):
        with patch("builtins.input", side_effect=["testuser", "password"]):
            self.assertFalse(self.auth.register())

    def test_logout(self):
        self.auth.logout()
        self.assertIsNone(self.auth.current_user)

    def test_get_current_user(self):
        self.auth.current_user = self.user
        self.assertEqual(self.auth.get_current_user(), self.user)

if __name__ == "__main__":
    unittest.main()