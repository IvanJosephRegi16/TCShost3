# Generated by Django 4.2.5 on 2024-04-09 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0063_remove_feedbackstudent_radio_options_selectedoption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='questions',
        ),
    ]
