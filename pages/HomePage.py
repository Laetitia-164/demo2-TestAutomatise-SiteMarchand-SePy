from selenium.webdriver.remote.webdriver import WebDriver
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs
# documentation https://www.selenium.dev/documentation/webdriver/

class HomePage:

    # constructeur - attribut - méthode
    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = "Your Store" #driver.title

    # def current.url

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class HomePage : My current title is : {current_website_title}") # à remplacer par un logger
        assert current_website_title == wishedValue
