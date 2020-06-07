from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('games', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game_detail'),
]
