# Generated by Django 4.2.5 on 2023-12-04 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0007_leaverequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaverequest',
            old_name='description',
            new_name='reason',
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
