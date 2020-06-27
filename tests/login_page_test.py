import unittest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.home_page import HomePage


class LoginTest(BaseTest):
    def testLogOnToUserCorrect( self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        lp.fill_email("k.moszczynska13@wp.pl")
        lp.fill_password("Kn3SB7ca")
        lp.click_button()
        lp.assert_log()


    def testLogOnToUserIncorrect (self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        lp.fill_email("teścik mały")
        lp.fill_password("t")
        lp.click_button()
        lp.find_errors()




if __name__ == '__main__':
    unittest.main(verbosity=2)