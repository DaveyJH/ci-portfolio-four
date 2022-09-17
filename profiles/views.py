from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Review
from therapists.models import Therapist


class UserProfileView(
    LoginRequiredMixin,
    ListView
):
    """
    View to render reviews on profile page
    """
    model = Review
    template_name = 'profiles/profile.html'

    def get_queryset(self, *args, **kwargs):
        """
        - Returns all reviews by a standard user OR
        - Return all approved reviews about a staff user OR
        - Returns all reviews for a superuser
        """
        user = get_object_or_404(User, id=self.kwargs['pk'])
        print(user)
        print(user.id)
        if not user.is_superuser:
            queryset = Review.objects.filter(user=user.id)
        if user.is_staff and not user.is_superuser:
            this_staff_member = get_object_or_404(
                Therapist,
                first_name=user.first_name,
                last_name=user.last_name
            )
            queryset = queryset.union(Review.objects.filter(
                therapist=this_staff_member
            ).filter(
                approved=True
            ))
        if user.is_superuser:
            queryset = Review.objects.all().order_by('approved', '-date_time')
        return queryset

    def get_context_data(self):
        """Returns site owner and calculated reviews"""
        OWNER = get_object_or_404(
            Therapist, first_name="Marek", last_name="Frisk"
        )
        print(self.queryset)
        context = {
            'reviews': self.get_queryset(),
            'owner': OWNER,
        }
        return context
