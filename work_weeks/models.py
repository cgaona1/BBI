from email.policy import default
from django.db import models
from BBI.models import BaseModel
from bottles.models import Bottle

from django.utils import timezone
from datetime import timedelta
import datetime

def one_week_hence():
    import pytz
    tz = pytz.timezone("US/Mountain")
    time = timezone.now()+timedelta(days=7)
    return time.astimezone(tz)

class WorkWeek(BaseModel):
    period_start = models.DateField(default=datetime.date.today)
    period_end = models.DateField(default=one_week_hence)

    def __str__(self):
        return f'{self.period_start}, {self.period_end}'

class WorkWeekDay(BaseModel):
    DAYS = (
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    )

    work_week = models.ForeignKey(WorkWeek, on_delete=models.CASCADE)
    day = models.CharField(
        max_length=30,
        choices=DAYS,
        null=True,
        blank=True
    )
    bottle = models.ForeignKey(
        Bottle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    start_count = models.IntegerField()
    end_count = models.IntegerField(
        null=True,
        blank=True
    )
    def __str__(self):
        return f'{self.work_week}, {self.day}'
