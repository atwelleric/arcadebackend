from django.db import models
from django.utils.timezone import now
from creator.models import Creator

# Create your models here.


class Game(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=120)
    about = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.body
