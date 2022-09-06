from django.db import models
from therapists.models import Therapist
from therapies.models import Therapy


class Review(models.Model):
    """Review model

    ---
    Attributes:
        title: Short title of review
        date_time: Date/Time of creation
        user: user that wrote the review
        rating: numerical rating 1 to 5
        content: review text content
        therapist: therapist attached to review
        therapy: therapy attached to review
    """

    title = models.CharField(max_length=30, unique=True)
    date_time = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=30)  # ? foreign key
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i}") for i in range(1, 6)]
    )
    content = models.CharField(max_length=220)
    therapist = models.ForeignKey(
        Therapist, on_delete=models.CASCADE, related_name="reviews"
    )
    therapy = models.ForeignKey(
        Therapy, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        """Returns `title`"""
        return self.title
