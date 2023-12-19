from selenium.webdriver.common.by import By


class Toolbox:

    def login(self,username,password): 
        self.driver.find_element(By.CSS_SELECTOR, '#signin_button').click() 
        self.driver.find_element(By.CSS_SELECTOR, "#user_login").send_keys(username) 
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(password) 
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click() 
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="Sign in"]').click() 