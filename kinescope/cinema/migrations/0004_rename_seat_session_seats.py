# Generated by Django 4.2.17 on 2025-01-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_movie_genre_alter_seatforsession_seat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='seat',
            new_name='seats',
        ),
    ]
