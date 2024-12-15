import time

from pages.homepage import Homepage


class Test_home:
    def test_search(self):
        home_page= Homepage(self.driver)
        home_page.from_textbox_enter_by_XPATH()
        time.sleep(5)