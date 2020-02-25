from django.test import TestCase
from django.urls import reverse

from .models import Account

class UserCreationTests(TestCase):

    def setUp(self):
        # define test user credentials
        self.username = 'test_user'
        self.password = 'test_password'

    def create_user(self):
        # check if user account created response
        response = self.client.post(reverse('user-register'),
                                    {'username': self.username, 'password': self.password},
                                    content_type='application/json')
        return response

    def login_user(self):
        response = self.client.post(reverse('user-login'),
                                    {'username': self.username, 'password': self.password},
                                    content_type='application/json')
        return response

    def test_create_user(self):
        # check if user account created response
        response = self.create_user()
        users = Account.objects.all()
        self.assertEqual(self.username, str(users[0]))
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), {'message': 'Account Created Successfully'})

    def test_user_login(self):
        # create user account
        self.create_user()

        # check if created user account is able to login with refresh and access tokens provided
        response = self.login_user()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['access'])
        self.assertIsNotNone(response.json()['refresh'])

    def test_user_logout(self):
        # create user account
        self.create_user()

        # check if created user account is able to login with refresh and access tokens provided
        login_response = self.login_user()
        access_token = login_response.json()['access']
        refresh_token = login_response.json()['refresh']
        self.assertEqual(login_response.status_code, 200)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

        # check if created user account is able to logout with refresh and access tokens provided
        logout_response = self.client.post(reverse('user-logout'),
                                           {'refresh': refresh_token},
                                           content_type='application/json',
                                           **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        self.assertEqual(logout_response.status_code, 204)

    def test_user_retrieve_api_token(self):
        # create user account
        self.create_user()

        # check if created user account is able to login with refresh and access tokens provided
        login_response = self.login_user()
        access_token = login_response.json()['access']
        self.assertEqual(login_response.status_code, 200)
        self.assertIsNotNone(access_token)

        # check if user is able to generate an api token using the access token
        token_response = self.client.get(reverse('api-token'),
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        self.assertEqual(token_response.status_code, 200)
        self.assertIsNotNone(token_response.json()['token'])

    def test_user_verify_tokens(self):
        # create user account
        self.create_user()

        # check if created user account is able to login with refresh and access tokens provided
        login_response = self.login_user()
        access_token = login_response.json()['access']
        refresh_token = login_response.json()['refresh']
        self.assertEqual(login_response.status_code, 200)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

        # check if user is able to generate an api token using the access token
        token_response = self.client.get(reverse('api-token'),
                                         content_type='application/json',
                                          **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        api_token = token_response.json()['token']
        self.assertEqual(token_response.status_code, 200)
        self.assertIsNotNone(api_token)

        # verify that all three tokens are valid
        tokens = [access_token, refresh_token, api_token]
        for token in tokens:
            token_response = self.client.post(reverse('token-verify'),
                                              {'token': token},
                                              content_type='application/json')
            self.assertEqual(token_response.status_code, 200)

        # verify that invalid tokens are rejected
        token_response = self.client.post(reverse('token-verify'),
                                          {'token': 'INVALID_TOKEN'},
                                          content_type='application/json')
        self.assertNotEqual(token_response.status_code, 200)

    def test_user_refresh_token(self):
        # create user account
        self.create_user()

        # check if created user account is able to login with refresh and access tokens provided
        login_response = self.login_user()
        access_token = login_response.json()['access']
        refresh_token = login_response.json()['refresh']
        self.assertEqual(login_response.status_code, 200)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)

        # check if user is able to generate an api token using the access token
        refresh_response = self.client.post(reverse('user-refresh'),
                                            {'refresh': refresh_token},
                                            content_type='application/json',
                                            **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        self.assertEqual(refresh_response.status_code, 200)
        self.assertIsNotNone(refresh_response.json()['access'])