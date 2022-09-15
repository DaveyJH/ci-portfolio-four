from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    # UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from .models import Review
from .forms import CreateReviewForm
from therapies.models import Therapy


class CreateReviewView(
    SuccessMessageMixin,
    CreateView
):
    """Renders a single therapy"""
    model = Review
    form_class = CreateReviewForm

    def form_valid(self, form):
        """Add user to review and validate form, provide bool for template"""
        user = self.request.user
        form.instance.user = user
        therapy = get_object_or_404(Therapy, id=self.kwargs['pk'])
        form.instance.therapy = therapy
        self.success_url = f'/therapies/therapy_details/{str(therapy.pk)}/'
        self.success_message = (
            f'Thanks, {user}. Your review is awaiting approval...'
        )
        return super(CreateReviewView, self).form_valid(form)
