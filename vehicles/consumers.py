from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VehicleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.vehicles = self.scope['url_route']['kwargs']['vehicles']
        self.vehicles_group_name = 'vehicle_%s' % self.vehicles

        # Join room group
        await self.channel_layer.group_add(
            self.vehicles_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.vehicles_group_name,
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
            self.vehicles_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'lat': lat,
                'lon': lon,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        lat = event['lat']
        lon = event['lon']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'lat': lat,
            'lon': lon
        }))
