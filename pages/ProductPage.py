from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ProducPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.__website_title = driver.title
        self.btn_addToCart = '//div[@id="entry_216842"]//button[contains(text(),"Add to Cart")]'
        # ou //button[@title= "Add to Cart"][2]

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class ProducPage : My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    def select_addToCart(self):
        c_btn_btn_addToCart = self.driver.find_element(By.XPATH, self.btn_addToCart)
        c_btn_btn_addToCart.click()