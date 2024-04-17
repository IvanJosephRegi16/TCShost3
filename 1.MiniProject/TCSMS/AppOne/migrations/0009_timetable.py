# Generated by Django 4.2.5 on 2024-02-08 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0008_rename_description_leaverequest_reason_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppOne.myclass')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppOne.subject')),
            ],
        ),
    ]