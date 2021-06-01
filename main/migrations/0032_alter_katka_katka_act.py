# Generated by Django 3.2 on 2021-06-01 20:29

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_katka_katka_act'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katka',
            name='katka_act',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('img/activity/horse-riding.png', 6), ('img/activity/snowboard.png', 15), ('img/activity/dancing.png', 4), ('img/activity/volleyball.png', 18), ('img/activity/skate.png', 13), ('img/activity/pullups.png', 10), ('img/activity/basketball.png', 1), ('img/activity/motocross.png', 8), ('img/activity/run.png', 12), ('img/activity/trekking.png', 17), ('img/activity/yoga.png', 20), ('img/activity/bowling.png', 3), ('img/activity/walking.png', 19), ('img/activity/football.png', 5), ('img/activity/rolls.png', 11), ('img/activity/bicycle.png', 2), ('img/activity/skiing.png', 14), ('img/activity/ping-pong.png', 9), ('img/activity/tennis.png', 16), ('img/activity/lifting.png', 7)], max_length=505),
        ),
    ]
