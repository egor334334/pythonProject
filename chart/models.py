from django.db import models

class Musician(models.Model):
    author = models.CharField(max_length=50)
    song = models.CharField(max_length=50)
    position = models.PositiveBigIntegerField(unique=True)

