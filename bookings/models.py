from django.db import models
from therapists.models import Therapist
from therapies.models import Therapy
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Booking(models.Model):
    """Booking model

    ---
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


class BookingInfo(models.Model):
    """Booking info model

    ---
    Attributes:
        message : introductory text to the site
        contact_info : phone number
        open_times: dictionary of open/close times for each day

    ---
    ### Note:
        open_times format MUST be as follows with letter casing as shown:
            {
                "Monday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Tuesday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Wednesday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Thursday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Friday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Saturday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
                "Sunday": {
                    "open": "<open_time>",
                    "close": "<close_time>",
                },
            }
    """

    message = models.TextField()
    contact_info = PhoneNumberField()
    open_times = models.JSONField()

    def __str__(self):
        """Returns `message`"""
        return str(self.contact_info)
