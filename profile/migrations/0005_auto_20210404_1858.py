# Generated by Django 3.1.4 on 2021-04-04 15:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20210404_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='act',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('img/activity/football.png', 5), ('img/activity/ping-pong.png', 9), ('img/activity/tennis.png', 16), ('img/activity/basketball.png', 1), ('img/activity/skate.png', 13), ('img/activity/dancing.png', 4), ('img/activity/snowboard.png', 15), ('img/activity/horse-riding.png', 6), ('img/activity/walking.png', 19), ('img/activity/rolls.png', 11), ('img/activity/yoga.png', 20), ('img/activity/motocross.png', 8), ('img/activity/run.png', 12), ('img/activity/bicycle.png', 2), ('img/activity/trekking.png', 17), ('img/activity/lifting.png', 7), ('img/activity/bowling.png', 3), ('img/activity/pullups.png', 10), ('img/activity/volleyball.png', 18), ('img/activity/skiing.png', 14)], max_length=505, null=True),
        ),
    ]
