from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Therapist
from .forms import CreateTherapistForm
from therapies.models import Therapy


class TherapistsView(TemplateView):
    """Renders the therapists (all) page"""
    template_name = "therapists/therapists.html"

    def get_context_data(self):
        """Returns Therapist and Therapies objects"""
        context = {
            'therapists': Therapist.objects.all().order_by('last_name'),
            'therapies': Therapy.objects.all()
        }
        return context


class AddTherapistView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    CreateView
):
    """ Add Therapist view """
    model = Therapist
    form_class = CreateTherapistForm
    template_name = 'therapists/add_therapist.html'
    success_url = '/therapists/'
    success_message = '%(first_name)s %(last_name)s added successfully!'

    def test_func(self):
        """ Test user is superuser else throw 403 """
        return self.request.user.is_superuser


class EditTherapistView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    """ Edit Therapist view """
    model = Therapist
    form_class = CreateTherapistForm
    template_name = 'therapists/edit_therapist.html'
    success_url = "/therapists/"
    success_message = '%(first_name)s %(last_name)s edited successfully!'

    def test_func(self):
        """ Check user is staff else throw 403 """
        return self.request.user.is_superuser


class DeleteTherapistView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    """ Delete therapist view """
    model = Therapist
    success_url = "/therapists/"
    success_message = '%(first_name)s %(last_name)s deleted successfully!'

    def delete(self, request, *args, **kwargs):
        """ Display success message """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteTherapistView, self).delete(request)

    def test_func(self):
        """ Test user is staff else throw 403 """
        return self.request.user.is_superuser
