from therapies import views
from django.urls import path

urlpatterns = [
    path('', views.TherapiesView.as_view(), name='therapies'),
    path(
        'add_therapy/',
        views.AddTherapyView.as_view(),
        name='add_therapy'
    ),
]
