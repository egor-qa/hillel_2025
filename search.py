from core.UI.nova_post.pages.base import BasePage
from core.UI.nova_post.locators.search_locators import SearchLocators
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    def open_page(self):
        self.open(self.URL)

    def search(self, ttn: str):
        input_field = self.wait_for_element(SearchLocators.SEARCH_INPUT)
        input_field.clear()
        input_field.send_keys(ttn)
        input_field.send_keys(Keys.ENTER)

    def get_search_result_text(self) -> str:
        result_elem = self.wait_for_visible(SearchLocators.RESULT_TEXT)
        return result_elem.text.strip()