# Generated by Django 3.1.4 on 2020-12-29 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]