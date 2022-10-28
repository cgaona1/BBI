from django.db import models
from BBI.models import BaseModel

class Bottle(BaseModel):
    name = models.CharField(max_length=50)
    start_count = models.IntegerField()
    end_count = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name