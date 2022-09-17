from django.db import models
from cloudinary.models import CloudinaryField
import django.contrib.postgres.fields as pg_fields

from therapists.models import Therapist


class BodyArea(models.Model):
    """BodyArea model"""
    area = models.CharField(max_length=15, unique=True)
    order_position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order_position']

    def __str__(self):
        """Returns body area"""
        return self.area


class Therapy(models.Model):
    """Therapy model

    ---
    Attributes:
        therapy_name: Name of therapy
        body_area: Areas of the body covered by therapy
        benefits: List of benefits obtained from therapy
        description: Description of therapy
        duration: Length of time of therapy
        image: Relevant image for therapy
        therapists: Therapists that can perform therapy
        duration_is_variable: True if duration is variable, else False
        avg_rating: Average rating of therapy
    """

    therapy_name = models.CharField(max_length=40, unique=True)
    body_area = models.ManyToManyField(
        BodyArea, related_name="body_area"
    )
    benefits = pg_fields.ArrayField(models.CharField(max_length=50))
    description = models.CharField(max_length=180)
    duration = models.PositiveSmallIntegerField()
    image = CloudinaryField('image', default='no_image')
    image_alt_text = models.CharField(
        max_length=80, default="the therapy", blank=True
    )
    therapists = models.ManyToManyField(Therapist, related_name="therapies")
    duration_is_variable = models.BooleanField(default=False)
    specialism = models.ManyToManyField(
        Therapist, related_name="specialism", blank=True
    )

    class Meta:
        ordering = ['-duration']  # start at longer (more profitable) therapies

    def __str__(self):
        """Returns `therapy_name`"""
        return self.therapy_name

    @property
    def avg_rating(self):
        """Returns average rating of therapy"""
        avg = self.reviews.filter(approved=True).aggregate(
            avg=models.Avg('rating'))['avg']  # type: float | None
        if avg:
            if avg.is_integer():
                avg = int(avg)
            else:
                avg = round(avg, 1)
        return avg
