import pytest
import logging
from lesson_10.homework10 import (
    log_event,
)


@pytest.mark.parametrize(
    "status,expected_level",
    [
        ("success", logging.INFO),
        ("expired", logging.WARNING),
        ("failed", logging.ERROR)
    ]
)
def test_log_event_logging_levels(caplog, status, expected_level):
    username = "Yehor"
    expected_msg = f"Login event - Username: {username}, Status: {status}"

    # caplog - captures logger messages
    with caplog.at_level(logging.DEBUG):  # covering all levels
        log_event(username, status)

    # Search messages in caplog.records
    messages = [record for record in caplog.records if expected_msg in record.message]
    assert len(messages) == 1, f"Expected one log for '{status}'"
    assert messages[0].levelno == expected_level