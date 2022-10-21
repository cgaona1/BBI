from django.db import models

# Create your models here.
class Bottle(models.Model):
    name = models.CharField(max_length=50)
    start_count = models.IntegerField()
    end_count = models.IntegerField()