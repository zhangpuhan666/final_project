from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Sighting
import csv
import datetime as dt

class Command(BaseCommand):
    def add_arguments(self, parser):
       # parser.add_argument(
        #        'file_path',
         #       help='import_squirrel_data',
          #      type = str
           #     )
        parser.add_argument('args',nargs='+',type=str)

    def handle(self, *args, **options):

        path = args[0]

        with open(path) as f:
            reader = csv.DictReader(f)
            data = list(reader)

        #change to consistent true or false 
        def bool(string):
            if str(string) in ['true', 'True','T','True']:
                string = True
            elif str(string) in ['FALSE', 'false', 'False','F']:
                string = False
            else:
                string = None
            return string

        for item in data:
            o = Sighting(
                    Longitude = item['X'],
                    Latitude = item['Y'],
                    Unique_Squirrel_Id = item['Unique Squirrel ID'],
                    Shift = item['Shift'],
                    Date = dt.datetime.strptime(item['Date'],'%m%d%Y'),
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
                    Kuks = bool(item['Kuks']),
                    Quaas = bool(item['Quaas']),
                    Moans = bool(item['Moans']),
                    Tail_Flags = bool(item['Tail flags']),
                    Tail_Twitches = bool(item['Tail twitches']),
                    Approaches = bool(item['Approaches']),
                    Indifferent = bool(item['Indifferent']),
                    Runs_From = bool(item['Runs from']),
                    )
            o.save()


