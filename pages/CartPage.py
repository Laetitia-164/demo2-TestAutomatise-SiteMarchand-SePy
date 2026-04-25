from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = driver.title
         self.a_checkout= '//a[contains(text(),"Checkout")]'

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class CartPage : My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    def clickOn_CheckOut (self):
        c_a_checkout = self.driver.find_element(By.XPATH, self.a_checkout)
        c_a_checkout.click()
