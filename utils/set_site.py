from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class admin_set_site():

    def login(self):
        
        admin_email = "yahshua.systechqa@gmail.com"
        admin_password = "Qa_123456"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        self.driver.implicitly_wait(20)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/form/div[3]/button")
        email_input.send_keys(admin_email)
        password_input.send_keys(admin_password)
        password_input.send_keys(Keys.ENTER)
        #login_button.click()

        time.sleep(7)
        self.driver.execute_script("$('.btn-white').click();")
        time.sleep(5)

class  reviewer_set_site():
        
    def login(self):

        valid_email = "qaintern@ypo.com"
        valid_password = "123456"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        self.driver.implicitly_wait(20)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/form/div[3]/button")
        email_input.send_keys(valid_email)
        password_input.send_keys(valid_password)
        # password_input.send_keys(Keys.ENTER)
        login_button.click()

        time.sleep(10)
        # self.driver.execute_script("$('.btn-white').click();")
        # time.sleep(5)

class recommender_set_site():
    
    def login(self):

        valid_email = "recommend@ypo.com"
        valid_password = "Qa_12345"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        self.driver.implicitly_wait(20)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/form/div[3]/button")
        email_input.send_keys(valid_email)
        password_input.send_keys(valid_password)
        # password_input.send_keys(Keys.ENTER)
        login_button.click()

        time.sleep(10)
        # self.driver.execute_script("$('.btn-white').click();")
        # time.sleep(5)


class approver_set_site():

    def login(self):
        valid_email = "qaapprover@ypo.com"
        valid_password = "123456"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        self.driver.implicitly_wait(20)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/form/div[3]/button")
        email_input.send_keys(valid_email)
        password_input.send_keys(valid_password)
        password_input.send_keys(Keys.ENTER)
        #login_button.click()

        time.sleep(7)
        self.driver.execute_script("$('.btn-white').click();")
        time.sleep(5)
        
class LogIn():
    
    def login(self):
        valid_email = "admin@ypo.com"
        valid_password = "systech3223"
        email_input = self.driver.find_element_by_id("email")
        password_input = self.driver.find_element_by_id("password")
        self.driver.implicitly_wait(20)
        login_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/form/div[3]/button")
        email_input.send_keys(valid_email)
        password_input.send_keys(valid_password)
        login_button.click()

        time.sleep(5)
        notification = self.driver.find_element_by_xpath("//*[@id='page-top']/div[1]/div/div/div/div[3]/div/div/button")
        notification.click()
        #self.driver.execute_script("$('.btn-white').click();")
        time.sleep(3)
        