# Generated by Django 3.2 on 2021-04-24 17:43

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='signup.account')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/users/%Y/%m/%d')),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('date_of_birth', models.DateField(blank=True, max_length=150, null=True)),
                ('inst', models.CharField(blank=True, max_length=150, null=True)),
                ('vk', models.CharField(blank=True, max_length=150, null=True)),
                ('fb', models.CharField(blank=True, max_length=150, null=True)),
                ('act', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('img/activity/yoga.png', 20), ('img/activity/walking.png', 19), ('img/activity/basketball.png', 1), ('img/activity/bowling.png', 3), ('img/activity/football.png', 5), ('img/activity/trekking.png', 17), ('img/activity/motocross.png', 8), ('img/activity/tennis.png', 16), ('img/activity/horse-riding.png', 6), ('img/activity/skiing.png', 14), ('img/activity/dancing.png', 4), ('img/activity/snowboard.png', 15), ('img/activity/pullups.png', 10), ('img/activity/lifting.png', 7), ('img/activity/bicycle.png', 2), ('img/activity/rolls.png', 11), ('img/activity/skate.png', 13), ('img/activity/ping-pong.png', 9), ('img/activity/volleyball.png', 18), ('img/activity/run.png', 12)], max_length=1500, null=True)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
