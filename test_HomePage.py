import pytest

from TestData.HomePageData import HomePageData
from pageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.support.select import Select

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getlogger()
        #driver.find_element_by_css_selector("input[name= 'name']").send_keys("Linjo P Kurian")
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        log.info("Entered first name:"+getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        log.info("Entered email id :"+getData["email"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmitButton().click()
        message = homepage.getMessage().text
        try:
            assert "Success" in message
            log.info("Message is:" + message)

        except AssertionError as e:
            log.critical("No success message")

        self.driver.refresh()

        # driver.close()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param
