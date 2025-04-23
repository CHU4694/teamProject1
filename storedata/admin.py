from django.contrib import admin
from .models import StoreGameData
from .models import MonthlyGame

# Register your models here.
admin.site.register(StoreGameData)
admin.site.register(MonthlyGame)