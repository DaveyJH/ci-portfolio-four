from django.views.generic import TemplateView
from .models import Home


class HomeView(TemplateView):
    """Renders the home page"""
    template_name = "index.html"

    def get_context_data(self):
        """Returns first Home object"""
        context = {
            'home': Home.objects.all().first()
        }
        return context
