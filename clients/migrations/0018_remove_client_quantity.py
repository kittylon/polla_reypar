# Generated by Django 2.0.1 on 2018-04-17 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_auto_20180417_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='quantity',
        ),
    ]