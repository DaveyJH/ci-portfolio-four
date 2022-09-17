from django.contrib import admin
from .models import Therapy, BodyArea
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Therapy)
class TherapiesAdmin(SummernoteModelAdmin):
    """Add Therapy model to admin pages"""
    pass


@admin.register(BodyArea)
class BodyAreaAdmin(SummernoteModelAdmin):
    """Add BodyArea model to admin pages"""
    pass
