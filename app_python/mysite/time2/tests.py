"""
This module is providing the test cases for the website that shows current Moscow time
"""
from datetime import datetime, timezone
from django.test import TestCase
from freezegun import freeze_time
import pytz
from . import views

# Create your tests here.
timezone = pytz.timezone('Europe/Moscow')


class DateTestCase(TestCase):
    """
    This class is created to test
    """
    datetime_moscow = datetime.now(timezone)

    @freeze_time(datetime_moscow)
    def test_get_current_time(self):

        """
        method tests that the my website shows the correct time in moscow
        :return:
        """
        request = views.get_time()
        current_time = datetime.now(timezone)

        self.assertEqual(request, current_time)
