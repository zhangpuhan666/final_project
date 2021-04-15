from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('map/',views.map),
    path('sightings/',views.sightList),
    path('sightings/stats/',views.stats),
    path('sightings/add/',views.add),
    re_path(r'sightings/(?P<Id>[a-zA-Z0-9-]+)',views.update),
    ]
