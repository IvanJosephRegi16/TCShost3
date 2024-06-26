# Generated by Django 4.2.5 on 2024-02-19 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0010_studentnew_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
    ]
