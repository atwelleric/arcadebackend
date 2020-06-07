from rest_framework import serializers
from .models import Game, Comment

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'img_source', 'about', 'creator_info',]
