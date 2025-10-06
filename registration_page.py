from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):

    FIRST_NAME_LOCATOR = (By.ID, "signupName")
    LAST_NAME_LOCATOR = (By.ID, "signupLastName")
    EMAIL_LOCATOR = (By.ID, "signupEmail")
    PASSWORD_LOCATOR = (By.ID, "signupPassword")
    REPEAT_PASSWORD_LOCATOR = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Register']")
    SUCCESS_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".alert-success")

    @property
    def first_name(self):
        return self.wait_for_visible(self.FIRST_NAME_LOCATOR)

    @property
    def last_name(self):
        return self.wait_for_visible(self.LAST_NAME_LOCATOR)

    @property
    def email(self):
        return self.wait_for_visible(self.EMAIL_LOCATOR)

    @property
    def password(self):
        return self.wait_for_visible(self.PASSWORD_LOCATOR)

    @property
    def repeat_password(self):
        return self.wait_for_visible(self.REPEAT_PASSWORD_LOCATOR)

    @property
    def register_button(self):
        return self.wait_for_clickable(self.REGISTER_BUTTON_LOCATOR)

    @property
    def success_message(self):
        return self.wait_for_visible(self.SUCCESS_MESSAGE_LOCATOR)
