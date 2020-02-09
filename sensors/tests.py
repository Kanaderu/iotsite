from django.test import TestCase, SimpleTestCase, TransactionTestCase
from django.urls import reverse


class SensorRESTApiTests(TestCase):

    def setUp(self):
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

    def test_empty_sensors_list(self):
        response = self.client.get(reverse('sensor-list'),
                                   content_type='application/json',
                                   **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), {'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_generic_serializer(self):
        generic_data = {
            'sensor': 'F',
            'sensor_id': '1',
            'timestamp': '2019-10-03T19:17:10.067889-04:00',
            'coordinates': [
                -83.9972,
                39.7771
            ],
            'data': [
                {
                    'data_id': '1',
                    'type': 'Temperature',
                    'data': 19.813000,
                    'units': 'C'
                },
                {
                    'data_id': '2',
                    'type': 'Temperature',
                    'data': '16.1880',
                    'units': 'C'
                }
            ]
        }
        response = self.client.post(reverse('sensor-list'),
                                    generic_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})
        expected_response = {
            'sensor': 'F',
            'sensor_id': '1',
            'timestamp': '2019-10-03T19:17:10.067889-04:00',
            'coordinates': [-83.9972, 39.7771],
            'data': [
                {
                    'data_id': '2',
                    'type': 'Temperature',
                    'data': '16.18800000',
                    'units': 'C'
                },
                {
                    'data_id': '1',
                    'type': 'Temperature',
                    'data': '19.81300000',
                    'units': 'C'
                }
            ]
        }
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_response)

    def test_feather_serializer(self):
        feather_data = {
            'dev_id': 1,
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
            'sensor': 'F',
            'sensor_id': '1',
            'timestamp': '2019-10-02T19:17:10.067889-04:00',
            'coordinates': [
                -83.9972,
                39.7771
            ],
            'data': [
                {
                    'data_id': '1',
                    'type': 'Temperature',
                    'data': '19.81300000',
                    'units': 'C'
                },
                {
                    'data_id': '2',
                    'type': 'Temperature',
                    'data': '16.18800000',
                    'units': 'C'
                }
            ]
        }
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_response)

    def test_lora_gateway_serializer(self):
        lora_data = {
            'app_id': 'dayton-engineering-and-geology',
            'dev_id': '180291',
            'hardware_serial': '000DB5390864367B',
            'port': 2,
            'counter': 4555,
            'payload_raw': '0oCH/////w==',
            'payload_fields': {
                'b': 4.2,
                'sm1': 255,
                'sm2': 255,
                'sm3': 255,
                'sm4': 255,
                't1': 28,
                't2': 35
            },
            'metadata': {
                'time': '2019-09-29T17:17:03.147714091Z',
                'frequency': 904.9,
                'modulation': 'LORA',
                'data_rate': 'SF10BW125',
                'coding_rate': '4/5',
                'gateways': [
                    {
                        'gtw_id': 'rg1xx294cb6',
                        'gtw_trusted': True,
                        'timestamp': 10479492,
                        'time': '',
                        'channel': 5,
                        'rssi': -58,
                        'snr': 9.25,
                        'rf_chain': 1,
                        'latitude': 39.741287,
                        'longitude': -84.18488
                    }
                ]
            },
            'downlink_url': 'https://integrations.thethingsnetwork.org/ttn-us-west/api/v2/down/dayton-engineering-and-geology/webhook_test?key=ttn-account-v2.kY1MRQUoGICp7C9CAEvhEdGklPVWW-ztIiU0aVRLxno'
        }
        response = self.client.post(reverse('LoRaGateway-list'),
                                    lora_data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.api_token)})
        expected_response = {
            'sensor': 'LG',
            'sensor_id': '180291',
            'timestamp': '2019-09-29T17:17:03.147714091Z',
            'coordinates': [-84.18488, 39.741287],
            'data': [
                {
                    'data_id': 't2',
                    'type': '',
                    'data': '35.00000000',
                    'units': ''
                },
                {
                    'data_id': 't1',
                    'type': '',
                    'data': '28.00000000',
                    'units': ''
                },
                {
                    'data_id': 'sm4',
                    'type': '',
                    'data': '255.00000000',
                    'units': ''
                },
                {
                    'data_id': 'sm3',
                    'type': '',
                    'data': '255.00000000',
                    'units': ''
                },
                {
                    'data_id': 'sm2',
                    'type': '',
                    'data': '255.00000000',
                    'units': ''
                },
                {
                    'data_id': 'sm1',
                    'type': '',
                    'data': '255.00000000',
                    'units': ''
                },
                {
                    'data_id': 'b',
                    'type': '',
                    'data': '4.20000000',
                    'units': ''
                }
            ]
        }
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_response)
