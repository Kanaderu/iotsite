import pytest
from channels.testing import HttpCommunicator
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