from time import sleep
import unittest
from pages.base_page import BasePage
from locators import HomePageLocators



class HomePage(BasePage):
    def testVerifySiteTitle(self):
        self.driver.get("https://botland.com.pl/pl")
        assert "Internetowy sklep elektroniczny - Botland - Sklep dla robotyków" in self.driver.title

    def testClickLogo(self):
        sleep(5)
        self.driver.find_element(*HomePageLocators.LOGO_EL).click()

    def testOverlapOne(self):
        self.driver.get("https://botland.com.pl/pl/content/53-dlaczego-warto-u-nas-kupowac")
        H = self.driver.find_element(*HomePageLocators.HEAD1_EL)
        text = H.text
        print(text)
        H2 = self.driver.find_element(*HomePageLocators.HEAD2_EL)
        text = H2.text
        print(text)
        H3 = self.driver.find_element(*HomePageLocators.HEAD3_EL)
        text = H3.text
        print(text)

    def testSearchingOverlapAndCategory(self):
        E = self.driver.find_element(*HomePageLocators.OVERLAPS_EL)
        if E.is_displayed():
            text = E.text
            print("Zakładki to:"+text)
        E2 = self.driver.find_element(*HomePageLocators.CATEGORIES_EL)
        if E2.is_displayed():
            text = E2.text
            print("Kategorie to:"+text)

    def testSearchPhoto(self):
        self.driver.get("https://botland.com.pl/pl/content/53-dlaczego-warto-u-nas-kupowac")
        P = self.driver.find_element(*HomePageLocators.PHOTO_EL)
        P.click()
        sleep(5)




if __name__ == '__main__':
    unittest.main(verbosity=2)
