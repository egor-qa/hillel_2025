import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_site(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    return driver

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def go_to_registration(open_site, main_page):
    open_site
    main_page.sign_up_button.click()