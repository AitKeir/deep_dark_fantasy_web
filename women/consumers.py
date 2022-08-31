# Импорт для работы с JSON
import json, random
# Импорт для асинхронного программирования
import re

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# Импорт для работы с БД в асинхронном режиме
from channels.db import database_sync_to_async
# Импорт модели сообщений
from women.models import *
from chat.models import *

# Класс ChatConsumer
class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def add_to_group(self):
        user_id = self.scope["user"].id
        group = Ch_groups.objects.get_or_create(
            name=f"{self.scope['url_route']['kwargs']['game_slug']}/{self.scope['url_route']['kwargs']['room_name']}"
        )[0]
        if not group.pers:
            group.pers = f';{user_id}'
            group.save()
        elif f'{user_id}' not in group.pers:
            group.pers += f';{user_id}'
            group.save()

    @database_sync_to_async
    def delete_to_group(self):
        user_id = self.scope["user"].id
        group = Ch_groups.objects.get(
            name=f"{self.scope['url_route']['kwargs']['game_slug']}/{self.scope['url_route']['kwargs']['room_name']}"
        )
        if f'{user_id}' in group.pers:
            group.pers = group.pers.replace(f';{user_id}', '')
            group.save()

    # Метод подключения к WS
    async def connect(self):
        # Назначим пользователя в комнату
        self.room_name = f"{self.scope['url_route']['kwargs']['game_slug']}_{self.scope['url_route']['kwargs']['room_name']}"
        self.room_group_name = 'maps_%s' % self.room_name

        # print(self.scope['url_route']['kwargs']['room_name'])

        # Добавляем новую комнату
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.add_to_group()
        # Принимаем подключаем
        await self.accept()

    # Метод для отключения пользователя
    async def disconnect(self, close_code):
        await self.delete_to_group()
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
            plusroll=0,
            photo="players/default.png",
            name='default'
    ):
        # Создаём сообщение в БД
        Message.objects.create(
            message=message,
            type=type1,
            player=player,
            rolled=rolled,
            strRoll=strroll,
            sumRoll=sumroll,
            plusRoll=plusroll,
            photo=photo,
            name=name
        )

    @database_sync_to_async
    def get_pers(self, game_slug):
        game = Game.objects.get(slug=game_slug)
        squads = game.squad_set.all()
        for squad in squads:
            players = squad.squad.all()
            for player in players:
                if player.user_id == self.scope["user"].id:
                    return player

    @database_sync_to_async
    def get_roll(self, message):

        nums = self.get_numbers_of_roll(message)
        rolls, strRoll, sumRoll, plus = self.rolls(
            nums=int(nums[0]),
            end=int(nums[1]),
            plus=int(nums[2])
        )
        return strRoll, sumRoll, plus

    @database_sync_to_async
    def get_roll_attack(self, pers, nums=1, enemy_evade=4):

        attr_tt = pers.attr_tt
        # attr_ch = pers.attr_ch
        # attr = pers.attr

        if attr_tt.energy == 0:
            self.change_attr(pers=pers, energy=1)
            result = 'Не хватает энергии на удар'
        else:
            rolls_hit, str_roll, sum_roll, plus = self.rolls(
                nums=nums,
                plus=attr_tt.hit
            )
            self.change_attr(pers=pers, energy=-1)
            best_roll_hit = 0
            for roll in rolls_hit:
                if roll > best_roll_hit:
                    best_roll_hit = roll
            if best_roll_hit == 1:
                result = 'Автопромах!'
            elif best_roll_hit == 6:
                result = 'Автопопадание!'
            else:
                if sum_roll > enemy_evade:
                    result = 'Попадание!'
                else:
                    result = 'Промах!'
        return result

    # Функция обработки сообщения о роле
    def get_numbers_of_roll(self, nums):
        nums = re.findall(r'\d+', nums)
        if len(nums) > 2:
            return nums[0], nums[1], nums[2]
        elif len(nums) == 2:
            return nums[0], nums[1], 0
        elif len(nums) == 1:
            return nums[0], 6, 0
        else:
            return 1, 6, 0

    # Функция обработки ролов
    def rolls(self, nums, start=1, end=6, plus=0):
        rolls = []
        while nums > 0:
            rolls.append(random.randint(start, end))
            nums -= 1
        strRoll = f'({" + ".join(f"{n}" for n in rolls)})'
        sumRoll = sum(rolls)
        if plus != 0:
            strRoll += f'+{plus}'
            sumRoll += plus
        return rolls, strRoll, sumRoll, plus

    # Функция изменения атрибутов
    def change_attr(
            self,
            pers,
            energy=0,
            regenEnergy=0,
            haste=0,
            hit=0,
            dmg='0/0/0',
            arp=0,
            hp=0,
            regenHp=0,
            regenHpDaily=0,
            evade=0,
            armor=0,
            magicArmor=0,
            magicResist=0,
            mp=0,
            regenMp=0,
            regenMpDaily=0,
            magicPenetration=0,
            magicIgnore=0,
            magicDirDmg=0,
            magicPeriodicDmg=0,
            poisonPeriodicDmg=0,
            bleedingPeriodicDmg=0
    ):
        attr_tt = pers.attr_tt
        attr_ch = pers.attr_ch
        attr = pers.attr

        # Блок временных атрибутов
        attr_ch.energy += energy
        attr_ch.regenEnergy += regenEnergy
        attr_ch.haste += haste
        attr_ch.hit += hit
        dmg_min_new = int(dmg.split('/')[0])
        dmg_mid_new = int(dmg.split('/')[1])
        dmg_max_new = int(dmg.split('/')[2])
        dmg_min_now = int(attr_ch.dmg.split('/')[0]) + dmg_min_new
        dmg_mid_now = int(attr_ch.dmg.split('/')[1]) + dmg_mid_new
        dmg_max_now = int(attr_ch.dmg.split('/')[2]) + dmg_max_new
        attr_ch.dmg = f'{dmg_min_now}/{dmg_mid_now}/{dmg_max_now}'
        attr_ch.arp += arp
        attr_ch.hp += hp
        attr_ch.regenHp += regenHp
        attr_ch.regenHpDaily += regenHpDaily
        attr_ch.evade += evade
        attr_ch.armor += armor
        attr_ch.magicArmor += magicArmor
        attr_ch.magicResist += magicResist
        attr_ch.mp += mp
        attr_ch.regenMp += regenMp
        attr_ch.regenMpDaily += regenMpDaily
        attr_ch.magicPenetration += magicPenetration
        attr_ch.magicIgnore += magicIgnore
        attr_ch.magicDirDmg += magicDirDmg
        attr_ch.magicPeriodicDmg += magicPeriodicDmg
        attr_ch.poisonPeriodicDmg += poisonPeriodicDmg
        attr_ch.bleedingPeriodicDmg += bleedingPeriodicDmg

        # Блок итоговых атрибутов
        attr_tt.energy = attr.energy + attr_ch.energy
        attr_tt.regenEnergy = attr.regenEnergy + attr_ch.regenEnergy
        attr_tt.haste = attr.haste + attr_ch.haste
        attr_tt.hit = attr.hit + attr_ch.hit
        dmg_min_st = int(attr.dmg.split('/')[0])
        dmg_mid_st = int(attr.dmg.split('/')[1])
        dmg_max_st = int(attr.dmg.split('/')[2])
        attr_tt.dmg = f'{dmg_min_st+dmg_min_now}/{dmg_mid_st+dmg_mid_now}/{dmg_max_st+dmg_max_now}'
        attr_tt.arp = attr.arp + attr_ch.arp
        attr_tt.hp = attr.hp + attr_ch.hp
        attr_tt.regenHp = attr.regenHp + attr_ch.regenHp
        attr_tt.regenHpDaily = attr.regenHpDaily + attr_ch.regenHpDaily
        attr_tt.evade = attr.evade + attr_ch.evade
        attr_tt.armor = attr.armor + attr_ch.armor
        attr_tt.magicArmor = attr.magicArmor + attr_ch.magicArmor
        attr_tt.magicResist = attr.magicResist + attr_ch.magicResist
        attr_tt.mp = attr.mp + attr_ch.mp
        attr_tt.regenMp = attr.regenMp + attr_ch.regenMp
        attr_tt.regenMpDaily = attr.regenMpDaily + attr_ch.regenMpDaily
        attr_tt.magicPenetration = attr.magicPenetration + attr_ch.magicPenetration
        attr_tt.magicIgnore = attr.magicIgnore + attr_ch.magicIgnore
        attr_tt.magicDirDmg = attr.magicDirDmg + attr_ch.magicDirDmg
        attr_tt.magicPeriodicDmg = attr.magicPeriodicDmg + attr_ch.magicPeriodicDmg
        attr_tt.poisonPeriodicDmg = attr.poisonPeriodicDmg + attr_ch.poisonPeriodicDmg
        attr_tt.bleedingPeriodicDmg = attr.bleedingPeriodicDmg + attr_ch.bleedingPeriodicDmg

        attr_ch.save()
        attr_tt.save()

    # Принимаем сообщение от пользователя
    async def receive(self, text_data=None, bytes_data=None):
        print('check2')
        # Форматируем сообщение из JSON
        text_data_json = json.loads(text_data)
        # Получаем текст сообщения
        message = text_data_json['message']
        rolls = '0'
        sumroll = 0
        plusroll = 0
        rolled = 0

        playerNow = await self.get_pers(
            game_slug=self.scope['url_route']['kwargs']['game_slug']
        )
        print('get_player')

        if '/roll' in message:
            message = message.replace('/roll ', '')
            rolls, sumroll, plusroll = await self.get_roll(
                message=message,
            )
            rolled = 1

        elif '/attack' in message:
            message = await self.get_roll_attack(
                pers=playerNow
            )

        # Добавляем сообщение в БД
        if rolled == 1:
            await self.new_message(
                message=message,
                type1=f"{self.scope['url_route']['kwargs']['game_slug']}_{self.scope['url_route']['kwargs']['room_name']}",
                player=playerNow,
                rolled=True,
                strroll=rolls,
                sumroll=sumroll,
                plusroll=plusroll,
                photo=playerNow.photo,
                name=playerNow.name
            )
        else:
            await self.new_message(
                message=message,
                type1=f"{self.scope['url_route']['kwargs']['game_slug']}_{self.scope['url_route']['kwargs']['room_name']}",
                player=playerNow,
                photo=playerNow.photo,
                name=playerNow.name
            )

        print('sended mes')

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
        # message = event['message']
        # Отправляем сообщение клиентам
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'name': event['name'],
            'avatar': event['avatar'],
            'rolls': event['rolls'],
            'sumroll': event['sumroll'],
            'plusRoll': event['plusroll'],
        }))