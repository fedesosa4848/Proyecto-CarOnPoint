# urls.py
from django.urls import path
from .views import inbox, send_message,send_md

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('send/', send_message, name='send_message'),
    path('send_message/<int:user_id>/', send_md, name='send_message'),
]
