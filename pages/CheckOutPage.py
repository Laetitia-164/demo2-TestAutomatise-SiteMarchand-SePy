from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# bonne pratique : créer une méthode par selector, plus maintanable à terme
# créer un dico avec (nomlocator, donnee) pas bonne idée pas mantenable à terme

class CheckOut_donnee:
    def __init__(self, driver: WebDriver): #constructeur
         self.driver = driver
         self.__website_title = driver.title
         self.lbl_select_checkout_guest = '//label[@for="input-account-guest"]'
             #'//input[@id="input-account-guest"]/following-sibling::label[contains(text(),"Guest Checkout")]'
            # ou //label[@for='input-account-guest']
         self.btn_select_accept_terms = '//*[@for="input-agree"]'
             #'//input[@id="input-account-agree"]/following-sibling::label'
            # ou Accept conditions & terms = //*[@for='input-agree']
         self.btn_select_save = '//button[@id="button-save"]'
            # ou Click "Continue" = //*[@id='button-save']

        # xpath donnée formulaire
         self.first_name = '//input[@name="firstname"]'
         self.last_name = '//input[@name="lastname"]'
         self.e_mail = '//input[@name="email"]'
         self.telephone = '//input[@name="telephone"]'
         self.adress_1 = '//input[@name="address_1"]'
         self.city = '//input[@name="city"]'
         self.post_code = '//input[@name="postcode"]'
             # ou Fill mandatory fields = //input[@name='firstname'], //input[@name='lastname'], //input[@name='email'],
             #//input[@name='telephone'], //input[@name='company'], //input[@name='address_1'], //input[@name='adress_2'],
             #//input[@name='city'], //input[@name='postcode']
         #self.country = '//select[@name="country_id"]//option[@value="74"]'
         #self.region_state = '//select[@name="zone_id"]//option[contains(text(),"Finistère")]'

         self.donnee_formulaire = '//input[@name="'

         # nom donnée formulaire
         self.first_name_nom = "firstname"
         self.country_nom = "country_id"
         self.region_nom = "zone_id"

    # page visible
    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"class CheckOut_donne: My current title is : {current_website_title}")
        assert current_website_title == wishedValue

    # bouton
    def select_checkout_guest(self):
        c_lbl_select_checkout_guest = self.driver.find_element(By.XPATH, self.lbl_select_checkout_guest)
        c_lbl_select_checkout_guest.click()

    def select_accept_terms(self):
        c_btn_select_accept_terms = self.driver.find_element(By.XPATH, self.btn_select_accept_terms)
        c_btn_select_accept_terms.click()

    def select_save(self):
        c_btn_select_confirm = self.driver.find_element(By.XPATH, self.btn_select_save)
        c_btn_select_confirm.click()

    # donnée par xpath
    def envoi_donnee_prenom(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.first_name)
        input_nom.send_keys(info)

    def envoi_donnee_nom(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.last_name)
        input_nom.send_keys(info)

    def envoi_donnee_mail(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.e_mail)
        input_nom.send_keys(info)

    def envoi_donnee_telephone(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.telephone)
        input_nom.send_keys(info)

    def envoi_donnee_adresse(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.adress_1)
        input_nom.send_keys(info)

    def envoi_donnee_ville(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.city)
        input_nom.send_keys(info)

    def envoi_donnee_codePostal(self, info: str):
        input_nom = self.driver.find_element(By.XPATH, self.post_code)
        input_nom.send_keys(info)

    # par Name
    def envoi_donnee_prenom_byName(self, info: str):
        input_nom = self.driver.find_element(By.NAME, self.first_name_nom)
        input_nom.send_keys(info)

    # menu déroulant info passé
    def envoi_donnee_pays(self, info: str):
        input_nom = self.driver.find_element(By.NAME, self.country_nom)
        select = Select(input_nom)
        select.select_by_visible_text(info)

    def envoi_donnee_region(self, info: str):
        input_nom = self.driver.find_element(By.NAME, self.region_nom)
        select = Select(input_nom)
        select.select_by_visible_text(info)


    def envoi_donnee_(self, nom,prenom, email: str):
        #autre méthode de raisonnement
        input_nom1 = self.driver.find_element(By.XPATH, self.first_name)
        input_nom1.send_keys(nom)
        input_nom2 = self.driver.find_element(By.XPATH, self.last_name)
        input_nom2.send_keys(prenom)
        input_nom3 = self.driver.find_element(By.XPATH, self.email)
        input_nom3.send_keys(email)