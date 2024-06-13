import unittest
from test_snapdeal import TestSnapDealTitle
from test_amazon import TestAmazonTitle

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the TestSnapDealTitle and TestAmazonTitle test cases to the suite
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSnapDealTitle))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAmazonTitle))

    # Run the test suite
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
