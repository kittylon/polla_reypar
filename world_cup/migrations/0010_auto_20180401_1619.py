# Generated by Django 2.0.1 on 2018-04-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0009_usermatch_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='realmatch',
            name='penals_team_one',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='realmatch',
            name='penals_team_two',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usermatch',
            name='penals_team_one',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usermatch',
            name='penals_team_two',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
