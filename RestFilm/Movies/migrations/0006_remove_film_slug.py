# Generated by Django 2.1.4 on 2018-12-12 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_auto_20181212_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='slug',
        ),
    ]