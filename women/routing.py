from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/maps/(?P<game_slug>\w+)/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/maps/<game_slug>/<room_name>/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/maps/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]