# Generated by Django 4.2.5 on 2024-03-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOne', '0050_marks_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=9),
        ),
    ]