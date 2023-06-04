import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage # importing class
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("************ Test__001__Login ******************")
        self.logger.info("************* verifying home page title **********")

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("************ home page title is passed **********")
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_homePageTitle.png")
            self.driver.close()

            self.logger.error("*********** home page title is failed *********")
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** login test is passed ******* ")
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_login.png")

            self.driver.close()
            self.logger.error("********* login test is failed ********* ")
            assert False








