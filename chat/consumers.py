# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    # *args는 값을 넣으면 함수에 변수가 튜플형태로 입력되는 것이고, **kwargs는 딕셔너리 형태로 입력되는 것이다.
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chinese = text_data_json['chinese']
        japanese = text_data_json['japanese']
        english = text_data_json['english']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'chinese': chinese,
                'japanese': japanese,
                'english': english,
            }
        )

    # json.dumps 는 파이썬 Object(Dictionary, List, Tuple 등)를 JSON 문자열로 바꿔주는 함수, JSON 인코딩
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        chinese = event['chinese']
        japanese = event['japanese']
        english = event['english']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'chinese': chinese,
            'japanese': japanese,
            'english': english,
        }))
