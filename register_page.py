import unittest
from pages.base_page import BasePage
from locators import RegisterPageLocators

class RegisterPage(BasePage):
    def close_cookies(self):
        cookies = self.driver.find_element(*RegisterPageLocators.COOKIES_BTN)
        if cookies.is_displayed():
            self.driver.find_element(*RegisterPageLocators.COOKIES_BTN).click()

    def click_register(self):
        self.driver.find_element(*RegisterPageLocators.LOG_AND_REGISTER_BTN).click()

    def fill_input(self, email):
        self.driver.find_element(*RegisterPageLocators.NEW_EMAIL_INPUT).send_keys(email)


    def click_submit(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BTN).click()

    def error_register(self):
        el = self.driver.find_element(*RegisterPageLocators.ERROR_COM)
        el2 = self.driver.find_element(*RegisterPageLocators.ERROR2_COM)
        assert el == el2

    def clear_input(self):
        self.driver.find_element(*RegisterPageLocators.NEW_EMAIL_INPUT).clear()

    # def close_popup(self):
    #     popup = self.driver.find_element(*RegisterPageLocators.BAD_POPUP_BTN)
    #     if popup.is_displayed:
    #         self.driver.find_element(*RegisterPageLocators.BAD_POPUP_BTN).click()

    def fill_name(self, name):
        self.driver.find_element(*RegisterPageLocators.FIRSTNAME_INPUT).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*RegisterPageLocators.LASTNAME_INPUT).send_keys(surname)

    def assert_email(self):
        self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT)

    def fill_password(self, password):
        self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    def fill_company(self, company):
        self.driver.find_element(*RegisterPageLocators.COMPANY_NAME_INPUT).send_keys(company)

    def fill_nip(self, nip):
        self.driver.find_element(*RegisterPageLocators.NIP_INPUT).send_keys(nip)

    def fill_address1(self, address1):
        self.driver.find_element(*RegisterPageLocators.ADDRESS1_INPUT).send_keys(address1)

    def fill_adress2(self, address2):
        self.driver.find_element(*RegisterPageLocators.ADDRESS2_INPUT).send_keys(address2)

    def fill_city(self, city):
        self.driver.find_element(*RegisterPageLocators.CITY_INPUT).send_keys(city)

    def fill_code(self, code):
        self.driver.find_element(*RegisterPageLocators.POSTCODE_INPUT).send_keys(code)

    def fill_info(self, info):
        self.driver.find_element(*RegisterPageLocators.OTHERS_INFORMATIONS_INPUT).send_keys(info)

    def fill_number(self, number):
        self.driver.find_element(*RegisterPageLocators.PHONE_NUMBER_INPUT).send_keys(number)

    def click_checkbox(self):
        self.driver.find_element(*RegisterPageLocators.NEWSLETTER_CHECKBOX).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")




if __name__ == '__main__':
    unittest.main(verbosity=2)