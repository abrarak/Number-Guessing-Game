# Generated by Django 4.2.5 on 2023-11-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guessing_game_App', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='usernumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userrangeandchance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowerrange', models.IntegerField()),
                ('upperrange', models.IntegerField()),
                ('chance', models.IntegerField()),
                ('systemnumber', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='info',
        ),
    ]
