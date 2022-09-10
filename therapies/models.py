from django.db import models
from cloudinary.models import CloudinaryField
import django.contrib.postgres.fields as pg_fields

from therapists.models import Therapist

BODY_AREAS = (
    (1, "Head"),
    (2, "Neck"),
    (3, "Shoulders"),
    (4, "Torso"),
    (5, "Upper Legs"),
    (6, "Lower Legs"),
    (7, "Buttocks"),
    (8, "Feet"),
    (9, "Full Body"),
    (10, "Upper Body"),
    (11, "Lower Body"),
    (12, "Back"),
)


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
    body_area = pg_fields.ArrayField(models.IntegerField(
        choices=BODY_AREAS
    ))
    benefits = pg_fields.ArrayField(models.CharField(max_length=50))
    description = models.CharField(max_length=180)
    duration = models.PositiveSmallIntegerField()
    image = CloudinaryField('image', default='no_image')
    image_alt_text = models.CharField(max_length=80, default="the therapy")
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
        return self.reviews.aggregate(avg=models.Avg('rating'))['avg']
