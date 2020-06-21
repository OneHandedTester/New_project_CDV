import unittest


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page ( self ):
        return

    if __name__ == '__main__':
        unittest.main(verbosity=2)
