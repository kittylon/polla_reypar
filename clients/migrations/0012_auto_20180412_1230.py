# Generated by Django 2.0.1 on 2018-04-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20180411_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='document_number',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
