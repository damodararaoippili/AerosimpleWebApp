import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Set up the ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_successful_login(self):
        self.driver.get("https://us.staging.aerosimple.com/")
        # Add your test code here

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
