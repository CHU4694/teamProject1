from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stores')
    owned_games = models.IntegerField(default=0)
    not_owned_game = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.location.name})"
