from django.core.management import BaseCommand
from squirrel.models import Sight

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			dest='file_path',
			type=str,  
			help='export_squirrel_data',
		)

	def handle(self, *args, **options):
		file_path = options["file_path"]
		all = Squirrel.objects.all()
		# print(len(all))
		file = open(file_path,'w')
		file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age\n")
		for data in all:
			write_str = "{},{},{},{},{},{}\n".format(data.latitude,data.longitude,data.unique_squirrel_id,data.shift,data.date,data.age)
			file.write(write_str)
		file.close()
		# print("export_squirrel_data")


if __name__ == "__main__":
	file_path = "."
	all = Squirrel.objects.all()
	print(len(all))
	file = open(file_path,'w')
	file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age\n")
	for data in all:
		write_str = "{},{},{},{},{},{}\n".format(data.latitude,data.longitude,data.unique_squirrel_id,data.shift,data.date,data.age)
		file.write(write_str)
	file.close()
