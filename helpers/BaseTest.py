#emcapsule éléments de sélénium
#chromedriver_path = 'D:\\chromedriver\\chromedriver.exe' #compris dans webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager


class BaseTest:

    def setup_method(self): #environnement différent selon que l'on est en local et en CI (headless / sans visuel)
        options = Options()
        if os.environ.get("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        else:
            print("Running in non-CI environment, launching browser with GUI.")
            options.add_argument("start-maximized")
            # ici pour choisir le navigateur
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def open_application(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php")

    # travailler avec les fichiers json.
    def get_user_data(self, user_key="guest_user_1"):
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")
        with open(data_path, "r") as f:
            return json.load(f)[user_key]