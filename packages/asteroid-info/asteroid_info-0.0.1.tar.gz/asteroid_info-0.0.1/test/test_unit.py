import pytest
import requests
import sys
sys.path.insert(0,"./")
from main import get_largest_asteroid, check_potentially_hazardous_asteroids,count_asteroids

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


def test_count_asteroids():
    response = get_response()
    asteroids_info = response.json()
    num_asteroids = count_asteroids(asteroids_info, date)
    assert isinstance(num_asteroids, (float, int))
    assert num_asteroids >= 0
    assert num_asteroids == 10


def test_get_largest_asteroid():
    response = get_response()
    asteroids_info = response.json()
    largest_asteroid_id, largest_diameter = get_largest_asteroid(asteroids_info, date)
    assert isinstance(largest_diameter, (float, int))
    assert largest_diameter >= 0
    assert round(largest_diameter,2) == 590.94


def test_check_potentially_hazardous_asteroids():
    response = get_response()
    asteroids_info = response.json()
    potentially_hazardous = check_potentially_hazardous_asteroids(asteroids_info, date)
    assert isinstance(potentially_hazardous, bool)
    assert potentially_hazardous == True