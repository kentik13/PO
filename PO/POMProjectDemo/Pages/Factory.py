from .HomePage import Homepage
from .LoginPage import LoginPage


class On:
    def __init__(self, driver):
        self.__driver = driver

    @property
    def login_page(self):
        return LoginPage(self.__driver)

    @property
    def home_page(self):
        return LoginPage(self.__driver)


class Navigate:
    def __init__(self, home_url, driver):
        self.__driver = driver

    @property
    def login_page(self):
        self.__driver.get(f'{self.home_url}/login.html')
        return LoginPage(self.__driver)

    @property
    def home_page(self):
        self.__driver.get(f'{self.home_url}/home.html')
        return LoginPage(self.__driver)
