from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import GameSerializer, GameDetailSerializer
from .models import Game, Comment


class GameListView(ListAPIView):
    queryset = Game.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = GameSerializer


class GameView(RetrieveAPIView):
    queryset = Game.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = GameDetailSerializer
    lookup_field = 'slug'


# class SearchView(APIView):
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = GameSerializer

#     def post(self, request, format=None):
#         queryset = Game.objects.all()
#         data = self.request.data

#         name = data['name']
#         queryset = queryset.filter(name__iexact=name)
