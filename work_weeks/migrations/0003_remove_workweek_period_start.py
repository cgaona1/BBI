# Generated by Django 4.1.2 on 2022-10-30 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_weeks', '0002_alter_workweek_period_start_alter_workweek_work_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workweek',
            name='period_start',
        ),
    ]