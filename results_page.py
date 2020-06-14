import unittest
from time import sleep
from pages.base_page import BasePage
from locators import ResultsPageLocators



class ResultsPage(BasePage):
    def close_cookies(self):
        cookies = self.driver.find_element(*ResultsPageLocators.COOKIES_BTN)
        if cookies.is_displayed():
            self.driver.find_element(*ResultsPageLocators.COOKIES_BTN).click()

    def search_product(self, el):
        self.driver.find_element(*ResultsPageLocators.SEARCHER_INPUT).send_keys(el)

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
        print(len(lista))

    def sum_of_products(self):
        SUM = self.driver.find_element_by_xpath('//*[@id="total_product"]')
        text = SUM.text
        A = print("Cena brutto: "+text)
        print("+")
        SUM2= self.driver.find_element_by_xpath('//*[@id="total_shipping"]')
        text = SUM2.text
        B = print("Koszty przesyłki: "+text)
        print("=")
        ALL = self.driver.find_element_by_xpath('//*[@id="total_price"]')
        text = ALL.text
        C = print("Cena całkowita: "+text)



    def clear_basket(self):
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_BTN)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_BTN).click()
        self.driver.find_element(*ResultsPageLocators.CLEAR_BASKET_ACCEPT_BTN).click()
        lista = self.driver.find_elements(*ResultsPageLocators.ORDER_PRODUCT_LIST)
        print("Liczba produktów w koszyku klienta to:")
        print(len(lista))



if __name__ == '__main__':
    unittest.main(verbosity=2)