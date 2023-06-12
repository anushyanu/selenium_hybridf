import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage  # importing class
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xl_utils


class Test_001_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    #path = "/home/anushya/Desktop/ddt_test_login.xlsx"
    path = "./testData/ddt_test_login.xlsx"

    logger = LogGen.loggen()

    def test_ddt_login(self, setup):
        self.logger.info("******** test_002_ddt_login ************")
        self.logger.info("******** verifying test_login_ddt test ************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = xl_utils.getRowCount(self.path, "Sheet1")
        list_status = []
        for r in range(2, self.rows + 1):
            self.user = xl_utils.readData(self.path, "Sheet1", r, 1)
            print(self.user)
            self.pwd = xl_utils.readData(self.path, "Sheet1", r, 2)
            print(self.pwd)
            self.exp = xl_utils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("** passed **")
                    self.lp.logout()
                    list_status.append("pass")
                if self.exp == "fail":
                    self.logger.info("** failed **")
                    self.lp.logout()
                    list_status.append("fail")

            if act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("** failed **")

                    list_status.append("fail")
                if self.exp == "fail":
                    self.logger.info("** passed **")

                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("***** Login DDT test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test is failed ***** ")
            self.driver.close()
            assert False

        self.logger.info("**** end of login DDT test case ****")
        self.logger.info(" *** completed login_ddt_002 testcase*******")
