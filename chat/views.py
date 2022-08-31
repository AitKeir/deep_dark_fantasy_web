from django.shortcuts import render
from django.views import generic

from chat.models import *


def chat(request):
    return render(request, 'room.html')

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    messageHistory = Message.objects.filter(type=room_name)
    return render(request, 'room_new.html', {
        'room_name': room_name,
        'messageHistory': messageHistory
    })

# class IndexView(generic.View):
#
#     def get(self, request):
#         # Показ последних 10 сообщений
#         chat_queryset = ChatMessage.objects.order_by("-created")[:10]
#         chat_message_count = len(chat_queryset)
#         if chat_message_count > 0:
#             first_message_id = chat_queryset[len(chat_queryset) - 1].id
#         else:
#             first_message_id = -1
#         previous_id = -1
#         if first_message_id != -1:
#             try:
#                 previous_id = ChatMessage.objects.filter(pk__lt=first_message_id).order_by("-pk")[:1][0].id
#             except IndexError:
#                 previous_id = -1
#         chat_messages = reversed(chat_queryset)
#
#         return render(request, "chatdemo/chatroom.html", {
#             'chat_messages': chat_messages,
#             'first_message_id': previous_id,
#         })