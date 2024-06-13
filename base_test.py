from datetime import datetime
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

# Create a 'logs' folder if it doesn't exist
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Generate a timestamp for the log file
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Specify the path for your log file with timestamp
log_file_path = os.path.join(log_folder, f'test_logs_{timestamp}.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Class-level setup code
        logging.info("Setting up the class with DB connection code")

    @classmethod
    def tearDownClass(cls):
        # Class-level teardown code
        logging.info("Tearing down the class with DB connection closure")

    def setUp(self):
        # Setup method to initialize the browser before each test
        logging.info("Setting up the test case - browser open")
        serv_obj = Service(r'C:\Users\rihaa\Documents\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

    def tearDown(self):
        # Teardown method to close the browser after each test
        logging.info("Tearing down the test case - browser close")
        self.driver.quit()
