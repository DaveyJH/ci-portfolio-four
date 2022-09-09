from django.conf import settings


def cloud(request):
    """Provides Cloudinary URL for images"""
    return {'CLOUD': settings.CLOUD}
