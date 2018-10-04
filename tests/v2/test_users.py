"""
This module facilitates testing
"""
import unittest
import os
import sys
import json
from tests.v2.base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'

class UserTest(BaseTests):
    """
    This class contain methods for user manipulation
    """

    def test_successful_registration(self):
        """
        This method tests successful user creation
        """
        user = {
            "username": "jamalkim",
            "email": "jamal97@gmail.com",
            "password": "pariskimmy",
            "confirm_password": "pariskimmy"
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'successfully registered')

    def test_wrong_input_during_signup(self):
        """
        This method tests error returned if wrong password input is used
        """
        data = {
            'username': 'melvinkeys',
            'email': 'melvinkeys@gmail.com',
            'password': '',
            'confirm_password': 'jamesbond'
        }
        response = self.client().post(SIGNUP_URL, data=data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'password and confirm password should be identical')

    def test_double_signup(self):
        """
        This method tests error return for double registration
        """
        user = {
            'username': 'aliciakeys',
            'email': 'aliciakeys@gmail.com',
            'password': 'aliciakeys',
            'confirm_password': 'aliciakeys'
        }
        self.client().post(SIGNUP_URL, data=user)
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'username already taken')

    def test_failed_registration_with_invalid_email(self):
        """
        This method tests failed registration with invalid email
        """
        user = {
            'username': 'jamesbond',
            'email': 'jamesbondgmail.com',
            'password': 'jamesbond',
            'confirm_password': 'jamesbond'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), {'email': 'kindly provide a valid email address'})

    def test_failed_registration_short_password(self):
        """
        This method tests failed registration for short password
        """
        user = {
            'username': 'jamesbond',
            'email': 'jamesbond@gmail.com',
            'password': 'james',
            'confirm_password': 'james'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], 'password should be atleast 8 characters')

    def test_successful_login(self):
        """
        This method tests a successful login
        """
        user = {
            'username': 'lucasthomas',
            'email': 'lucasthomas@gmail.com',
            'password': 'lucasthomas',
            'confirm_password': 'lucasthomas'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 201)
        data = {
            'email': 'lucasthomas@gmail.com',
            'password': 'lucasthomas'
        }
        res = self.client().post(LOGIN_URL, data=data)
        self.assertEqual(res.status_code, 200)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'you are successfully logged in')

    def test_fail_login_wrong_password(self):
        """
        This method tests unsuccessful login for wrong password
        """
        user = {
            'username': 'eminem',
            'email': 'eminem@gmail.com',
            'password': 'kamikaze',
            'confirm_password': 'kamikaze'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 201)
        data = {
            'email': 'eminem@gmail.com',
            'password': 'killshot'
        }
        res = self.client().post(LOGIN_URL, data=data)
        self.assertEqual(res.status_code, 401)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'invalid email or password')

    def test_fail_login_wrong_email(self):
        """
        This method tests unsuccessful login for wrong email
        """
        user = {
            'username': 'eminem',
            'email': 'eminem@gmail.com',
            'password': 'kamikaze',
            'confirm_password': 'kamikaze'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 201)
        data = {
            'email': 'emin@gmail.com',
            'password': 'kamikaze'
        }
        res = self.client().post(LOGIN_URL, data=data)
        self.assertEqual(res.status_code, 404)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'invalid email or password')

    def test_login_non_existing_user(self):
        """
        This method tests unsuccessful login for a user that doesnt exist
        """
        user = {
            'username': 'eminem',
            'email': 'eminem@gmail.com',
            'password': 'kamikaze',
            'confirm_password': 'kamikaze'
        }
        response = self.client().post(SIGNUP_URL, data=user)
        self.assertEqual(response.status_code, 201)
        data = {
            'email': 'eminem97@gmail.com',
            'password': 'kamikazeeer'
        }
        res = self.client().post(LOGIN_URL, data=data)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'invalid email or password')


if __name__ == '__main__':
    unittest.main()
