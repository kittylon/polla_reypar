# Generated by Django 2.0.1 on 2018-03-11 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20180311_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile',
            field=models.CharField(choices=[('5_Participantes', 'A'), ('2_Participantes', 'B'), ('1_Participante', 'C')], max_length=50),
        ),
    ]
