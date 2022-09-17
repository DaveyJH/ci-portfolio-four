from django.contrib import admin
from .models import Booking, BookingInfo
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """Add Booking model to admin pages"""
    pass


@admin.register(BookingInfo)
class BookingInfoAdmin(SummernoteModelAdmin):
    """Add Booking info model to admin pages"""
    pass
