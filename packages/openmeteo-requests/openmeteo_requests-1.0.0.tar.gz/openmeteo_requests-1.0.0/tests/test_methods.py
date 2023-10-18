"""Test client"""
from __future__ import annotations

import pytest

import openmeteo_requests


def test_fetch_all():
    om = openmeteo_requests.Client()
    params = {
        "latitude": [52.54, 48.1, 48.4],
        "longitude": [13.41, 9.31, 8.5],
        "hourly": ["temperature_2m", "precipitation"],
        "start_date": "2023-08-01",
        "end_date": "2023-08-02",
        # 'timezone': 'auto',
        # 'current': ['temperature_2m','precipitation'],
        # 'current_weather': 1,
    }

    results = om.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)
    assert len(results) == 3
    result = results[0]
    assert result.Latitude() == pytest.approx(52.5)
    assert result.Longitude() == pytest.approx(13.4)
    result = results[1]
    assert result.Latitude() == pytest.approx(48.1)
    assert result.Longitude() == pytest.approx(9.3)
    result = results[0]

    print(f"Coordinates {result.Latitude()}°E {result.Longitude()}°N {result.Elevation()} m asl")
    print(f"Timezone {result.Timezone()} {result.TimezoneAbbreviation()} {result.UtcOffsetSeconds()}")
    print(f"Generation time {result.GenerationtimeMs()} ms")


def test_int_client():
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
