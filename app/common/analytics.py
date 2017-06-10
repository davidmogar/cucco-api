import os
import requests

GA_URL = 'http://www.google-analytics.com/collect'
GA_TRACKING_ID = os.environ['GA_TRACKING_ID']

def track_event(category, action, label=None, value=0):
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
