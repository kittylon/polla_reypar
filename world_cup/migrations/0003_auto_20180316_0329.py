# Generated by Django 2.0.1 on 2018-03-16 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0002_auto_20180315_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='match',
            new_name='date',
        ),
    ]
