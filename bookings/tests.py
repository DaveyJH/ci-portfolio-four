from django.test import TestCase
from .models import BookingInfo
from home.models import Home


class TestViews(TestCase):

    def setUp(self):
        """creates a home object"""
        self.home = Home(content="Some content", address="an address")
        self.home.save()

    def test_booking_info_template(self):
        """Tests bookings page renders when all necessary data is present"""
        self.booking_info = BookingInfo(
            message="A message",
            contact_info="0761234567",
            open_times={
                "Monday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Tuesday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Wednesday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Thursday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Friday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Saturday": {
                    "open": "0900",
                    "close": "1400",
                },
                "Sunday": {
                    "open": "0900",
                    "close": "1400",
                },
            }
        )
        self.booking_info.save()
        response = self.client.get('/bookings/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_info.html')
        self.assertTemplateUsed(response, 'base.html')
