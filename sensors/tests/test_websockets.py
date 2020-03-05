import pytest
import json

from django.conf.urls import url
from django.urls import reverse

from channels.routing import URLRouter
from channels.testing import HttpCommunicator
from channels.testing import WebsocketCommunicator

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer,
    AsyncWebsocketConsumer,
    JsonWebsocketConsumer,
    WebsocketConsumer,
)

from iotsite.asgi import application
from sensors.consumers import SensorConsumer


@pytest.mark.asyncio
async def test_my_consumer():
    print('in test!')
    '''
    communicator = HttpCommunicator(SensorConsumer, "GET", "/test/")
    response = await communicator.get_response()
    assert response["body"] == b"test response"
    assert response["status"] == 200
    '''

#@pytest.mark.asyncio
#async def test_generic_websocket_consumer():
#
#    results = {}
#
#    '''
#    class TestConsumer(AsyncWebsocketConsumer):
#        async def connect(self):
#            results["connected"] = True
#            await self.accept()
#
#        async def receive(self, text_data=None, bytes_data=None):
#            results["received"] = (text_data, bytes_data)
#            await self.send(text_data=text_data, bytes_data=bytes_data)
#
#        async def disconnect(self, code):
#            results["disconnected"] = code
#    '''
#
#    #communicator = WebsocketCommunicator(SensorConsumer, "/live/test/")
#    communicator = WebsocketCommunicator(SensorConsumer, "/live/test/")
#    connected, subprotocol = await communicator.connect()
#    print('testing if true')
#    print(connected)
#    assert connected
#
#    await communicator.disconnect()
#    '''
#    communicator = WebsocketCommunicator(SimpleWebsocketApp, "/testws/")
#    connected, subprotocol = await communicator.connect()
#    assert connected
#    # Test sending text
#    await communicator.send_to(text_data="hello")
#    response = await communicator.receive_from()
#    assert response == "hello"
#    # Close
#    await communicator.disconnect()
#    '''

@pytest.mark.asyncio
@pytest.mark.filterwarnings('ignore::DeprecationWarning')
async def test_async_websocket_initialization():
    # initialize communicator for application
    communicator = WebsocketCommunicator(application, "live/test_room/")

    # connect
    connected, subprotocol = await communicator.connect()
    assert connected

    # verify initial connection response
    str_response = await communicator.receive_from()
    response = json.loads(str_response)

    assert response['type'] == 'sensor_initialize'
    assert response['linkstations'] == reverse('linkstations')

    # disconnect
    await communicator.disconnect()

@pytest.mark.asyncio
@pytest.mark.filterwarnings('ignore::DeprecationWarning')
async def test_async_websocket_send_coordinates():
    # initialize communicator for application
    communicator = WebsocketCommunicator(application, "live/test_room/")

    # connect
    connected, subprotocol = await communicator.connect()
    assert connected

    # verify client-sent data is broadcasted
    send_data = {
        'type': 'sensor_message',
        'message': 'UUID_1',
        'lat': 10.1234,
        'lon': -13.2345,
    }
    await communicator.send_to(text_data=json.dumps(send_data))
    response = await communicator.receive_from()
    assert json.loads(response) == send_data

    # disconnect
    await communicator.disconnect()