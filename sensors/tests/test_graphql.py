import pytest
from django.urls import reverse
from graphene_django.utils.testing import GraphQLTestCase

from django.contrib.gis.geos import Point

from iotsite.schema import schema
from sensors.models import Sensor, SensorData


class SensorGraphQLTests(GraphQLTestCase):
    # setup schema for test case
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        instance = Sensor.objects.create(sensor='LG', sensor_id='some_sensor_id',
                                         coordinates=Point(x=1.31415, y=-5.4321, srid=4326),
                                         timestamp='2019-10-02T19:17:10.067889-04:00')
        SensorData.objects.create(sensor=instance, type='blue', data_id='blue_data', data=10)
        SensorData.objects.create(sensor=instance, type='green', data_id='green_data', data=12)

    @pytest.mark.filterwarnings('ignore::DeprecationWarning')
    def test_graphql_endpoint(self):
        query = '''
            {
                sensors {
                    sensorId
                    timestamp
                    coordinates
                    data {
                        type
                        data
                        units
                    }
                }
            }
            '''
        response = self.client.post(reverse('graphql'),
                                   {'query': query},
                                   content_type='application/json')
        expected_response = {
            'data': {
                'sensors': [
                    {
                        'sensorId': 'some_sensor_id',
                        'timestamp': '2019-10-02T23:17:10.067889+00:00',
                        'coordinates': {
                            'type': 'Point',
                            'coordinates': [1.31415, -5.4321]
                        },
                        'data': [
                            {
                                'type': 'green',
                                'data': 12.0,
                                'units': ''
                            },
                            {
                                'type': 'blue',
                                'data': 10.0,
                                'units': ''
                            }
                        ]
                    }
                ]
            }
        }
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, expected_response)

    def test_list_sensors_query(self):
        response = self.query(
            '''
            query {
                sensors {
                    sensorId
                    timestamp
                    coordinates
                    data {
                        type
                        data
                        units
                    }
                }
            }
            ''',
            op_name='list_sensors'
        )
        expected_response = {
            'data': {
                'sensors': [
                    {
                        'sensorId': 'some_sensor_id',
                        'timestamp': '2019-10-02T23:17:10.067889+00:00',
                        'coordinates': {
                            'type': 'Point',
                            'coordinates': [1.31415, -5.4321]
                        },
                        'data': [
                            {
                                'type': 'green',
                                'data': 12.0,
                                'units': ''
                            },
                            {
                                'type': 'blue',
                                'data': 10.0,
                                'units': ''
                            }
                        ]
                    }
                ]
            }
        }
        self.assertJSONEqual(response.content, expected_response)
        self.assertResponseNoErrors(response)

    def test_list_sensor_data_query(self):
        response = self.query(
            '''
            query {
                sensorData{
                    sensor {
                        timestamp
                    }
                    type
                    data
                    units
                }
            }
            ''',
            op_name='list_sensor_data'
        )
        expected_response = {
            'data': {
                'sensorData': [
                    {
                        'sensor': {
                            'timestamp': '2019-10-02T23:17:10.067889+00:00'
                        },
                        'type': 'blue',
                        'data': 10.0,
                        'units': ''
                    },
                    {
                        'sensor': {
                            'timestamp': '2019-10-02T23:17:10.067889+00:00'
                        },
                        'type': 'green',
                        'data': 12.0,
                        'units': ''
                    }
                ]
            }
        }
        self.assertJSONEqual(response.content, expected_response)
        self.assertResponseNoErrors(response)