# Generated by Django 2.0.1 on 2018-03-15 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='goals_one',
        ),
        migrations.RemoveField(
            model_name='match',
            name='goals_two',
        ),
        migrations.AlterField(
            model_name='match',
            name='team_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_one', to='world_cup.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_two', to='world_cup.Team'),
        ),
    ]
