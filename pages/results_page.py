import unittest
from time import sleep
from pages.base_page import BasePage
from locators import ResultsPageLocators
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

class ResultsPage(BasePage):
    def close_cookies(self):
        cookies = self.driver.find_element(*ResultsPageLocators.COOKIES_BTN)
        if cookies.is_displayed():
            self.driver.find_element(*ResultsPageLocators.COOKIES_BTN).click()
        else:
            ""

    @data(*get_data("/home/tester/PycharmProjects/BotlandProjectPOP/tests/products.csv"))
    @unpack
    def search_product(self, products):
        searcher = self.driver.find_element(*ResultsPageLocators.SEARCHER_INPUT)
        searcher.send_keys(products)

    def search_product2(self):
        el = self.driver.find_element_by_css_selector('#search_query_top')
        print(el)

    def search_product_results(self):
        sleep(3)
        search_value = self.driver.find_element_by_xpath('//*[@id="index"]/div[3]/ul')
        text = search_value.text
        print("Wartości zwrócone to:"+text)


    def submit_results(self):
        self.driver.find_element(*ResultsPageLocators.SEARCHER_INPUT).submit()

    def product_sorting(self):
        self.driver.find_element(*ResultsPageLocators.SELECT_LIST_EL).click()

    def choose_products(self):
        self.driver.find_element(*ResultsPageLocators.RANDOM_PRODUCT1_EL).click()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.driver.find_element(*ResultsPageLocators.RANDOM_PRODUCT2_EL).click()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.driver.find_element(*ResultsPageLocators.RANDOM_PRODUCT3_EL).click()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.driver.find_element(*ResultsPageLocators.RANDOM_PRODUCT4_EL).click()
        sleep(5)

    def order_click(self):
        self.driver.find_element(*ResultsPageLocators.ORDER_BTN).click()
        sleep(3)

    def verify_site_order(self):
        print(self.driver.current_url)
        assert "Zamówienie | Botland - Sklep dla robotyków" in self.driver.title
        lista = self.driver.find_elements(*ResultsPageLocators.ORDER_PRODUCT_LIST)
        print("Liczba produktów w koszyku klienta to:")
        x = print(len(lista))
        if x == 0:
            print("Test failed.")
        else:
            print("Test passed.")


    def sum_of_products(self):
        price = self.driver.find_element(*ResultsPageLocators.SUM_BRUTTO_EL)
        text = price.text
        x = text.replace(" zł", "")
        x = x.replace(",", ".")
        x = x.replace(" ", "")
        price1 = float(x)
        print("Cena produktów :", price1)


        transport = self.driver.find_element(*ResultsPageLocators.SUM_SHIPPING_EL)
        text = transport.text
        if text == "Darmowa Dostawa":
            price2 = 0.0
        elif text == "":
            price2 = 0.0
        else:
            x = text.replace(" zł", "")
            x = x.replace(",", ".")
            price2 = float(x)

        print("Cena dostawy: ", price2)


        suma = price1 + price2
        print("Wychodzi razem: ", suma)

    def client_order(self):
        suma_all = self.driver.find_element(*ResultsPageLocators.SUM_TOTAL_PRICE)
        text = suma_all.text
        x = text.replace(" zł", "")
        x = x.replace(",", ".")
        x = x.replace(" ", "")
        zamowienie = float(x)
        print("Suma zamówienia - całość (kwota do porównania): ", zamowienie)


    def clear_basket(self):
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_BTN)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_BTN).click()
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_ACCEPT_BTN).click()
        lista = self.driver.find_elements(*ResultsPageLocators.ORDER_PRODUCT_LIST)
        print("Liczba produktów w koszyku klienta (po usunięciu) to:")
        x = print(len(lista))
        if x != 0:
            print("Usunięte, ok.")
        else:
            print("Błąd usuwania")


if __name__ == '__main__':
    unittest.main(verbosity=2)
