from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class AddToCartPopUp:

    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.__website_title = driver.title
        self.btn_Cartview = '//a[contains(text(),"View Cart ")]'
            # ou //*[contains(text(),"Checkout")]

    def select_cart_view(self):
        c_btn_Cartview = self.driver.find_element(By.XPATH, self.btn_Cartview)
        c_btn_Cartview.click()