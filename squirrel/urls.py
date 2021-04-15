from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('sightings/',views.sightList),
    path('sightings/stats/',views.stats),
    re_path(r'sightings/(?P<Unique_Squirrel_Id>[a-zA-Z0-9-]+)',views.update),
    path('map/',views.map),
    path('sightings/add/',views.add),
    ]
