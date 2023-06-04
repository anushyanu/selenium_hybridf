from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        user_clear = self.driver.find_element(By.ID, self.textbox_username_id)
        user_clear.clear()
        user = self.driver.find_element(By.ID, self.textbox_username_id)
        user.send_keys(username)

    def setPassword(self, password):
        pwd_clear = self.driver.find_element(By.ID, self.textbox_password_id)
        pwd_clear.clear()
        pwd = self.driver.find_element(By.ID, self.textbox_password_id)
        pwd.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

