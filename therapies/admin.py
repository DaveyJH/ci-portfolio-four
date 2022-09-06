from django.contrib import admin
from .models import Therapy
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Therapy)
class TherapiesAdmin(SummernoteModelAdmin):
    """Add Therapy model to admin pages"""

    summernote_fields = (
        'description',
    )
