import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.results_page import ResultsPage
# import random
from ddt import ddt, data, unpack
import csv


def get_data(file_name):
    open('/home/tester/PycharmProjects/BotlandProjectPOP/tests/products.csv')
    slowa = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    next(reader, 1)
    for row in reader:
        slowa.append(row)
        print(row)
    return slowa



@ddt
class ResultsTests(BaseTest):
    @data(*get_data("/home/tester/PycharmProjects/BotlandProjectPOP/tests/products.csv"))
    @unpack
    def testProductSearch(self, products):
        hp = HomePage(self.driver)
        rp = ResultsPage(self.driver)
        rp.search_product(products)

        #test z elementem losowości: losuje 1 wartość z listy poniżej i wyszukuje w sklepie:
        # rp.search_product(
        #     (random.choice(["Drony", "Java Script", "Java", "Roboty", "Raspberry"])))

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