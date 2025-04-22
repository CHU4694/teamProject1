from django.urls import path
from . import views

<<<<<<< HEAD
=======

>>>>>>> 8de243b016fbf2c548428995a7a66d8fa9699a5e
app_name = 'storedata'



urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='dashboard'),
]

# urlpatterns = [
#     path('',views.index, name='index'),
#     path('api/regions/', views.region_list), 
# ]

=======
    #path('',views.index, name='index'),
    path('api/regions/', views.region_list), 
    path('', views.dashboard, name='dashboard')
]

>>>>>>> 8de243b016fbf2c548428995a7a66d8fa9699a5e
