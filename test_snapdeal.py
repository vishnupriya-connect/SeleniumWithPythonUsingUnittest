import logging
import unittest
from base_test import BaseTest

EXPECTED_TITLE = 'Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items'


class TestSnapDealTitle(BaseTest):
    def test_snap_deal_title(self):
        try:
            # Test method to navigate to Snapdeal and check the title
            self.driver.get("https://www.snapdeal.com")
            logging.info("Actual Title of snapdeal.com : %s", self.driver.title)
            logging.info("Expected Title of snapdeal.com : %s", EXPECTED_TITLE)
            logging.info("test_snap_deal_title %s", str(self.driver.title + "..." in EXPECTED_TITLE))
            self.assertIn(self.driver.title + "...", EXPECTED_TITLE)
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")

    @unittest.skipIf(True, "Conditionally skipping this test")
    def test_snap_deal_title_2(self):
        # Test method to navigate to Snapdeal and check the title
        self.driver.get("https://www.snapdeal.com")
        logging.info("Actual Title of snapdeal.com2 : %s", self.driver.title)
        logging.info("Expected Title of snapdeal.com2 : %s", EXPECTED_TITLE)
        logging.info("test_snap_deal_title_2 %s", str(self.driver.title in EXPECTED_TITLE))
        self.assertIn(self.driver.title, EXPECTED_TITLE)
