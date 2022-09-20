from django.views.generic import TemplateView
from .models import Home


class HomeView(TemplateView):
    """Renders the home page"""
    template_name = "home/index.html"

    def get_context_data(self):
        """Returns first Home object

        Try:except allows for erroneous extra Home models

        ---
        Raises:
            500 error if no Home object is found
        """
        home = {'content': '', 'address': ''}
        if len(Home.objects.all()):
            home = Home.objects.all()[0]
        context = {
            'home': home,
        }
        return context
