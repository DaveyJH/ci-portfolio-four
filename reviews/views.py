from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
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
        therapy_pk = self.kwargs['therapy_pk']
        self.success_url = f'/therapies/therapy_details/{str(therapy_pk)}/'
        self.success_message = (
            f'Thanks, {user}. Your edited review is awaiting approval...'
        )
        if user.is_superuser:
            self.success_message = (
                'Review edited!'
            )
        return self.success_url

    def form_valid(self, form, *args, **kwargs):
        """Updates review and sets approved to false"""
        form.instance.approved = False
        if self.request.user.is_superuser:
            form.instance.approved = True
        return super(EditReviewView, self).form_valid(form)


class DeleteReviewView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView
):
    """Deletes a review"""
    model = Review

    def delete(self, *args, **kwargs):
        """Deletes the relevant review and redirects to the therapy details"""
        user = self.request.user
        self.object = get_object_or_404(Review, id=self.kwargs['pk'])
        if user.is_superuser:
            messages.success(
                self.request, 'Review deleted!'
            )
            self.object.delete()
        elif user.id == self.object.user.id:
            messages.success(
                self.request, f'Thanks, {user}. Your review has been removed.'
            )
            self.object.delete()
        therapy_pk = self.request.resolver_match.kwargs['therapy_pk']
        self.success_url = (
            f'/therapies/therapy_details/{str(therapy_pk)}/'
        )
        return redirect(self.success_url)
