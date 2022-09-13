from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Therapy
from .forms import CreateTherapyForm
from therapists.models import Therapist


class TherapiesView(TemplateView):
    """Renders the therapies (all) page"""
    template_name = "therapies/therapies.html"

    def get_context_data(self):
        """Returns Therapist and Therapies objects"""
        context = {
            'therapists': Therapist.objects.all().order_by('last_name'),
            'therapies': Therapy.objects.all().order_by('therapy_name')
        }
        return context


class AddTherapyView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    CreateView
):
    """ Add Therapist view """
    model = Therapy
    form_class = CreateTherapyForm
    template_name = 'therapies/add_therapy.html'
    success_url = '/therapies/'
    success_message = '%(therapy_name)s added successfully!'

    def test_func(self):
        """ Test user is superuser else throw 403 """
        return self.request.user.is_superuser


class EditTherapyView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    """ Edit Therapy view """
    model = Therapy
    form_class = CreateTherapyForm
    template_name = 'therapies/edit_therapy.html'
    success_url = "/therapies/"
    success_message = '%(therapy_name)s edited successfully!'

    def test_func(self):
        """ Check user is staff else throw 403 """
        return self.request.user.is_superuser


class DeleteTherapyView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    """ Delete therapist view """
    model = Therapy
    success_url = "/therapies/"
    success_message = '%(therapy_name)s deleted successfully!'

    def delete(self, request, *args, **kwargs):
        """ Display success message """
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteTherapyView, self).delete(request)

    def test_func(self):
        """ Test user is staff else throw 403 """
        return self.request.user.is_superuser
