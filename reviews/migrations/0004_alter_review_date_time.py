# Generated by Django 3.2 on 2022-09-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_time',
            field=models.DateField(auto_now=True),
        ),
    ]