import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from utilibox import Toolbox




class Testlogin(Toolbox):
    load_dotenv(dotenv_path=r'C:\Users\dhana\Downloads\New folder (3) - Copy\.env')
    secret_username = os.getenv('USERNAME1')
    secret_password = os.getenv('PASSWORD1')
    secret_username1 = os.getenv('INVALID_USERNAME')
    secret_password1 = os.getenv('INVALID_PASSWORD')


    def test_url(self):
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url


    def test_login_valid_cred(self):
        print(f"Username: {self.secret_username}, Password: {self.secret_password}")
        self.login(self.secret_username, self.secret_password)
        # rest of the code
        time.sleep(10)
        self.driver.back()
        assert self.driver.find_elements(By.CSS_SELECTOR,'.dropdown-toggle')[1].text == self.secret_username
        self.driver.find_elements(By.CSS_SELECTOR,'.dropdown-toggle')[1].click()
        self.driver.find_element(By.CSS_SELECTOR,'#logout_link').click()

    def test_login_invalid_cred(self):
        self.login(self.secret_username1, self.secret_password1)

        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-error").text == "Login and/or password are wrong."
        time.sleep(2)


  