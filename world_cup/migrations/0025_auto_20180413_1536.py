# Generated by Django 2.0.1 on 2018-04-13 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0024_auto_20180413_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datepermissions',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='datepermissions',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
