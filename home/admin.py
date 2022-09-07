from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Home)
class HomeAdmin(SummernoteModelAdmin):
    """Add Home model to admin pages"""

    summernote_fields = ('content', 'address')
