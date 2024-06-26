# Generated by Django 4.2.5 on 2024-02-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0013_class_exceldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='exceldata',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='exceldata',
            name='password',
            field=models.CharField(default='django.utils.crypto.get_random_string', max_length=128),
            preserve_default=False,
        ),
    ]
