import requests

HEROES_URL = "https://api.deadlock-api.com/v1/assets/heroes"
ITEMS_URL = "https://api.deadlock-api.com/v1/assets/items"


def fetch_heroes():
    response = requests.get(HEROES_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def fetch_items():
    response = requests.get(ITEMS_URL, timeout=10)
    response.raise_for_status()
    return response.json()