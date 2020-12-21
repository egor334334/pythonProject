from rest_framework import serializers

from .models import Musician


class MySerial(serializers.ModelSerializer):
    class Meta:
        model = Musician
        cell = ['author', 'song', 'position']