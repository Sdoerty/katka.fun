# Generated by Django 3.1.4 on 2021-04-04 15:47

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/users/%Y/%m/%d')),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('date_of_birth', models.DateField(blank=True, max_length=150, null=True)),
                ('inst', models.CharField(blank=True, max_length=150, null=True)),
                ('vk', models.CharField(blank=True, max_length=150, null=True)),
                ('fb', models.CharField(blank=True, max_length=150, null=True)),
                ('act', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('img/activity/tennis.png', 16), ('img/activity/motocross.png', 8), ('img/activity/dancing.png', 4), ('img/activity/yoga.png', 20), ('img/activity/lifting.png', 7), ('img/activity/ping-pong.png', 9), ('img/activity/football.png', 5), ('img/activity/horse-riding.png', 6), ('img/activity/run.png', 12), ('img/activity/rolls.png', 11), ('img/activity/basketball.png', 1), ('img/activity/volleyball.png', 18), ('img/activity/pullups.png', 10), ('img/activity/snowboard.png', 15), ('img/activity/trekking.png', 17), ('img/activity/bowling.png', 3), ('img/activity/skate.png', 13), ('img/activity/walking.png', 19), ('img/activity/bicycle.png', 2), ('img/activity/skiing.png', 14)], max_length=505, null=True)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
