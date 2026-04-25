from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ProductListPage:

    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = driver.title
         self.lbl_AvailabilityFilter = '//input[@id="mz-fss-0--1"]/following-sibling::label[contains(text(),"In stock")]'
            # ou //label[@for='mz-fss-0--1']
         self.div_productItem = '(//div[@class="product-thumb-top"])[6]'
            # ou //*[@class= "carousel-item active"]/*[@class= "lazy-load"]

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class ProductListPage : My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    def clickOn_FilterInStock (self):
        c_lbl_AvailabilityFilter = self.driver.find_element(By.XPATH, self.lbl_AvailabilityFilter)
        c_lbl_AvailabilityFilter.click()

    def select_div_ProductItem(self):
        c_div_ProductItem = self.driver.find_element(By.XPATH, self.div_productItem)
        c_div_ProductItem.click()