from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ConfirmSend:

    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = driver.title
         self.btn_send= '//a[contains(text(),"Continue")]'
            # ou Click "Confirm Order button" = //*[@id='button-confirm']
         self.h1 = '//h1'
            # ou //h1[text()=" Your order has been placed!"]

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class ConfirmSendPage: My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    def clickOn_SendOrder (self):
        c_btn_send = self.driver.find_element(By.XPATH, self.btn_send)
        c_btn_send.click()

    def is_h1_correct(self, wishedValue: str):
        nom_h1 = self.driver.find_element(By.XPATH, self.h1).text
        print(f"class ConfirmSendPage : My current h1 is : {nom_h1}")
        assert nom_h1 == str(wishedValue)

    def displayH1(self)-> str:
        return self.driver.find_element(By.XPATH, self.h1).text



