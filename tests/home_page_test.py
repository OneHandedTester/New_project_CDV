import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage


class HomeTest(BaseTest):
    def testHomePageElements(self):
        hp = HomePage(self.driver)
        hp.testVerifySiteTitle()
        hp.testClickLogo()
        hp.testOverlapOne()
        hp.testSearchingOverlapAndCategory()
        hp.testSearchPhoto()


if __name__ == '__main__':
    unittest.main(verbosity=2)