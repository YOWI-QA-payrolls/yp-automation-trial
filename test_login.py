import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestLogin:
    #hello
    def setup_method(self, method):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()

        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_valid_email_and_password(self):
        """ Check response when entering a valid Email and Password """
        ### Arrange
        expected_text = "Logging In..."
        valid_email = "qaintern@ypo.com"
        valid_passsword = "123456"

        #self.driver.find_element(By.LINK_TEXT, 'LOGIN').click()
        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//*[@id='form_submit']/div[3]/button")

        ### Act
        self.driver.implicitly_wait(10)
        email_input.send_keys(valid_email)
        password_input.send_keys(valid_passsword)
        login_button.click()

        sleep(0.5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='toast-container']/div/div[2]/div")
        
        actual_text = toast_container.text

        # sleep(1.5)
        # close_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button")
        # close_button.click()
        # sleep(5)

        ### Assert
        assert actual_text == expected_text

        self.driver.close()

    def test_login_invalid_email_and_valid_password(self):
        """ Check response when entering an invalid Email and valid Password """
        ### Arrange
        expected_text = "Invalid username or password"
        invalid_email = "example@email.com"
        valid_passsword = "123456"

        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//*[@id='form_submit']/div[3]/button")

        ### Act
        self.driver.implicitly_wait(10)
        email_input.send_keys(invalid_email)
        password_input.send_keys(valid_passsword)
        login_button.click()

        sleep(0.5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='toast-container']/div/div[2]/div")

        ### Assert
        actual_text = toast_container.text
        assert actual_text == expected_text

        self.driver.close()

    def test_login_valid_email_and_invalid_password(self):
        """ Check response when entering a valid Email and invalid Password """
        ### Arrange
        expected_text = "Invalid username or password"
        valid_email = "qaintern@ypo.com"
        invalid_passsword = "Sample_1234"

        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//*[@id='form_submit']/div[3]/button")

        ### Act
        self.driver.implicitly_wait(10)
        email_input.send_keys(valid_email)
        password_input.send_keys(invalid_passsword)
        login_button.click()

        sleep(0.5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='toast-container']/div/div[2]/div")

        ### Assert
        actual_text = toast_container.text
        assert actual_text == expected_text

        self.driver.close()

    def test_login_invalid_email_and_password(self):
        """ Check response when entering an invalid Email and Password """
        ### Arrange
        expected_text = "Invalid username or password"
        invalid_email = "example@email.com"
        invalid_passsword = "Sample_1234"

        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//*[@id='form_submit']/div[3]/button")

        ### Act
        self.driver.implicitly_wait(10)
        email_input.send_keys(invalid_email)
        password_input.send_keys(invalid_passsword)
        login_button.click()

        sleep(0.5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='toast-container']/div/div[2]/div")

        ### Assert
        actual_text = toast_container.text
        assert actual_text == expected_text

        self.driver.close()

    def test_login_no_email_and_no_password(self):
        """ Check response when email and password has no entry """
        ### Arrange
        expected_text = "Please fill out this field."
        no_email = " "
        no_passsword = " "

        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//*[@id='form_submit']/div[3]/button")

        ### Act
        self.driver.implicitly_wait(10)
        email_input.send_keys(no_email)
        password_input.send_keys(no_passsword)
        login_button.click()

        sleep(0.5)
        toast_container = email_input.get_attribute('validationMessage')

        ### Assert
        actual_text = toast_container
        assert actual_text == expected_text

        self.driver.close()

    def test_forgot_password_valid_email(self):
        """ Check response when entering a valid email address """
        ### Arrange
        expected_text = "An email has been sent to the address on record. If you do not receive one shortly, please contact the Administrator."
        valid_email = "qaintern@ypo.com"

        forgot_password_button = self.driver.find_element(By.ID, 'forgot_password')
        forgot_password_button.click()

        self.driver.implicitly_wait(10)
        email_input = self.driver.find_element(By.XPATH, "//input[@ng-model='forgot_password_email']")
        email_input.send_keys(valid_email)
        
        reset_password_button = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[4]/div/form/button")
        reset_password_button.click()

        sleep(5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[1]")

        ### Assert
        actual_text = toast_container.text
        assert actual_text == expected_text

        self.driver.close()

    def test_forgot_password_invalid_email(self):
        """ Check response when entering an invalid email address """
        ### Arrange
        expected_text = "Email do not exists!"
        invalid_email = "sample@email.com"

        forgot_password_button = self.driver.find_element(By.ID, 'forgot_password')
        forgot_password_button.click()

        self.driver.implicitly_wait(10)
        email_input = self.driver.find_element(By.XPATH, "//input[@ng-model='forgot_password_email']")
        email_input.send_keys(invalid_email)
        
        reset_password_button = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[4]/div/form/button")
        reset_password_button.click()

        sleep(5)
        toast_container = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[2]")

        ### Assert
        actual_text = toast_container.text
        assert actual_text == expected_text

        self.driver.close()

    def test_forgot_password_no_email_entry(self):
        """ Check response when email has no entry """
        ### Arrange
        expected_text = "Please fill out this field."
        no_email = ""

        forgot_password_button = self.driver.find_element(By.ID, 'forgot_password')
        forgot_password_button.click()

        self.driver.implicitly_wait(10)
        email_input = self.driver.find_element(By.XPATH, "//input[@ng-model='forgot_password_email']")
        email_input.send_keys(no_email)
        
        reset_password_button = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[4]/div/form/button")
        reset_password_button.click()

        sleep(5)
        toast_container = email_input.get_attribute('validationMessage')

        ### Assert
        actual_text = toast_container
        assert actual_text == expected_text

        self.driver.close()

    def test_privacy_notice(self):
        """ Check response when clicking 'Privacy Notice' button """
        privacy_notice_button = self.driver.find_element(By.ID, 'privacy')
        privacy_notice_button.click()

        self.driver.implicitly_wait(10)
        privacy_notice_file = self.driver.find_element(By.XPATH, "//*[@id='myFrame']")

        sleep(3)
        toast_container = privacy_notice_file.is_displayed()

        ### Assert
        assert toast_container == True

        self.driver.close()
