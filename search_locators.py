from selenium.webdriver.common.by import By

class SearchLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.track__form-group-input")
    RESULT_TEXT = (By.CSS_SELECTOR, "div.header__status-text")