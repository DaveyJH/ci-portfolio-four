# Generated by Django 3.2 on 2022-09-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0002_therapist_image_alt_text'),
        ('therapies', '0002_auto_20220909_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapy',
            name='specialism',
            field=models.ManyToManyField(blank=True, related_name='specialism', to='therapists.Therapist'),
        ),
    ]
