# Generated by Django 5.0.1 on 2024-02-05 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vandi_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentials',
            name='password',
        ),
        migrations.RemoveField(
            model_name='credentials',
            name='username',
        ),
    ]
