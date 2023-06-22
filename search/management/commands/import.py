import csv
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        file_path = './restaurants_small.csv' 

        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                dish = Dish(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
                dish.save()

