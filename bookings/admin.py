from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class ReviewAdmin(SummernoteModelAdmin):
    """Add Bookking model to admin pages"""
    pass
