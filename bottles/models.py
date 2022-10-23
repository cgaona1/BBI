from django.db import models

class Bottle(models.Model):
    name = models.CharField(max_length=50)
    start_count = models.IntegerField()
    end_count = models.IntegerField()

    def __str__(self):
        return self.name