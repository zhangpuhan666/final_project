from django.forms import ModelForm

from .models import Sighting

class SightRequestForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
                'Latitude',
                'Longitude',
                'Unique_Squirrel_Id',
                'Shift',
                'Date',
                'Age',
                ]
