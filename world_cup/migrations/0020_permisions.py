# Generated by Django 2.0.1 on 2018-04-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cup', '0019_auto_20180410_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='permisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('phase', models.CharField(choices=[('Groups', 'Grupos'), ('Eights', 'Octavos'), ('Fourths', 'Cuartos'), ('Semi', 'Semifinal'), ('3y4', 'Puesto 3 y 4'), ('Finals', 'Final')], max_length=50)),
            ],
        ),
    ]