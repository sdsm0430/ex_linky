# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    # *args는 값을 넣으면 함수에 변수가 튜플형태로 입력되는 것이고, **kwargs는 딕셔너리 형태로 입력되는 것이다.
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'operate_%s' % self.room_name

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
        chinese_song = text_data_json['chinese_song']
        chinese_actor = text_data_json['chinese_actor']
        chinese_music = text_data_json['chinese_music']

        japanese_song = text_data_json['japanese_song']
        japanese_actor = text_data_json['japanese_actor']
        japanese_music = text_data_json['japanese_music']

        english_song = text_data_json['english_song']
        english_actor = text_data_json['english_actor']
        english_music = text_data_json['english_music']

        korean_song = text_data_json['korean_song']
        korean_actor = text_data_json['korean_actor']
        korean_music = text_data_json['korean_music']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',

                'chinese_song': chinese_song,
                'chinese_actor': chinese_actor,
                'chinese_music': chinese_music,

                'japanese_song': japanese_song,
                'japanese_actor': japanese_actor,
                'japanese_music': japanese_music,

                'english_song': english_song,
                'english_actor': english_actor,
                'english_music': english_music,

                'korean_song': korean_song,
                'korean_actor': korean_actor,
                'korean_music': korean_music,
            }
        )

    # json.dumps 는 파이썬 Object(Dictionary, List, Tuple 등)를 JSON 문자열로 바꿔주는 함수, JSON 인코딩
    # Receive message from room group
    async def chat_message(self, event):
        chinese_song = event['chinese_song']
        chinese_actor = event['chinese_actor']
        chinese_music = event['chinese_music']

        japanese_song = event['japanese_song']
        japanese_actor = event['japanese_actor']
        japanese_music = event['japanese_music']

        english_song = event['english_song']
        english_actor = event['english_actor']
        english_music = event['english_music']

        korean_song = event['korean_song']
        korean_actor = event['korean_actor']
        korean_music = event['korean_music']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'chinese_song': chinese_song,
            'chinese_actor': chinese_actor,
            'chinese_music': chinese_music,

            'japanese_song': japanese_song,
            'japanese_actor': japanese_actor,
            'japanese_music': japanese_music,

            'english_song': english_song,
            'english_actor': english_actor,
            'english_music': english_music,

            'korean_song': korean_song,
            'korean_actor': korean_actor,
            'korean_music': korean_music,
        }))
