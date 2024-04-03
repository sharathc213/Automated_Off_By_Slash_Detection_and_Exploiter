from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/output/', RealtimeOutput.as_asgi()),
]