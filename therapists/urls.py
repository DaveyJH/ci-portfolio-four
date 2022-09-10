from therapists import views
from django.urls import path

urlpatterns = [
    path('', views.TherapistsView.as_view(), name='therapists'),
]
