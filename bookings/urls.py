from . import views
from django.urls import path

urlpatterns = [
    path('book', views.BookingInfoView.as_view(), name='booking_info'),
]
