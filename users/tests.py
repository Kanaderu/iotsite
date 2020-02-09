import json
from django.test import TestCase
from django.urls import reverse


class UserCreationTests(TestCase):

    def setUp(self):
        # define test user credentials
        self.username = 'test_user'
        self.password = 'test_password'

    def test_create_user(self):
        # check if user account created response
        response = self.client.post(reverse('user-register'),
                                    {'username': self.username, 'password': self.password},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), {'message': 'Account Created Successfully'})

    def test_user_login(self):
        # create user account
        self.test_create_user()

        # check if created user account is able to login with refresh and access tokens provided
        response = self.client.post(reverse('user-login'),
                                    {'username': self.username, 'password': self.password},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['access'])
        self.assertIsNotNone(response.json()['refresh'])

    def test_user_retrieve_api_token(self):
        # create user account
        self.test_create_user()

        # check if created user account is able to login with refresh and access tokens provided
        login_response = self.client.post(reverse('user-login'),
                                    {'username': self.username, 'password': self.password},
                                    content_type='application/json')
        self.assertEqual(login_response.status_code, 200)

        access_token = login_response.json()['access']
        self.assertIsNotNone(access_token)

        token_response = self.client.get(reverse('api-token'),
                                   content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        self.assertEqual(token_response.status_code, 200)
        self.assertIsNotNone(token_response.json()['token'])