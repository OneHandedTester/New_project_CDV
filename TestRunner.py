from unittest import TestLoader, TestSuite, TextTestRunner
from tests.base_test import BaseTest
from tests.home_page_test import HomeTest
from tests.login_page_test import LoginTest
from tests.register_page_test import RegisterTest
from tests.results_page_test import ResultsTests

import testtools as testtools

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(BaseTest),
        loader.loadTestsFromTestCase(HomeTest),
        loader.loadTestsFromTestCase(LoginTest),
        loader.loadTestsFromTestCase(RegisterTest),
        loader.loadTestsFromTestCase(ResultsTests)))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
concurrent_suite.run(testtools.StreamResult())