from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def navigate_to_portal_url(self,url):
        self.driver.get(url)

    @classmethod
    def wait_for_element_to_be_clickable(cls, driver, locator, timeout=20):
        from LoginTestData import LoginTestData  # Import inside method
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator))
