from django.urls import path
from . import views

app_name = 'boardgame_locations'

urlpatterns = [
    path('', views.location_list, name='location_list'),
    path('<str:location_name>', views.location_detail, name='location_detail'),
]