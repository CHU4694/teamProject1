from django.urls import path
from . import views

app_name = 'storedata'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]