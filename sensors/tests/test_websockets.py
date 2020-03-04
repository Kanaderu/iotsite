import pytest
from channels.testing import HttpCommunicator
from channels.testing import WebsocketCommunicator
from sensors.consumers import SensorConsumer

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

@pytest.mark.asyncio
async def test_async_websocket_consumer():

    results = {}

    class TestConsumer(AsyncWebsocketConsumer):
        async def connect(self):
            results["connected"] = True
            await self.accept()

        async def receive(self, text_data=None, bytes_data=None):
            results["received"] = (text_data, bytes_data)
            await self.send(text_data=text_data, bytes_data=bytes_data)

        async def disconnect(self, code):
            results["disconnected"] = code

    communicator = WebsocketCommunicator(TestConsumer, "/testws/")
    connected, subprotocol = await communicator.connect()
    assert connected

    await communicator.disconnect()
    '''
    communicator = WebsocketCommunicator(SimpleWebsocketApp, "/testws/")
    connected, subprotocol = await communicator.connect()
    assert connected
    # Test sending text
    await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    assert response == "hello"
    # Close
    await communicator.disconnect()
    '''