# Generated by Django 4.1.2 on 2022-10-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='updated_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]