# Generated by Django 4.2.5 on 2023-11-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guessing_game_App', '0004_delete_boundary_delete_chance_delete_guessed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('usernumber', models.IntegerField()),
                ('systemnumber', models.IntegerField()),
                ('chance', models.IntegerField()),
            ],
        ),
    ]
