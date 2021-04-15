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
        file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age,Primary Fur Color,Location,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from\n")
        for data in a:
            writeString = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                    data.Latitude,data.Longitude,data.Unique_Squirrel_Id,data.Shift,data.Date,data.Age,data.Primary_Fur_Color,data.Location,data.Specific_Location,
                    data.Running,data.Chasing, data.Climbing, data.Eating, data.Foraging, data.Other_Activities, data.Kuks, data.Quaas, data.Moans, data.Tail_Flags,
                    data.Tail_Twitches, data.Approaches, data.Indifferent, data.Runs_From)
            file.write(writeString)
        file.close()
