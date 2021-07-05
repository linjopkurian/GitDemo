"""
This is End to End program
Author : Linjo P Kurian

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        log = self.getlogger()
        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        checkoutpage = CheckoutPage(self.driver)
        products = checkoutpage.getPhoneDetails()
        for product in products:
            prod_name = checkoutpage.getProdname(product)
            log.info("Product Name:" + prod_name)
            # prod_name = product.find_element_by_xpath("div/h4/a").text
            if prod_name == "Blackberry":
                log.info("Item Matched proceeding to checkout with :" + prod_name)
                checkoutpage.click(product)
                # product.find_element_by_xpath("div/button").click()
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        self.driver.find_element_by_id("country").send_keys("Ind")
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = (self.driver.find_element_by_class_name("alert-success").text)

        assert "Success! Thank you!" in successText
        log.info("Checkout completed"+successText)
        self.driver.get_screenshot_as_file("success.png")
