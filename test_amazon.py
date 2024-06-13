import logging
import time
import unittest
from base_test import BaseTest

EXPECTED_TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'


class TestAmazonTitle(BaseTest):
    def test_amazon_title(self):
        try:
            # Test method to navigate to Amazon and check the title
            self.driver.get("https://www.amazon.in")
            time.sleep(2)
            logging.info("Actual Title of amazon.in : %s", self.driver.title)
            logging.info("Expected Title of amazon.in : %s", EXPECTED_TITLE)
            logging.info("test_amazon_title %s", str(self.driver.title in EXPECTED_TITLE))
            self.assertIn(self.driver.title, EXPECTED_TITLE)
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")

    @unittest.skip("Skipping this test for now")
    def test_amazon_title_com(self):
        # Test method to navigate to Amazon and check the title
        self.driver.get("https://www.amazon.com")
        logging.info("Actual Title of amazon.com : %s", self.driver.title)
        logging.info("Expected Title of amazon.com : %s", EXPECTED_TITLE)
        logging.info("test_amazon_title_com %s", str(self.driver.title in EXPECTED_TITLE))
        self.assertIn(EXPECTED_TITLE, self.driver.title)

