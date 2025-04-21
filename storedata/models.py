from django.db import models

class StoreGameData(models.Model):
    region = models.CharField(max_length=50)
    store = models.CharField(max_length=100)
    owned_count = models.IntegerField()
    missing_count = models.IntegerField()
    owned_list = models.TextField()
    missing_list = models.TextField()

    def __str__(self):
        return f"[{self.region}] {self.store}"
