from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

#from time import sleep

class HeaderPageFragment():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.menu = '//span[contains(text(),"Mega Menu")]'
         self.subMenu = '//a[contains(text(),"Power bank")]'
            # ou //*[contains(@title, 'Power bank')]

    def select_menu (self):
        c_menu = self.driver.find_element(By.XPATH, self.menu)
        #c_menu.click()
        # Mouse Over
        ActionChains(self.driver) \
            .move_to_element(c_menu) \
            .perform()

    def select_submenu (self):
        c_submenu = self.driver.find_element(By.XPATH, self.subMenu)
        c_submenu.click()
        #sleep(10)