# Generated by Django 4.2.5 on 2024-03-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0048_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='mark',
            new_name='scored_marks',
        ),
        migrations.AddField(
            model_name='marks',
            name='grade',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='marks',
            name='percentage',
            field=models.FloatField(blank=True, default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marks',
            name='total_marks',
            field=models.IntegerField(default=50),
        ),
    ]
