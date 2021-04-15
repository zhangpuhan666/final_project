from django.forms import ModelForm

from .models import Sighting

class SightRequestForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
