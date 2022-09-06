from django.db import models
from therapists.models import Therapist
from therapies.models import Therapy
from django.contrib.auth.models import User


class Booking(models.Model):
    """Booking model

    Attributes:
        user: The user that made the booking
        date: The date of the booking
        time: The time of the booking
        therapist: The therapist the booking is with
        therapy: The therapy the booking is for
        duration: The length of time of the therapy
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    date = models.DateField()
    time = models.TimeField()
    therapist = models.ForeignKey(
        Therapist, on_delete=models.CASCADE, related_name="bookings"
    )
    therapy = models.ForeignKey(
        Therapy, on_delete=models.CASCADE, related_name="bookings"
    )
    duration = models.IntegerField()
