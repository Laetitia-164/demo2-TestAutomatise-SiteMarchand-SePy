from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_current_title(self) -> str:
        return self.driver.title