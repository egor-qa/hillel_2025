import os
import pytest
import logging
from homework10 import log_event

log_file = "login_system.log"

@pytest.fixture(autouse=True)
def clear_log_file():
    """Clear log before test."""
    if os.path.exists(log_file):
        os.remove(log_file)
    # Clear log
    logger = logging.getLogger("log_event")
    logger.handlers.clear()


@pytest.mark.parametrize(
    "status,expected_level",
    [
        ("success", "INFO"),
        ("expired", "WARNING"),
        ("failed", "ERROR"),
        ("unknown", "ERROR"),  # extra case
    ]
)
def test_log_event_appends_to_log_file(status, expected_level):
    username = "Yehor"
    expected_message = f"Login event - Username: {username}, Status: {status}"

    log_event(username, status)

    assert os.path.exists(log_file), "Log file was not created."

    with open(log_file, "r", encoding='utf-8') as file:
        lines = file.readlines()

    # Останній запис
    last_entry = lines[-1].strip()

    assert expected_message in last_entry, f"Expected message not found: {last_entry}"
    assert expected_level in last_entry, f"Expected level {expected_level} not found: {last_entry}"
