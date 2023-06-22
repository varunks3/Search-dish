import csv
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        file_path = './restaurants_small.csv'  # Update with the actual path to your CSV file

        # Open the CSV file and read the data
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Create a Dish object and populate its fields from the CSV row
                dish = Dish(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
                dish.save()

