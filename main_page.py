from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):

    SIGN_UP_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Sign up']")

    @property
    def sign_up_button(self):
        return self.wait_for_clickable(self.SIGN_UP_BUTTON_LOCATOR)