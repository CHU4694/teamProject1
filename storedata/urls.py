from django.urls import path
from . import views

<<<<<<< HEAD
app_name = 'storedata'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
=======
urlpatterns = [
    path('',views.index, name='index'),
    path('api/regions/', views.region_list), 
]

>>>>>>> 07f0949 (내 작업 백업 커밋)
