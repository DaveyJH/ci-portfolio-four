from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """Add Review model to admin pages"""

    summernote_fields = (
        'content',
    )
