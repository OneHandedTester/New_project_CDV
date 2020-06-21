import unittest
from time import sleep
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from faker import Faker

faker = Faker()



class RegisterTest(BaseTest):
    # def testInvalidEmail(self):
    #     hp = HomePage(self.driver)
    #     rp = RegisterPage(self.driver)
    #     rp.click_register()
    #     rp.fill_input("test")
    #     rp.click_submit()
    #     rp.clear_input()
    #     rp.fill_input("test@test")
    #     rp.click_submit()
    #     rp.clear_input()
    #     rp.fill_input("1234567890000029595956565558TEST")
    #     rp.click_submit()


    def testValidEmail(self):
        hp = HomePage(self.driver)
        rp = RegisterPage(self.driver)
        rp.click_register()
        rp.fill_input(faker.safe_email())
        sleep(1)
        rp.click_submit()
        rp.fill_name(faker.first_name())
        sleep(1)
        rp.fill_surname(faker.last_name())
        rp.check_email()
        rp.close_cookies()
        sleep(1)
        rp.close_popup()
        rp.click_checkbox()
        rp.scroll_down()
        sleep(1)
        rp.fill_password("52565865wertyhgfdfv!@#$")
        sleep(1)
        rp.fill_company(faker.word())
        sleep(1)
        rp.fill_address1(faker.address())
        sleep(1)
        rp.fill_nip("3944383857")
        sleep(1)
        rp.fill_adress2(faker.address())
        rp.scroll_down()
        rp.fill_city(faker.word())
        rp.check_country()
        rp.fill_code(faker.random_int())
        sleep(1)
        rp.fill_info(faker.word())
        sleep(1)
        rp.fill_number(faker.phone_number())



if __name__ == '__main__':
    unittest.main(verbosity=2)
