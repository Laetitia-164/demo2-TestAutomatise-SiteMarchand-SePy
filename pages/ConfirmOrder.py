from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ConfirmOrder:

    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = driver.title
         self.btn_confirm= '//button[@id="button-confirm"]'
            # ou Click "Confirm Order button" = //*[@id='button-confirm']

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class ConfirmOrder : My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    def clickOn_ConfirmOrder (self):
        c_btn_confirm = self.driver.find_element(By.XPATH, self.btn_confirm)
        c_btn_confirm.click()
