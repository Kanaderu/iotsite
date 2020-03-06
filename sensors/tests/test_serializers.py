import pytest
import json
from django.test import TestCase
from django.urls import reverse
from sensors.models import Sensor


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


class SensorSerializersTests(TestCase):

    def setUp(self):
        self.maxDiff = None

        # define test user credentials
        self.username = 'test_user'
        self.password = 'test_password'

        # create user
        create_user_response = self.client.post(reverse('user-register'),
                                                {'username': self.username, 'password': self.password},
                                                content_type='application/json')
        self.assertEqual(create_user_response.status_code, 201)

        # login user
        login_response = self.client.post(reverse('user-login'),
                                          {'username': self.username, 'password': self.password},
                                          content_type='application/json')
        access_token = login_response.json()['access']
        self.assertEqual(login_response.status_code, 200)

        # get user api token
        token_response = self.client.get(reverse('api-token'),
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token)})
        self.api_token = token_response.json()['token']
        self.assertIsNotNone(self.api_token)

    def test_feather_serializer_missing_dev_id(self):
        feather_data = {
            'metadata': {
                'location': 'Apartment',
                'latitude': 39.77710000,
                'longitude': -83.99720000,
                'time': '2019-10-02T19:17:10.067889-04:00'
            },
            'data': [
                {
                    'sensor_id': 1,
                    'sensor_type': "Temperature",
                    'sensor_data': 19.813,
                    'sensor_units': "C"
                },
                {
                    'sensor_id': 2,
                    'sensor_type': "Temperature",
                    'sensor_data': 16.188,
                    'sensor_units': 'C'
                }
            ]
        }
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'dev_id': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

    def test_feather_serializer_missing_metadata(self):
        feather_data = {
            'dev_id': 1,
            'data': [
                {
                    'sensor_id': 1,
                    'sensor_type': "Temperature",
                    'sensor_data': 19.813,
                    'sensor_units': "C"
                },
                {
                    'sensor_id': 2,
                    'sensor_type': "Temperature",
                    'sensor_data': 16.188,
                    'sensor_units': 'C'
                }
            ]
        }
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'metadata': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

    def test_feather_serializer_incorrect_metadata(self):
        # test missing metadata
        feather_data = {
            'dev_id': 1,
            'metadata': None,
            'data': [
                {
                    'sensor_id': 1,
                    'sensor_type': "Temperature",
                    'sensor_data': 19.813,
                    'sensor_units': "C"
                },
                {
                    'sensor_id': 2,
                    'sensor_type': "Temperature",
                    'sensor_data': 16.188,
                    'sensor_units': 'C'
                }
            ]
        }
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'metadata': 'This field must be a nested JSON.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test latitude None
        metadata = {
            'location': 'Apartment',
            'latitude': None,
            'longitude': -83.99720000,
            'time': '2019-10-02T19:17:10.067889-04:00'
        }
        feather_data['metadata'] = metadata
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'latitude': 'This field must be a number.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test longitude None
        feather_data['metadata']['latitude'] = -83.99720000
        feather_data['metadata']['longitude'] = None
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'longitude': 'This field must be a number.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test missing longitude
        feather_data['metadata'].pop('longitude')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'longitude': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test missing latitude
        feather_data['metadata']['longitude'] = 12.12345
        feather_data['metadata'].pop('latitude')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'latitude': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test missing time
        feather_data['metadata']['latitude'] = 12.12345
        feather_data['metadata'].pop('time')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'time': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        # test invalid time
        feather_data['metadata']['time'] = 1234
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'time': 'This field must be a string in ISO-8601 format.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

    def test_feather_serializer_missing_data(self):
        feather_data = {
            'dev_id': 1,
            'metadata': {
                'location': 'Apartment',
                'latitude': 39.77710000,
                'longitude': -83.99720000,
                'time': '2019-10-02T19:17:10.067889-04:00'
            }
        }
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'data': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

    def test_feather_serializer_incorrect_data(self):
        feather_data = {
            'dev_id': 1,
            'metadata': {
                'location': 'Apartment',
                'latitude': 39.77710000,
                'longitude': -83.99720000,
                'time': '2019-10-02T19:17:10.067889-04:00'
            },
            'data': None
        }
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'data': 'This field must be a list.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        feather_data['data'] = [{
            'sensor_type': "Temperature",
            'sensor_data': 19.813,
            'sensor_units': "C"
        }]
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'sensor_id': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        feather_data['data'][0]['sensor_id'] = 1
        feather_data['data'][0].pop('sensor_type')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'sensor_type': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        feather_data['data'][0]['sensor_type'] = 'Temperature'
        feather_data['data'][0].pop('sensor_data')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'sensor_data': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)

        feather_data['data'][0]['sensor_data'] = 123.45
        feather_data['data'][0].pop('sensor_units')
        response = self.client.post(reverse('Feather-list'),
                                    feather_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})

        expected_response = {
            'sensor_units': 'This field is required.'
        }

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, expected_response)