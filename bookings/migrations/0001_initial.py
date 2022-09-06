# Generated by Django 3.2 on 2022-09-06 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('therapies', '0001_initial'),
        ('therapists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='therapists.therapist')),
                ('therapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='therapies.therapy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
