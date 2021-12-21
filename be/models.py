from django.db import models

class Film(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=50)
    poster = models.ImageField()
    trailer = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
=======
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
>>>>>>> f502015b66f4345e3dc2e321b4affac6c2483dc1
    year_released = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
