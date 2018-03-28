# Generated by Django 2.0.1 on 2018-03-22 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0002_auto_20180322_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realmatch',
            name='team_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_team_one', to='world_cup.UserTeam'),
        ),
        migrations.AlterField(
            model_name='realmatch',
            name='team_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_team_two', to='world_cup.UserTeam'),
        ),
    ]