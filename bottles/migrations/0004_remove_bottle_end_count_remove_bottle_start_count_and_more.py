# Generated by Django 4.1.2 on 2022-11-03 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bottles', '0003_alter_bottle_end_count_alter_bottle_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='end_count',
        ),
        migrations.RemoveField(
            model_name='bottle',
            name='start_count',
        ),
        migrations.CreateModel(
            name='BottleInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_by', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_count', models.IntegerField()),
                ('end_count', models.IntegerField(blank=True, null=True)),
                ('bottle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bottles.bottle')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
