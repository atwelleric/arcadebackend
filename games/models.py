from django.db import models
from django.utils.timezone import now
from creator.models import Creator

# Create your models here.


class Game(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=120)
    img_source = models.URLField()
    about = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.body
