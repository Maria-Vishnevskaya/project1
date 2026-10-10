import requests
from configuration import URL_SERVICE, REQUEST_TIMEOUT

def post_create_order(body):
    url = f"{URL_SERVICE}/api/v1/orders"
    return requests.post(url, json=body, timeout=REQUEST_TIMEOUT)

def get_order_by_track(track_number):
    # 
    url = f"{URL_SERVICE}/api/v1/orders/track"
    params = {"t": track_number}
    return requests.get(url, params=params, timeout=REQUEST_TIMEOUT)