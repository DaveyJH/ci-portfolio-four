from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView, UpdateView,
    # DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Review
from .forms import CreateReviewForm
from therapies.models import Therapy


class CreateReviewView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    """Adds a review to a therapy"""
    model = Review
    form_class = CreateReviewForm

    def form_valid(self, form):
        """Adds user to review and validate form"""
        user = self.request.user
        form.instance.user = user
        therapy = get_object_or_404(Therapy, id=self.kwargs['pk'])
        form.instance.therapy = therapy
        self.success_url = f'/therapies/therapy_details/{str(therapy.pk)}/'
        self.success_message = (
            f'Thanks, {user}. Your review is awaiting approval...'
        )
        return super(CreateReviewView, self).form_valid(form)


class EditReviewView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    """Edits a review"""
    model = Review
    form_class = CreateReviewForm

    def get_success_url(self, *args, **kwargs):
        """Configures the URL and success message"""
        user = self.request.user
        therapy_pk = self.request.resolver_match.kwargs['therapy_pk']
        self.success_url = f'/therapies/therapy_details/{str(therapy_pk)}/'
        self.success_message = (
            f'Thanks, {user}. Your edited review is awaiting approval...'
        )
        return self.success_url

    def form_valid(self, form, *args, **kwargs):
        """Updates review and sets approved to false"""
        form.instance.approved = False
        return super(EditReviewView, self).form_valid(form)
