from django.contrib import admin
from .models import Therapist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Therapist)
class TherapistsAdmin(SummernoteModelAdmin):
    """Add Therapist model to admin pages"""

    summernote_fields = (
        'bio',
    )
