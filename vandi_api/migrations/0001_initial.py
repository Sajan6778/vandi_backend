# Generated by Django 5.0.1 on 2024-02-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'others')], max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('categories', models.CharField(choices=[('customer', 'customer'), ('worker', 'worker'), ('transport', 'transport')], max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
