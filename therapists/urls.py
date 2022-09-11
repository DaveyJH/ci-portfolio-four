from therapists import views
from django.urls import path

urlpatterns = [
    path('', views.TherapistsView.as_view(), name='therapists'),
    path(
        'add_therapist/',
        views.AddTherapistView.as_view(),
        name='add_therapist'
    ),
    path(
        'delete_therapist/',
        views.TherapistsView.as_view(),
        name='delete_therapist'
    ),
    path(
        'edit_therapist/<int:pk>',
        views.EditTherapistView.as_view(),
        name='edit_therapist'
    ),
]
