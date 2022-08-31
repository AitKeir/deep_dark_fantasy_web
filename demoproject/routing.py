from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import re_path

from .wsgi import *  # add this line to top of your code
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import women.routing as routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

# from chat.consumers import ChatConsumer
# application = ProtocolTypeRouter({
# # Empty for now (http->django views is added by default)
# 'websocket': AllowedHostsOriginValidator(
#     AuthMiddlewareStack(
#         URLRouter(
#             [
#                 re_path(r'ws/chat/', ChatConsumer.as_asgi()),
#             ]
#         )
#     )
# )
# })