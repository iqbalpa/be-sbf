from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField()
    trailer = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    year_released = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
