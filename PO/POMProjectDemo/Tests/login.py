import time
from POMProjectDemo.Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProjectDemo.Pages.LoginPage import LoginPage
from POMProjectDemo.Pages.HomePage import Homepage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/kentik/PycharmProjects/PO/POMProjectDemo/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")
        login_page = LoginPage(driver)
        login_page.login_form.enter_username("NotAdmin")
        login_page.login_form.enter_username("Admin")
        login_page.login_from.enter_password("admin123")
        login_page.login_form.click_login()

        # TODO: Wait for page to reload
        # TODO: Check session token instead of home page

        homepage = Homepage(driver)
        homepage.click_menu()
        homepage.click_logout()

        time.sleep(2)


    def test_login_invalid_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(2)
        login.check_invalid_username_message()


        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Finish")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kentik/PycharmProjects/PO/POMProjectDemo/reports"))

