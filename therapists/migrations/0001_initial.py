# Generated by Django 3.2 on 2022-09-06 07:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=240)),
                ('image', cloudinary.models.CloudinaryField(default='no_image', max_length=255, verbose_name='image')),
                ('hourly_rate', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
