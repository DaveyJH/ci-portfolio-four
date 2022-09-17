# Generated by Django 3.2 on 2022-09-17 14:36

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_bookinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='contact_info',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
