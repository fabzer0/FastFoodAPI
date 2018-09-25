"""
This module facilitates testing
"""
import unittest
import json
import sys
import os

from .base_setup import BaseTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))





class TestUserRegistration(BaseTest):
    """
    This class contains methods to test user manipulation
    """

    def test_successful_user_creation(self):
        """
        Tests successful user creation
        """
        first_user = self.client().post('/api/v1/auth/signup', data=self.user_1)
        self.assertEqual(first_user.status_code, 201)
        result_1 = json.loads(first_user.data.decode('utf-8'))
        self.assertEqual(result_1['username'], 'fabischapeli')
        second_user = self.client().post('/api/v1/auth/signup', data=self.user_2)
        self.assertEqual(second_user.status_code, 201)
        result_2 = json.loads(second_user.data.decode('utf-8'))
        self.assertEqual(result_2['username'], 'enockolasi')


    def test_return_all_users(self):
        """
        Tests successful return of all users
        """
        data_1 = {
            "username": "mercyapril",
            "email": "mercyapril@gmail.com",
            "password": "alwaysimple",
            "confirm_password": "alwaysimple"
        }
        data_2 = {
            "username": "melvinfreizer",
            "email": "melvinfreizer@gmail.com",
            "password": "alwaysfreizer",
            "confirm_password": "alwaysfreizer"
        }
        self.client().post('/api/v1/auth/signup', data=data_1)
        self.client().post('/api/v1/auth/signup', data=data_2)
        response = self.client().get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_return_one_user(self):
        """
        Tests successful return of a particular user
        """
        data = {
            "username": "jamalcassidy",
            "email": "jamalcassidy@gmail.com",
            "password": "alwayscassidy",
            "confirm_password": "alwayscassidy"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        self.assertEqual(response.status_code, 201)
        res = self.client().get('/api/v1/users')
        self.assertEqual(res.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['email'], 'jamalcassidy@gmail.com')
        list_user = []
        list_user.append(result)
        self.assertTrue(len(list_user) == 1)

    def test_successful_user_update(self):
        """
        This method successfully updates user
        """
        data = {
            "username" : "fabischapeli",
            "email" : "fabischapeli97@gmail.com",
            "password" : "pass12342",
            "confirm_password" : "pass12342"
        }
        response = self.client().put('/api/v1/users/2', data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_an_existing_user(self):
        """
        Tests successful deletion of a user
        """
        response = self.client().delete('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

    def test_create_user_with_existing_email(self):
        """
        Tests return of error if email matches an already existing one during creation
        """
        data = {
            "username": "jamiefoxx",
            "email": "jamiefoxx@gmail.com",
            "password": "alwaysjamie",
            "confirm_password": "alwaysjamie"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        self.assertEqual(response.status_code, 201)
        res = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['message'], 'user with that email already exist')

    def test_get_non_existing_user(self):
        """
        Tests error return for getting a non existing user
        """
        data = {
            "username": "anikasavannah",
            "email": "anikasavannah@gmail.com",
            "password": "alwaysanika",
            "confirm_password": "alwaysanika"
        }
        self.client().post('/api/v1/auth/signup', data=data)
        res = self.client().get('/api/v1/users/11')
        self.assertEqual(res.status_code, 401)

    def test_edit_user_that_doest_not_exist(self):
        """
        Tests error returned for updating a non existing user
        """
        old_data = {
            "username": "pierramakena",
            "email": "pierramakena@gmail.com",
            "password": "alwaysmakena",
            "confirm_password": "alwaysmakena"
        }
        new_data = {
            "username": "pierramakena",
            "email": "pierramakena@gmail.com",
            "password": "alwayspierra",
            "confirm_password": "alwayspierra"
        }
        response = self.client().post('/api/v1/auth/signup', data=old_data)
        self.assertEqual(response.status_code, 201)
        res = self.client().put('/api/v1/users/2', data=new_data)
        self.assertEqual(res.status_code, 200)

    def test_delete_user_that_doest_not_exist(self):
        """
        Tests error returned for deleting a non existing user
        """
        res = self.client().delete('/api/v1/users/25')
        self.assertEqual(res.status_code, 404)

    def test_create_user_non_identical_passwords(self):
        """
        Tests ensuring password and confirm_password are identical
        """
        data = {
            "username": "niklaus",
            "email": "niklaus@gmail.com",
            "password": "alwaysnikki",
            "confirm_password": "alwaysniklaus"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "password and confirm password should be identical")

    def test_user_creation_short_password(self):
        """
        Tests return error for short passwords
        """
        data = {
            "username": "remyma",
            "email": "remyma@gmail.com",
            "password": "remyma",
            "confirm_password": "remyma"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'], "password should be atleast 8 characters")

    def test_create_user_empty_username(self):
        """
        This method returns error if user is created with an empty username
        """
        data = {
            "username" : "",
            "email" : "geazy@gmail.com",
            "password" : "sec",
            "confirm_password" : "secretkey123"
            }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], {"username": "kindly provide a valid username"})

    def test_user_creation_empty_email(self):
        """
        This method returns error if user is created with an empty email
        """
        data = {
            "username" : "rkelly",
            "email" : "",
            "password" : "secretkey",
            "confirm_password" : "secretkey"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], {"email": "kindly provide a valid email address"})

    def test_create_user_invalid_email(self):
        """
        This method returns error if user is created with an invalid email
        """
        data = {
            "username" : "apeli",
            "email" : "apelifabischgmail.com",
            "password" : "secretsanta",
            "confirm_password" : "secretsanta"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], {"email": "kindly provide a valid email address"})

    def test_create_user_empty_password(self):
        """
        This method returns error if user is created with an empty password
        """
        data = {
            "username" : "apeli",
            "email" : "apelifabisch@gmail.com",
            "password" : "",
            "confirm_password" : "secretsanta"
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "password and confirm password should be identical")

    def test_user_create_empty_confirm_password(self):
        """
        This method returns error if user is created with an empty confirm password
        """
        data = {
            "username" : "apeli",
            "email" : "apelifabisch@gmail.com",
            "password" : "secretsanta",
            "confirm_password" : ""
        }
        response = self.client().post('/api/v1/auth/signup', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "password and confirm password should be identical")


class TestUserLogin(BaseTest):
    """
    This class contains tests for user login manipulation
    """
    def test_login_invalid_email(self):
        """
        Test a unsuccessful because of email that does not pass email regex
        """
        data = {"email" : "jasonderulo.com", "password" : "secretjason"}
        response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"email": "kindly provide a valid email address"})
        self.assertEqual(response.status_code, 400)

    def test_login_wrong_email(self):
        """
        Test a unsuccessful login because of wrong email
        """
        data = {"email" : "jason@gmail.com", "password" : "secretjason"}
        response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "invalid email address or password")
        self.assertEqual(response.status_code, 401)

    def test_login_empty_password(self):
        """
        Test a unsuccessful login because of empty password
        """
        data = {"email" : "jasonderulo@gmail.com", "password" : ""}
        response = self.client().post('/api/v1/auth/login', data=data)
        print(response.data.decode('utf-8'))
        result = json.loads(response.data.decode('utf-8'))
        print(result)
        self.assertEqual(result.get("message"), "invalid email address or password")
        self.assertEqual(response.status_code, 401)

    def test_login_wrong_password(self):
        """
        Test a unsuccessful login because of wrong password
        """
        data = {"email" : "jasonderulo@gmail.com", "password" : "mysecretjason"}
        response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "invalid email address or password")
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
