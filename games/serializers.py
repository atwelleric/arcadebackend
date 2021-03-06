from rest_framework import serializers
from .models import Game, Comment


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'photo_main', 'slug', ]


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        look_field = 'slug'
