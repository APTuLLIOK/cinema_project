# Generated by Django 4.2.17 on 2025-01-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_movie_is_in_the_cinema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(default='01:00', verbose_name='Продолжительность'),
        ),
    ]