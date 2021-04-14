from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Sighting
import csv
import datetime as dt

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
                dest='file_path',
                help='import_squirrel_data',
                )
    def handle(self, *args, **options):
        path = options['file_path']

        f = open(path, 'rb')
        data = csv.reader(f)
        next(data)

        #change to consistent true or false 
        def bool(string):
            if string in ['true', 'True','T','True']:
                string = "True"
            elif string in ['FALSE', 'false', 'False','F']:
                string = "False"
            else:
                string = ""
            return string

        for item in data:
            s = Sighting(
                    Longitude = item['X'],
                    Latitude = item['Y'],
                    Unique_Squirrel_Id = item['Unique Squirrel ID'],
                    Shift = item['Shift'],
                    Date = dt.strptime(item['Date'],'%m%d%Y'),
                    Age = item['Age'],
                    Primary_Fur_Color = item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_Location = item['Specific Location'],
                    Running = bool(item['Running']),
                    Chasing = bool(item['Chasing']),
                    Climbing = bool(item['Climbing']),
                    Eating = bool(item['Eating']),
                    Foraging = bool(item['Foraging']),
                    Other_Activities = item['Other Activities'],
                    Kuks = convertBool(item['Kuks']),
                    Quaas = convertBool(item['Quaas']),
                    Moans = convertBool(item['Moans']),
                    Tail_Flags = convertBool(item['Tail flags']),
                    Tail_Twitches = convertBool(item['Tail twitches']),
                    Approaches = convertBool(item['Approaches']),
                    Indifferent = convertBool(item['Indifferent']),
                    Runs_From = convertBool(item['Runs from']),
                    )
            s.save()
