import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth
import os

# Logging to file + console

log_path = os.path.join(os.path.dirname(__file__), 'test_search.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Fixture — login once per class

@pytest.fixture(scope='class')
def auth_session():
    """Creates a requests.Session with a Bearer token."""
    base_url = "http://127.0.0.1:8080"

    s = requests.Session()
    auth_url = f"{base_url}/auth"

    username = "test_user"
    password = "test_pass"

    resp = s.post(auth_url, auth=HTTPBasicAuth(username, password))
    assert resp.status_code == 200, f"Auth failed: {resp.text}"
    token = resp.json().get("access_token")
    assert token, "No token received"

    s.headers.update({'Authorization': f'Bearer {token}'})
    logger.info("Authentication successful, token stored.")
    return s

# Parameterized test

@pytest.mark.usefixtures("auth_session")
class TestCarsAPI:

    @pytest.mark.parametrize(
        "sort_by,limit",
        [
            ("price", 3),
            ("year", 5),
            ("brand", 4),
            ("engine_volume", 6),
            ("price", 10),
            ("year", 2),
        ]
    )
    def test_cars_search(self, auth_session, sort_by, limit):
        base_url = "http://127.0.0.1:8080/cars"
        params = {"sort_by": sort_by, "limit": limit}

        logger.info(f"Request /cars with sort_by={sort_by}, limit={limit}")
        r = auth_session.get(base_url, params=params)

        assert r.status_code == 200, f"Bad status: {r.status_code} {r.text}"
        cars = r.json()

        # Check number of results
        assert isinstance(cars, list), "Expected a list"
        assert len(cars) <= limit, f"Returned more than {limit}"

        logger.info(f"Received {len(cars)} records")

        # Check sorting
        if cars:
            values = [c[sort_by] for c in cars]
            sorted_values = sorted(values)
            assert values == sorted_values, f"Sorting by {sort_by} failed"

        logger.info(f"Test sort_by={sort_by}, limit={limit} passed")