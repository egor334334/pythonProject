from django.db import models

class Musician(models.Model):
    author = models.CharField(max_length=50, default='', blank=True, null=True)
    song = models.CharField(max_length=50, default='', blank=True, null=True)
    position = models.PositiveBigIntegerField(unique=True)
    def __str__(self):
        return str(self.author)

