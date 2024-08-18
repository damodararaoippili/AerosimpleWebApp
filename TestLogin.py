import time
import unittest
from selenium import webdriver
from LoginPage import LoginPage
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.perform_login()
        time.sleep(20)
        # Add assertions to verify successful login, e.g., check for a welcome message or redirect URL

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()