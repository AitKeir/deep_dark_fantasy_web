# Импорт для работы с JSON
import json, random
# Импорт для асинхронного программирования
import re

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
# Импорт для работы с БД в асинхронном режиме
from channels.db import database_sync_to_async
# Импорт модели сообщений
from .models import *
from women.models import *


# Класс ChatConsumer
class ChatConsumer(AsyncWebsocketConsumer):

    # Метод подключения к WS
    async def connect(self):
        # Назначим пользователя в комнату
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Добавляем новую комнату
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Принимаем подключаем
        await self.accept()

    # Метод для отключения пользователя
    async def disconnect(self, close_code):
        # Отключаем пользователя
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Декоратор для работы с БД в асинхронном режиме
    @database_sync_to_async
    # Функция для создания нового сообщения в БД
    def new_message(
            self,
            message,
            type1,
            player,
            rolled=False,
            strroll='0',
            sumroll=0,
            plusroll=0
    ):
        # Создаём сообщение в БД
        Message.objects.create(
            message=message,
            type=type1,
            player=player,
            rolled=rolled,
            strRoll=strroll,
            sumRoll=sumroll,
            plusRoll=plusroll
        )

    @database_sync_to_async
    def get_pers(self, room):
        game = Game.objects.get(name=room)
        squads = game.squad_set.all()
        for squad in squads:
            players = squad.squad.all()
            for player in players:
                if player.user_id == self.scope["user"].id:
                    return player

    @database_sync_to_async
    def get_roll(self, message):
        nums = re.findall(r'\d+', message)
        rolls = []
        while int(nums[0]) > 0:
            rolls.append(random.randint(1, int(nums[1])))
            nums[0] = int(nums[0]) - 1
        sumRoll = sum(rolls)
        strRoll = '('
        strRoll += " + ".join(f"{n}" for n in rolls)
        strRoll += ')'
        if '+' in message:
            sumRoll += int(nums[2])
            strRoll += f'+{nums[2]}'
            # message += f' {strRoll} = {sumRoll}'
            # return message, strRoll, sumRoll, nums[2]
            return strRoll, sumRoll, nums[2]
        else:
            # message += f' {strRoll} = {sumRoll}'
            # return message, strRoll, sumRoll, 0
            return strRoll, sumRoll, 0


    # Принимаем сообщение от пользователя
    async def receive(self, text_data=None, bytes_data=None):
        # Форматируем сообщение из JSON
        text_data_json = json.loads(text_data)
        # Получаем текст сообщения
        message = text_data_json['message']
        rolls = '0'
        sumroll = 0
        plusroll = 0
        rolled = 0

        if '/roll' in message:
            message = message.replace('/roll ', '')
            rolls, sumroll, plusroll = await self.get_roll(message)
            rolled = 1

        playerNow = await self.get_pers(
            room=self.scope['url_route']['kwargs']['room_name']
        )

        # Добавляем сообщение в БД
        if rolled == 1:
            await self.new_message(
                message=message,
                type1=self.scope['url_route']['kwargs']['room_name'],
                player=playerNow,
                rolled=True,
                strroll=rolls,
                sumroll=sumroll,
                plusroll=plusroll
            )
        else:
            await self.new_message(
                message=message,
                type1=self.scope['url_route']['kwargs']['room_name'],
                player=playerNow
            )

        # print(playerNow.photo)

        # Отправляем сообщение
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': playerNow.name,
                'avatar': playerNow.photo.url,
                'rolls': rolls,
                'sumroll': sumroll,
                'plusroll': plusroll,
            }
        )

    # Метод для отправки сообщения клиентам
    async def chat_message(self, event):
        # Получаем сообщение от receive
        message = event['message']
        # Отправляем сообщение клиентам
        await self.send(text_data=json.dumps({
            'message': message,
            'name': event['name'],
            'avatar': event['avatar'],
            'rolls': event['rolls'],
            'sumroll': event['sumroll'],
            'plusRoll': event['plusroll'],
        }))