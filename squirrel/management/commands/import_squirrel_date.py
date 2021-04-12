from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Sight
import csv
import datetime

def boolean(elem):
    return True if elem == 'TRUE' else False

class Command(BaseCommand):

    help = 'Import squirrel data from local csv files'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='/path/to/file.csv')

    def boolean(self, elem):
        return True if elem == 'TRUE' else False


    def handle(self, *args, **options):
        path = options['path']

        f = open(path, 'r')
        data = csv.reader(f)
        next(data)

        for row in data:
            _longitude = float(row[0])

            _latitude = float(row[1])

            _unique_squirrel_id = row[2]

            _shift = Squirrel.AM if row[4] == 'AM' else Squirrel.PM

            _date = datetime.date(int(row[5][-4:]),int(row[5][:2]),int(row[5][2:4]))

            if row[7] == 'Adult':
                _age = Squirrel.ADULT
            elif row[7] == 'JUVENILE':
                _age = Squirrel.JUVENILE
            else:
                _age = Squirrel.OTHER

            _primary_fur_color = row[8]

            if row[12] == 'Ground Plane':
                _location = Squirrel.GROUND_PLANE
            elif row[12] == 'Above Ground':
                _location = Squirrel.ABOVE_GROUND
            else:
                _location = Squirrel.OTHER

            _specific_location = row[14]
            _other_activities = row[20]

            _, created = Squirrel.objects.get_or_create(
                longitude=_longitude,
                latitude=_latitude,
                unique_squirrel_id=_unique_squirrel_id,
                shift=_shift,
                date=_date,
                age=_age,
                primary_fur_color=_primary_fur_color,
                location=_location,
                specific_location=_specific_location,
                running=self.boolean(row[15]),
                chasing=self.boolean(row[16]),
                climbing=self.boolean(row[17]),
                eating=self.boolean(row[18]),
                foraging=self.boolean(row[19]),
                other_activities=_other_activities,
                kuks=self.boolean(row[21]),
                quaas=self.boolean(row[22]),
                moans=self.boolean(row[23]),
                tail_flags=self.boolean(row[24]),
                tail_switches=self.boolean(row[25]),
                approaches=self.boolean(row[26]),
                indifferent=self.boolean(row[27]),
                runs_from=self.boolean(row[28]),
            )
