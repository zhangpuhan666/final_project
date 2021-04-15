from django.http import HttpResponse
from django.shortcuts import render

from .models import Sighting


def index(request):
    return render(request,'squirrel/index.html',{})
    #return HttpResponse('Hello')


def sightList(request):
    sights = Sighting.objects.all()
    fields = ['Unique_Squirrel_Id','Date']
    context = {
        'sights': sights,
        'fields': fields
    }
    return render(request, 'squirrel/sightings.html', context)

'''
def unique(request,unique_squirrel_id):

    context = {
        'sights': sights,
        'fields': fields
    }
    return render(request, 'sightings/unique.html', context)
'''
