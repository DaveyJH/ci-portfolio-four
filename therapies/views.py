from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView, TemplateView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Therapy
from .forms import CreateTherapyForm
from therapists.models import Therapist
from reviews.forms import CreateReviewForm
from reviews.models import Review


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


class TherapyDetailView(
    SuccessMessageMixin,
    DetailView
):
    """Renders a single therapy"""
    model = Therapy
    template_name = "therapies/therapy_details.html"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('therapy_detail', pk=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        """Retrieves relevant therapy and creates forms"""
        form = CreateReviewForm()
        therapy = get_object_or_404(Therapy, id=self.kwargs['pk'])
        context = {
            'therapy': therapy,
            'reviews': Review.objects.filter(
                therapy=therapy.id).order_by('-date_time'),
            'form': form,
        }
        return context
