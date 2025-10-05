import sys
from pathlib import Path
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from selenium.webdriver import Chrome

# Add the project root to PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parents[2]))

from core.UI.nova_post.pages.search import SearchPage

# Logging settings
log_conf_path = Path(__file__).resolve().parents[2] / "lesson_27" / "logging.conf"
logger = logging.getLogger()

@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

def test_tracking(driver):
    ttn = "59001458016240"  # or other valid TTN
    expected_status = "Отримана"

    page = SearchPage(driver)
    page.open_page()
    page.search(ttn)
    actual_status = page.get_search_result_text()

    logger.info(f"Status received: '{actual_status}'")

    assert actual_status == expected_status, f"Expected: '{expected_status}', received: '{actual_status}'"