# Generated by Django 4.1.2 on 2022-10-30 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_weeks', '0004_workweek_period_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workweek',
            name='period_start',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
