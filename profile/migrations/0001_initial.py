# Generated by Django 3.1.4 on 2020-12-29 18:32

from django.db import migrations, models
import django.db.models.deletion


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
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('date', models.DateField(max_length=150)),
                ('inst', models.CharField(blank=True, max_length=150, null=True)),
                ('vk', models.CharField(blank=True, max_length=150, null=True)),
                ('fb', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]