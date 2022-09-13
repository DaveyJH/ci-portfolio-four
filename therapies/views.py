from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
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


class AddTherapyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Add Therapist view """
    model = Therapy
    form_class = CreateTherapyForm
    template_name = 'therapies/add_therapy.html'
    success_url = '/therapies/'

    def test_func(self):
        """ Test user is superuser else throw 403 """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully added new therapy!'
        )

        return super(AddTherapyView, self).form_valid(form)


class EditTherapyView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Therapy view """
    model = Therapy
    form_class = CreateTherapyForm
    template_name = 'therapies/edit_therapy.html'
    success_url = "/therapies/"

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully edited therapy!'
        )
        return super(EditTherapyView, self).form_valid(form)

    def test_func(self):
        """ Check user is staff else throw 403 """
        return self.request.user.is_superuser


class DeleteTherapyView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete therapist view """
    model = Therapy
    success_url = "/therapies/"

    def form_valid(self, form):
        """ Validate form """
        messages.success(
            self.request,
            'Successfully deleted therapist'
        )
        return super(DeleteTherapyView, self).form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        return self.request.user.is_superuser
