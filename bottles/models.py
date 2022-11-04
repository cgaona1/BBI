from django.db import models
from BBI.models import BaseModel

class Bottle(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
