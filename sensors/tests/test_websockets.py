import pytest
from channels.testing import HttpCommunicator
from channels.testing import WebsocketCommunicator
from sensors.consumers import SensorConsumer

from django.conf.urls import url
from channels.routing import URLRouter

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer,
    AsyncWebsocketConsumer,
    JsonWebsocketConsumer,
    WebsocketConsumer,
)

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
async def test_async_websocket_consumer():
    print('Attempting to test websocket')
    # URLRouter from routing
    application = URLRouter([url(r"^live/(?P<sensors>\w+)/$", SensorConsumer)])
    communicator = WebsocketCommunicator(application, "live/e/")
    connected, subprotocol = await communicator.connect()
    assert connected