from django.urls import path
from .views import GameListView, GameView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', GameListView.as_view()),
    # path('search', SearchView.as_view()),
    path('<slug>', GameView.as_view()),
]
