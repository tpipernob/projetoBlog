from django.urls import path
from .views import *

urlpatterns = [
    path('', postagem, name='home'),
    path('post/<int:pk>', postagem_list, name='post'),
]