from django.core.management import BaseCommand

from squirrel.models import Sighting

import csv

import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")


    def handle(self, *args, **options):
        a = Sighting.objects.all()
        file = open(options["path"],'w')
        file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age,Primary Fur Color\n")
        for data in a:
            writeString = "{},{},{},{},{},{},{}\n".format(data.Latitude,data.Longitude,data.Unique_Squirrel_Id,data.Shift,data.Date,data.Age,data.Primary_Fur_Color)
            file.write(writeString)
        file.close()
