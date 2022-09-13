from therapies import views
from django.urls import path

urlpatterns = [
    path('', views.TherapiesView.as_view(), name='therapies'),
    path(
        'add_therapy/',
        views.AddTherapyView.as_view(),
        name='add_therapy'
    ),
    path(
        'edit_therapy/<int:pk>',
        views.EditTherapyView.as_view(),
        name='edit_therapy'
    ),
    path(
        'delete_therapy/<int:pk>',
        views.DeleteTherapyView.as_view(),
        name='delete_therapy'
    ),
]
