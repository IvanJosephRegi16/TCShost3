# Generated by Django 4.2.5 on 2024-02-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0015_timetable_class_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AlterField(
            model_name='myclass',
            name='class_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]