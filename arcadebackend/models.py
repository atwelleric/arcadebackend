from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120)
    img_source = models.URLField()
    about = models.TextField()
    creator_info = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.body