from django.db import models
from datetime import datetime

class Creator(models.Model):
    name = models.CharField(max_length=50)
    descritpion = models.TextField(blank=True)
    github = models.URLField()
    email = models.CharField(max_length=100)
    top_creator = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name