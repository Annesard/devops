"""
This module is providing the functionality for the webpage that displays time in Moscow
"""
from datetime import datetime
from django.shortcuts import render
import pytz


def index(request):
    """
    Method index is design to get the current time in Moscow, Russia
    """
    # get the Moscow current date and time
    timezone = pytz.timezone('Europe/Moscow')
    time_now = datetime.now(timezone)

    # store only time without milliseconds
    moscow_time = {
        'hour': time_now.hour,
        'minute': time_now.minute,
    }

    # to pas the time for rendering
    context = {'moscow_time': moscow_time}

    return render(request, 'time2/website.html', context)
