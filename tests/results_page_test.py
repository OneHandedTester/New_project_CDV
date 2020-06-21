import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.results_page import ResultsPage
import random

class ResultsTests(BaseTest):
    def testProductSearch(self):
        hp = HomePage(self.driver)
        rp = ResultsPage(self.driver)
        rp.search_product(
            (random.choice(["Drony"])))
        rp.search_product2()
        rp.search_product_results()
        rp.submit_results()
        rp.product_sorting()
        rp.choose_products()
        rp.close_cookies()
        rp.order_click()
        rp.verify_site_order()

        rp.sum_of_products()
        suma = rp.sum_of_products()
        zam2 = rp.client_order()
        self.assertEqual(suma, zam2, "Ceny nie są zgodne.")
        rp.clear_basket()



if __name__ == '__main__':
    unittest.main(verbosity=2)