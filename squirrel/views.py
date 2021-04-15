from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import SightRequestForm
from .models import Sighting
from django.db.models import Avg, Max, Min, Count

def index(request):
    return render(request,'squirrel/index.html',{})
    #return HttpResponse('Hello')


def sightList(request):
    sights = Sighting.objects.all()
    context = {
        'sights': sights,
    }
    return render(request, 'squirrel/sightings.html', context)

def update(request,unique_squirrel_id):
    sights = Sighting.objects.all()
    context = {
        'sights': sights,
    }
    return render(request, 'squirrel/add.html', context)

def map(request):
    sights = Sighting.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'squirrel/map.html', context)

def stats(request):
    sights = Sighting.objects.all()

    TotalNumber = len(sights)
    AvgLongitude = sights.aggregate(avg_latitude=Avg('Longitude'))
    AvgLatitude = sights.aggregate(avg_latitude=Avg('Latitude'))
    NumAboveGround = sights.filter(Location ='Above Ground').count()
    NumAdult = sights.filter(Age='ADULT').count()

    context = {
        "TotalNumber": TotalNumber,
        "AvgLongitude": AvgLongitude,
        "AvgLatitude": AvgLatitude,
        "NumAboveGround": NumAboveGround,
        "NumAdult": NumAdult,
    }
    return render(request, 'squirrel/stats.html', context)

def add(request):
    if request.method == 'POST':
        form = SightRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightRequestForm()

    context = {
            'form':form,
            }

    return render(request, 'squirrel/add.html', context)
