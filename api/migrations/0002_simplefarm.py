# Generated by Django 3.0.10 on 2020-10-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleFarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(default="My uncles' basement", max_length=15)),
                ('capacity', models.PositiveIntegerField()),
                ('buy_price', models.PositiveIntegerField()),
                ('farm_owner', models.CharField(default='Big Floppa', max_length=25)),
            ],
        ),
    ]
