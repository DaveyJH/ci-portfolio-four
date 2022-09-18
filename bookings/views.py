from django.http import HttpResponseServerError
from django.views.generic import TemplateView
from .models import BookingInfo
from home.models import Home


class BookingInfoView(TemplateView):
    """Renders some basic booking information"""
    template_name = "bookings/booking_info.html"

    def get_context_data(self, **kwargs):
        """Returns address from Home model and all booking info

        Try:except allows for erroneous extra Home/BookingInfo models

        ---
        Raises:
            500 error if no Home or BookingInfo object is found
        """
        try:
            booking_details = BookingInfo.objects.all()[0]
            home = Home.objects.all()[0]
        except IndexError:
            raise HttpResponseServerError()
        context = {
            'booking_details': booking_details,
            'address': home.address,
            'days': [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
        }
        return context
