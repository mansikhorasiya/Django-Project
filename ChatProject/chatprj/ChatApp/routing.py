from django.urls import path
from .consumers import ChatConsumer

websocket_urlspatterns =[
    path('ws/notification/<str:room_name>/',ChatConsumer.as_asgi()),
    
]