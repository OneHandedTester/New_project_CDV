import unittest
from time import sleep
from pages.base_page import BasePage
from locators import RegisterPageLocators

class RegisterPage(BasePage):
    def close_cookies(self):
        cookies = self.driver.find_element(*RegisterPageLocators.COOKIES_BTN)
        if cookies.is_displayed():
            self.driver.find_element(*RegisterPageLocators.COOKIES_BTN).click()
        else:
            ""

    def click_register(self):
        self.driver.find_element(*RegisterPageLocators.LOG_AND_REGISTER_BTN).click()

    def fill_input(self, email):
        self.driver.find_element(*RegisterPageLocators.NEW_EMAIL_INPUT).send_keys(email)
        print("1. "+email)

    def click_submit(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BTN).click()

    def error_register(self):
        el = self.driver.find_element(*RegisterPageLocators.ERROR_COM)
        el2 = self.driver.find_element(*RegisterPageLocators.ERROR2_COM)
        assert el == el2

    def clear_input(self):
        self.driver.find_element(*RegisterPageLocators.NEW_EMAIL_INPUT).clear()

    def close_popup(self):
        popup = self.driver.find_element(*RegisterPageLocators.BAD_POPUP_BTN)
        if popup.is_displayed():
            popup.click()

    def fill_name(self, name):
        self.driver.find_element(*RegisterPageLocators.FIRSTNAME_INPUT).send_keys(name)
        print("2. "+name)

    def fill_surname(self, surname):
        self.driver.find_element(*RegisterPageLocators.LASTNAME_INPUT).send_keys(surname)
        sleep(20)
        print("3. "+surname)

    def check_email(self):
        email2 = self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        print("4. Email zwrócony to: ")
        print(email2.get_attribute("value"))

    def fill_password(self, password):
        self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        print("5. "+password)

    def fill_company(self, company):
        self.driver.find_element(*RegisterPageLocators.COMPANY_NAME_INPUT).send_keys(company)
        print("6. "+company)

    def fill_nip(self, nip):
        self.driver.find_element(*RegisterPageLocators.NIP_INPUT).send_keys(nip)
        print("7. "+nip)

    def fill_address1(self, address1):
        self.driver.find_element(*RegisterPageLocators.ADDRESS1_INPUT).send_keys(address1)
        print("8. "+address1)

    def fill_adress2(self, address2):
        self.driver.find_element(*RegisterPageLocators.ADDRESS2_INPUT).send_keys(address2)
        print("9. "+address2)

    def fill_city(self, city):
        self.driver.find_element(*RegisterPageLocators.CITY_INPUT).send_keys(city)
        print("10. "+city)

    def check_country(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")
        country = self.driver.find_element(*RegisterPageLocators.COUNTRY_ID_SELECTLIST)
        print("Numer kraju to: ")
        print(country.get_attribute("value"))

    def fill_code(self, code):
        self.driver.find_element(*RegisterPageLocators.POSTCODE_INPUT).send_keys(code)
        code2 = str(code)
        print("11. "+code2)

    def fill_info (self, info):
        self.driver.find_element(*RegisterPageLocators.OTHERS_INFORMATIONS_INPUT).send_keys(info)
        print("12. "+info)

    def fill_number (self, number):
        self.driver.find_element(*RegisterPageLocators.PHONE_NUMBER_INPUT).send_keys(number)
        sleep(20)
        print("13. "+number)

    def click_checkbox (self):
        checkbox = self.driver.find_element(*RegisterPageLocators.NEWSLETTER_CHECKBOX).click()
        if checkbox != 0:
            print("Zaznaczony newsletter")
        else:
            print("Błąd.")

    def scroll_down ( self ):
        self.driver.execute_script("window.scrollTo(0, 1000);")



if __name__ == '__main__':
    unittest.main(verbosity=2)



