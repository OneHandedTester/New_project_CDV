import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.results_page import ResultsPage
import random

class ResultsTests(BaseTest):
    def testProductSearch(self):
        hp = HomePage(self.driver)
        rp = ResultsPage(self.driver)
        rp.close_cookies()
        rp.search_product(
            (random.choice(["Arduino", "Raspberry", "Roboty", "Drony", "JavaScript", "Groty", "Python", "Java"])))
        rp.search_product2()
        rp.search_product_results()
        rp.submit_results()
        rp.product_sorting()
        rp.choose_products()
        rp.order_click()
        rp.verify_site_order()
        rp.sum_of_products()
        rp.clear_basket()



if __name__ == '__main__':
    unittest.main(verbosity=2)