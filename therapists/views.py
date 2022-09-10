from django.views.generic import TemplateView
from .models import Therapist
from therapies.models import Therapy


class TherapistsView(TemplateView):
    """Renders the therapists (all) page"""
    template_name = "therapists.html"

    def get_context_data(self):
        """Returns first Therapist object"""

        context = {
            'therapists': Therapist.objects.all(),
            'therapies': Therapy.objects.all()
        }
        return context
