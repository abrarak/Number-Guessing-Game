# Generated by Django 4.2.5 on 2023-10-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guessing_game_App', '0002_rename_random_randomnumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='randomnumber',
            new_name='randomnumber_table',
        ),
    ]
