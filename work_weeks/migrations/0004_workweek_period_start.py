# Generated by Django 4.1.2 on 2022-10-30 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_weeks', '0003_remove_workweek_period_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='workweek',
            name='period_start',
            field=models.DateField(default=datetime.datetime(2022, 10, 30, 0, 11, 7, 345838, tzinfo=datetime.timezone.utc)),
        ),
    ]
