from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """Add Review model to admin pages"""

    summernote_fields = (
        'content',  # allow notes to be made to user if admin does not approve
    )
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        """Allows admin to approve reviews"""
        queryset.update(approved=True)
