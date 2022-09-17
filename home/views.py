from django.views.generic import TemplateView
from django.http import Http404
from .models import Home


class HomeView(TemplateView):
    """Renders the home page"""
    template_name = "home/index.html"

    def get_context_data(self):
        """Returns first Home object

        Try:except allows for erroneous extra Home models

        ---
        Raises:
            Http404 if no Home object is found
        """

        try:
            home = Home.objects.all()[0]
        except IndexError:
            raise Http404()
        context = {
            'home': home,
        }
        return context
