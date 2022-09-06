from django.db import models
from cloudinary.models import CloudinaryField


class Therapist(models.Model):
    """Therapist model

    ---
    Attributes:
        first_name: First name of therapist
        last_name: Last name of therapist
        bio: Therapist's bio
        image: Image of therapist
        hourly_rate: Hourly rate of therapist
        avg_rating: Average rating of therapist
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.CharField(max_length=240)
    image = CloudinaryField('image', default='no_image')
    hourly_rate = models.PositiveSmallIntegerField()

    def __str__(self):
        """Returns full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def avg_rating(self):
        """Returns average rating of therapist"""
        return self.reviews.aggregate(avg=models.Avg('rating'))['avg']
