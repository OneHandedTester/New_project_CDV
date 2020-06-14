import unittest
from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    def fill_email(self, email):
        self.driver.get("https://botland.com.pl/pl/logowanie")
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_button(self):
        self.driver.find_element(*LoginPageLocators.LOG_ON_TO_USER_BTN).click()

    def assert_log(self):
        self.driver.find_element(*LoginPageLocators.MY_ACCOUNT_LINK).click()
        url2 = self.driver.current_url
        print(url2)

    def find_errors(self):
        el = self.driver.find_element(*LoginPageLocators.ERROR_COM)
        if el.is_displayed():
            print("Logowanie zakończone niepowodzeniem. Błędne dane.")

if __name__ == '__main__':
    unittest.main(verbosity=2)