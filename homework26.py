import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


@pytest.fixture(scope="session")
def chrome_driver():
    print(">>> Start ChromeDriver and open the page <<<")


    service = ChromeService(executable_path="path/to/chromedriver")
    driver = ChromeDriver(service=service)

    driver.get("http://localhost:8000/lesson26/dz.html")
    driver.maximize_window()

    yield driver

    print(">>> Ending the session and closing the browser <<<")
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def verify_secret_text(chrome_driver, request):
    frame_id, secret_value = request.param

    chrome_driver.switch_to.frame(frame_id)

    input_selector = "#input1" if frame_id == "frame1" else "#input2"
    input_field = chrome_driver.find_element(By.CSS_SELECTOR, input_selector)

    input_field.clear()
    time.sleep(0.5)
    input_field.send_keys(secret_value)

    check_button = chrome_driver.find_element(By.TAG_NAME, "button")
    time.sleep(0.5)
    check_button.click()

    alert = Alert(chrome_driver)
    time.sleep(0.5)
    alert_text = alert.text
    alert.accept()

    chrome_driver.switch_to.default_content()
    time.sleep(0.5)

    yield alert_text