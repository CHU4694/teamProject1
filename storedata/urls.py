from django.urls import path
from . import views


app_name = 'storedata'



urlpatterns = [
    #path('',views.index, name='index'),
    path('api/regions/', views.region_list), 
    path('', views.dashboard, name='dashboard')
]

