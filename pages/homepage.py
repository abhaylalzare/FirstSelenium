from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Homepage:
    def __init__(self,driver):
        self.from_textbox_by_XPATH = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div[1]/div/label')
        self.from_textbox_enter_by_XPATH = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div[1]/div/span')
        self.to_textbox_by_XPATH = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/div/label')
        self.to_textbox_enter_by_XPATH = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/div/span')

    def click(self,by_locator):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located(by_locator)).click()

    def click_on_from_textbox(self):
        self.click(self.from_textbox_by_XPATH)

    def click_on_to_textbox(self):
        self.click(self.to_textbox_by_XPATH)