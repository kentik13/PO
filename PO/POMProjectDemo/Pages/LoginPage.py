from POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

        self.usernama_texbox_name = Locators.username_texbox_name
        self.password_texbox_name = Locators.password_texbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidUsername_message_xpath = Locators.invalidUsername_message_xpath


    def enter_username(self,username):
        self.driver.find_element(By.NAME, Locators.username_texbox_name).clear()
        self.driver.find_element(By.NAME, Locators.username_texbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, Locators.password_texbox_name).clear()
        self.driver.find_element(By.NAME, Locators.password_texbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,Locators.login_button_xpath).click()

    def check_invalid_username_message(self):
        message = self.driver.find_element(By.XPATH, Locators.invalidUsername_message_xpath).text
        assert message == "Invalid credentials"



