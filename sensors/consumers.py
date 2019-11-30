from channels.generic.websocket import AsyncWebsocketConsumer
import json


class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sensors = self.scope['url_route']['kwargs']['sensors']
        self.sensors_group_name = 'sensor_%s' % self.sensors

        # Join room group
        await self.channel_layer.group_add(
            self.sensors_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.sensors_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        lat = text_data_json['lat']
        lon = text_data_json['lon']

        # Send message to room group
        await self.channel_layer.group_send(
            self.sensors_group_name,
            {
                'type': 'sensor_message',
                'message': message,
                'lat': lat,
                'lon': lon,
            }
        )

    # Receive message from room group
    async def sensor_message(self, event):
        message = event['message']
        lat = event['lat']
        lon = event['lon']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'lat': lat,
            'lon': lon
        }))
