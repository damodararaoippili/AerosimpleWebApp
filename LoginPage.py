import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LoginTestData import LoginTestData
class LoginPage(LoginTestData):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver_Email = (By.XPATH, "//input[@name='email']")
        self.driver_Next=(By.XPATH, "//button[@type='submit']")
        self.driver_Password = (By.XPATH, "//input[@type='password']")
        self.driver_login = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, username):
        email_field = self.driver.find_element(*self.driver_Email)
        email_field.send_keys(username)
    def Click_on_Next(self):
        Next=self.driver.find_element(*self.driver_Next)
        Next.click()

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver_Password))
        password_field.send_keys(password)
    def click_login_button(self):
        login_button = self.driver.find_element(*self.driver_login)
        login_button.click()

    def perform_login(self):
        dict_data = self.read_excel_data()
        self.navigate_to_url(dict_data.get('Environment_Url'))
        self.enter_email(dict_data.get('User_name'))
        self.Click_on_Next()
        self.enter_password(dict_data.get('Password'))
        self.click_login_button()
        time.sleep(5)