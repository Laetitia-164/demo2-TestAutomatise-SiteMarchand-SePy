#https://ecommerce-playground.lambdatest.io/
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..")) # .. on remontepip

from time import sleep

from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import HeaderPageFragment
from pages.ProductListPage import ProductListPage
from pages.ProductPage import ProducPage
from pageFragments.AddToCartPopUpPage import AddToCartPopUp
from pages.CartPage import CartPage
from pages.CheckOutPage import CheckOut_donnee
from pages.ConfirmOrder import ConfirmOrder
from pages.ConfirmSendPage import ConfirmSend

class Test_FirstTest(BaseTest): # héritage

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        self.open_application()

        # page d'accueil
        # 2 approches tester URL (pb si env change) ou titre de la page
        home = HomePage(self.driver) #instanciation (créer bj avec des classes) avec méthode héritée - home obj classe HomePage
        home.is_page_visible("Your Store")

        # naviguer dans le menu principal et aller sur une page
        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_submenu()

        # page des produits : filtre et sélection produit
        productList = ProductListPage(self.driver)
        pageDesProduits = "Mac"
        productList.is_page_visible(pageDesProduits)
        productList = ProductListPage(self.driver)
        productList.clickOn_FilterInStock()
        sleep(3) # vérifier que page chargée
        productList.select_div_ProductItem()

        # page d'un produit
        productPage = ProducPage(self.driver)
        productPage.is_page_visible('HP LP3065')
        productPage.select_addToCart()

        # pop-up du panier
        cartPopUp = AddToCartPopUp(self.driver)
        sleep(0.05)  # vérifier que page chargée
        cartPopUp.select_cart_view()

        #page du checkout
        viewCart_page = CartPage(self.driver)
        sleep(0.05)
        viewCart_page.is_page_visible('Shopping Cart')
        viewCart_page.clickOn_CheckOut()

        #information sur la commande
            #variables
        first_name = "Jeanne"
        last_name = "Paris"
        e_mail = "jeanne.paris@gmail.com"
        telephone = "0033600000000"
        adress_1 = "1 bd du général de gaulle"
        city = "Brest"
        post_code = "29555"
        country = "France, Metropolitan"
        region_state = "Finistère"

            #actions
        checkOutPage = CheckOut_donnee(self.driver)
        checkOutPage.is_page_visible('Checkout')
        sleep(1)
        checkOutPage.select_checkout_guest()

        checkOutPage.envoi_donnee_prenom_byName(first_name)
        checkOutPage.envoi_donnee_nom(last_name)
        checkOutPage.envoi_donnee_mail(e_mail)
        checkOutPage.envoi_donnee_telephone(telephone)
        checkOutPage.envoi_donnee_adresse(adress_1)
        checkOutPage.envoi_donnee_ville(city)
        checkOutPage.envoi_donnee_codePostal(post_code)
        #checkOutPage.envoi_donnee_(first_name,last_name,e_mail)
        checkOutPage.envoi_donnee_pays(country)
        checkOutPage.envoi_donnee_region(region_state)

        checkOutPage.select_accept_terms()
        sleep(0.2)
        checkOutPage.select_save()

        # confirmation de commande
        sleep(0.2)
        confirm_page = ConfirmOrder(self.driver)
        confirm_page.is_page_visible('Confirm Order')
        confirm_page.clickOn_ConfirmOrder()

        # commande passée
        sleep(0.2)
        send_page = ConfirmSend(self.driver)
        send_page.is_page_visible('Your order has been placed!')
        try:
            send_page.is_h1_correct('Your order has been placed!')
            print("commande passée")
        except AssertionError:
            print("h1 incorrect - commande non passée")
        send_page.clickOn_SendOrder()