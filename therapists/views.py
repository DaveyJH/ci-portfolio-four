from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
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


class AddTherapistView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Add Therapist view """
    model = Therapist
    form_class = CreateTherapistForm
    template_name = 'therapists/add_therapist.html'
    success_url = '/therapists/'

    def test_func(self):
        """ Test user is superuser else throw 403 """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully added new therapist!'
        )

        return super(AddTherapistView, self).form_valid(form)


class EditTherapistView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Therapist view """
    model = Therapist
    form_class = CreateTherapistForm
    template_name = 'therapists/edit_therapist.html'
    success_url = "/therapists/"

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully edited therapist!'
        )
        return super(EditTherapistView, self).form_valid(form)

    def test_func(self):
        """ Check user is staff else throw 403 """
        return self.request.user.is_superuser


class DeleteTherapistView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete therapist view """
    model = Therapist
    success_url = "/therapists/"

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully deleted therapist'
        )
        return super(DeleteTherapistView, self).form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        return self.request.user.is_superuser
