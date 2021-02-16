# Generated by Django 3.1.4 on 2021-02-16 17:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Katka',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=150)),
                ('date', models.DateField(max_length=150)),
                ('time', models.TimeField(max_length=150)),
                ('descr', models.CharField(max_length=350)),
                ('katka_act', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'basketball'), ('2', 'bicycle'), ('3', 'bowling'), ('4', 'dancing'), ('5', 'football'), ('6', 'horse-riding'), ('7', 'lifting'), ('8', 'motocross'), ('9', 'ping-pong'), ('10', 'pullups'), ('11', 'rolls'), ('12', 'run'), ('13', 'skate'), ('14', 'skiing'), ('15', 'snowboard'), ('16', 'tennis'), ('17', 'trekking'), ('18', 'volleyball'), ('19', 'walking'), ('20', 'yoga')], max_length=50)),
            ],
            options={
                'verbose_name': 'Катка',
                'verbose_name_plural': 'Все события Катка',
            },
        ),
    ]
