# Generated by Django 3.0.10 on 2020-10-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_simplefarm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplefarm',
            name='farm_owner',
        ),
    ]
