from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        # = self.driver.find_element(By.ID, self.textbox_username_id)
        user = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.textbox_username_id))
        )
        user.clear()
        #user = self.driver.find_element(By.ID, self.textbox_username_id)
        user.send_keys(username)

    def setPassword(self, password):
        pwd= WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.textbox_password_id))
        )
        # = self.driver.find_element(By.ID, self.textbox_password_id)
        pwd.clear()
        #pwd = self.driver.find_element(By.ID, self.textbox_password_id)
        pwd.send_keys(password)

    def clickLogin(self):
        #login = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        login.click()

    def logout(self):
        #out = self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text)
        out = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_link_text))
        )
        out.click()

