"""
This module is providing the functionality for the webpage that displays time in Moscow
"""
from datetime import datetime
from django.shortcuts import render
import pytz


def get_time():
    """
    Method index is design to get the time in Moscow
    """
    # get the Moscow current date and time
    timezone = pytz.timezone('Europe/Moscow')
    time_now = datetime.now(timezone)

    return time_now


def index(request):
    """
    Method index is design to render all the data into template
    """

    time_now = get_time()
    # store only time without milliseconds
    moscow_time = {
        'hour': time_now.hour,
        'minute': time_now.minute,
    }

    # to pas the time for rendering
    context = {'moscow_time': moscow_time}

    return render(request, 'time2/website.html', context)
