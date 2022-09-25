from POMProjectDemo.Locators.locators import Locators
from selenium.webdriver.common.by import By

class Homepage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_link_text = Locators.logout_link_text

    def click_menu(self):
        self.driver.find_element(By.XPATH, Locators.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, Locators.logout_link_text).click()


