# Generated by Django 2.1.3 on 2018-12-18 22:42

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]
