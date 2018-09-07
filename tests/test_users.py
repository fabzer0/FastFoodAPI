"""
This module facilitates Testing
"""
import unittest
import json
import sys
import os
import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


app = app.create_app()
app.config.from_object('config.Testing')


class UserTest(unittest.TestCase):
    """
    This class contains tests for users manipulation
    """

    def setUp(self):
        self.app = app.test_client()
        self.data = json.dumps(
            {
                "username" : "fabischapeli",
                "email" : "fabischapeli97@gmail.com",
                "password" : "pass123",
                "confirm_password" : "pass123"
            }
        )

        self.existing_user = self.app.post("/api/v1/auth/signup",
                                           data=self.data, content_type='application/json')


    #'/api/v1/auth/signup'
    def test_successful_user_creation(self):
        """
        This method tests if a user is successfully created
        """
        data = json.dumps(
            {
                "username" : "rkelly",
                "email" : "rkelly@gmail.com",
                "password" : "secret12345",
                "confirm_password" : "secret12345"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("username"), "rkelly")
        self.assertEqual(result.get("email"), "rkelly@gmail.com")
        self.assertEqual(result.get("password"), "secret12345")
        self.assertEqual(response.status_code, 201)

    def test_user_creation_existing_email(self):
        """
        This method should return error if user created already exist
        """
        data = json.dumps(
            {
                "username" : "rkelly",
                "email" : "rkelly@gmail.com",
                "password" : "secret1234",
                "confirm_password" : "secret1234"
            }
        )
        self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "user with that email already exist")

    def test_user_creation_non_identical_passwords(self):
        """
        This method return error if user provides un identical passwors during registration
        """
        data = json.dumps(
            {
                "username" : "rkelly",
                "email" : "nikkita@gmail.com",
                "password" : "secret",
                "confirm_password" : "secret123"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "password and confirm password should be identical")

    def test_user_creation_short_password(self):
        """
        This method returns error is password is too short during registration
        """
        data = json.dumps(
            {
                "username" : "rkelly",
                "email" : "geazy@gmail.com",
                "password" : "sec",
                "confirm_password" : "sec"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "password should be atleast 8 characters")

    def test_create_user_empty_username(self):
        """
        This method returns error if user is created with an empty username
        """
        data = json.dumps(
            {
                "username" : "",
                "email" : "geazy@gmail.com",
                "password" : "sec",
                "confirm_password" : "secretkey123"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"username": "kindly provide a valid username"})

    def test_user_creation_empty_email(self):
        """
        This method returns error if user is created with an empty email
        """
        data = json.dumps(
            {
                "username" : "rkelly",
                "email" : "",
                "password" : "secretkey",
                "confirm_password" : "secretkey"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"email": "kindly provide a valid email address"})

    def test_create_user_invalid_email(self):
        """
        This method returns error if user is created with an invalid email
        """
        data = json.dumps(
            {
                "username" : "apeli",
                "email" : "apelifabischgmail.com",
                "password" : "secretsanta",
                "confirm_password" : "secretsanta"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), {"email": "kindly provide a valid email address"})

    def test_create_user_empty_password(self):
        """
        This method returns error if user is created with an empty password
        """
        data = json.dumps(
            {
                "username" : "apeli",
                "email" : "apelifabisch@gmail.com",
                "password" : "",
                "confirm_password" : "secretsanta"
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "password and confirm password should be identical")

    def test_user_create_empty_confirm_password(self):
        """
        This method returns error if user is created with an empty confirm password
        """
        data = json.dumps(
            {
                "username" : "apeli",
                "email" : "apelifabisch@gmail.com",
                "password" : "secretsanta",
                "confirm_password" : ""
            }
        )
        response = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get("message"), "password and confirm password should be identical")


    #'/api/v1/users'
    def test_get_all_users(self):
        """
        This method returns all users
        """
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_get_one_user(self):
        """
        This method returns one user
        """
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_user(self):
        """
        This method returns error if trying to get non-existing user
        """
        data = json.dumps(
            {
                "username" : "fabischapeli",
                "email" : "fabischapeli97@gmail.com",
                "password" : "pass12342",
                "confirm_password" : "pass12342"
            }
        )
        response1 = self.app.post('/api/v1/auth/signup', data=data, content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        response2 = self.app.get('/api/v1/users/2')
        self.assertEqual(response2.status_code, 401)

    def test_successful_user_update(self):
        """
        This method successfully updates user
        """
        data = json.dumps(
            {
                "username" : "fabischapeli",
                "email" : "fabischapeli97@gmail.com",
                "password" : "pass12342",
                "confirm_password" : "pass12342"
            }
        )
        response = self.app.put('/api/v1/users/2', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_updating_non_existing_user(self):
        """
        This method returns error if non-existing user is updated
        """
        data = json.dumps(
            {
                "username" : "graceunah",
                "email" : "graceunah@gmail.com",
                "password" : "secret12345",
                "confirm_password" : "secret12345"
            }
        )
        response = self.app.put('/api/v1/users/99', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_successful_user_deletion(self):
        """
        This method tests successful user deletion
        """
        response = self.app.delete('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

    def test_deleting_non_existing_user(self):
        """
        This method returns error if user that doesnt exist is deleted
        """
        response = self.app.delete('/api/v1/users/23')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
