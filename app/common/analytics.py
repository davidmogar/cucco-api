import os
import requests

GA_URL = 'http://www.google-analytics.com/collect'
GA_TRACKING_ID = os.environ['GA_TRACKING_ID']

def track_event(category, action, label=None, value=0):
    """Send a new event to Google Analytics.

    Attributes:
        category: Category of the event.
        action: Action performed.
        label: Label for the new event.
        value: Value to associate with the event.
    """
    data = {
        'v': '1',               # API version
        'tid': GA_TRACKING_ID,  # Tracking ID
        'cid': '555',
        'ds': 'api',            # Data source
        't': 'event',           # Event hit type
        'ec': category,         # Event category
        'ea': action,           # Event action
        'el': label,            # Event label
        'ev': value,            # Event value
    }

    response = requests.post(GA_URL, data=data)
