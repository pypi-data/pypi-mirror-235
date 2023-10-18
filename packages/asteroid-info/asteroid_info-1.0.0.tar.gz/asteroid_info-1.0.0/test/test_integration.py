import pytest
import requests
import sys
sys.path.insert(0,"./")
from main import get_largest_asteroid,get_volume_asteroid,get_surface_area_asteroid

ENDPOINT = "https://api.nasa.gov/neo/rest/v1/feed"
api_key = "tScvcOsV1N888Hx8M2gDh1lg1WEHltZhmdMYVl0x"
date = '2023-09-05'


def get_response():
    parameters = {
        "start_date": date,
        "end_date": date,
        "api_key": api_key
    }
    return requests.get(ENDPOINT, params=parameters, timeout=5)


def test_can_call_endpoint():
    response = get_response()
    assert response.status_code == 200


def test_get_volume_asteroid():
    response = get_response()
    asteroids_info = response.json()
    _, largest_diameter = get_largest_asteroid(asteroids_info, date)
    volume = get_volume_asteroid(largest_diameter)
    assert isinstance(volume, (float, int))
    assert volume >= 0
    assert round(volume,2) == 108050423.36


def test_get_surface_area_asteroid():
    response = get_response()
    asteroids_info = response.json()
    _, largest_diameter = get_largest_asteroid(asteroids_info, date)
    surface_area = get_surface_area_asteroid(largest_diameter)
    assert isinstance(surface_area, (float, int))
    assert surface_area >= 0
    assert round(surface_area,2) == 1097071.94
