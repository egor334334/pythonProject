from django.core.management.base import BaseCommand

from chart.models import Musician
from chart.chart_parser import Parser


class Command(BaseCommand):
    def handle(self, *args, **options):
        parser = Parser()
        result = parser.parse_chart()
        for position, record in enumerate(result, 1):
            obj, created = Musician.objects.get_or_create(position=position)
            obj.author = record.get('author')
            obj.song = record.get('song')
            obj.save()