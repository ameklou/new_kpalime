# Generated by Django 2.1.3 on 2018-12-19 06:12

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181219_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]