# Generated by Django 4.2.5 on 2024-02-28 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0027_timetable_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.TimeField(default=datetime.time(6, 8)),
        ),
    ]