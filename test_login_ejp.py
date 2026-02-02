import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLogin:

    def setup_method(self, method):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(width=1552, height=849)
        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)

    def teardown_method(self, method):
        self.driver.quit()

    #@pytest.mark.skip(reason="not needed")
    def test_login_valid_email_and_password(self):
        """Valid email and password input will notify 'Logging In...' text."""

        expected_text = "Logging In..."
        valid_email = "qaintern@ypo.com"
        valid_password = "123456"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="form_submit"]/div[3]/button')

        email_input.send_keys(valid_email)
        password_input.send_keys(valid_password)
        login_button.click()

        sleep(0.5)

        toast_container = self.driver.find_element(By.ID, "toast-container")
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_login_invalid_email_and_password(self):
        """Invalid email and password input will notify 'Invalid username or password' text"""

        expected_text = "Invalid username or password"
        invalid_email = "invalid@gmail.com"
        invalid_password = "invalid1234"
        email_input = self.driver.find_element(By.ID, 'email')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="form_submit"]/div[3]/button')

        email_input.send_keys(invalid_email)
        password_input.send_keys(invalid_password)
        login_button.click()

        sleep(0.5)

        toast_container = self.driver.find_element(By.ID, "toast-container")
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_login_valid_email_and_invalid_password(self):
        """Valid email and invalid password input will notify 'Invalid username or password' text"""

        expected_text = "Invalid username or password"
        valid_email = "qaintern@ypo.com"
        invalid_password = "invalid1234"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="form_submit"]/div[3]/button')

        email_input.send_keys(valid_email)
        password_input.send_keys(invalid_password)
        login_button.click()

        sleep(0.5)

        toast_container = self.driver.find_element(By.ID, "toast-container")
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_login_invalid_email_and_valid_password(self):
        """Invalid email and valid password input will notify 'Invalid username or password' text"""

        expected_text = "Invalid username or password"
        invalid_email = "invalid@ypo.com"
        valid_password = "123456"
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="form_submit"]/div[3]/button')

        email_input.send_keys(invalid_email)
        password_input.send_keys(valid_password)
        login_button.click()

        sleep(0.5)

        toast_container = self.driver.find_element(By.ID, "toast-container")
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_login_email_and_password_no_entry(self):
        """No entry will notify 'Please fill out this field.' text"""

        #expected_text = 'Please fill out this field.'
        valid_email = ""
        correct_password = ""
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="form_submit"]/div[3]/button')

        email_input.send_keys(valid_email)
        password_input.send_keys(correct_password)
        login_button.click()

        sleep(0.5)

        #toast_container = self.driver.find_element(By.ID, "toast-container")
        #actual_text = toast_container.text

        #assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_forgot_password_functionality(self):
        """Display: An email has been sent to the address on record. If you do not receive one shortly, please contact the Administrator."""

        expected_text = "An email has been sent to the address on record. If you do not receive one shortly, please contact the Administrator."
        forgot_password_button = self.driver.find_element(By.ID, 'forgot_password')
        forgot_password_button.click()
        self.driver.implicitly_wait(10)
        valid_email = "qaintern@ypo.com"
        email_input = self.driver.find_element(By.XPATH, "//input[@ng-model='forgot_password_email']")
        email_input.send_keys(valid_email)
        reset_password_button = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[4]/div/form/button")
        reset_password_button.click()
        sleep(10)

        toast_container = self.driver.find_element(By.XPATH, '//*[@id="forgot-password-modal"]/div[2]/div/div[1]/div[1]')
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_forgot_password_if_email_does_not_match(self):
        """Email does not match will notify 'Email do not exists!' """

        expected_text = "Email do not exists!"
        forgot_password_button = self.driver.find_element(By.ID, 'forgot_password')
        forgot_password_button.click()
        self.driver.implicitly_wait(10)
        valid_email = "invalid@ypo.com"
        email_input = self.driver.find_element(By.XPATH, "//input[@ng-model='forgot_password_email']")
        email_input.send_keys(valid_email)
        reset_password_button = self.driver.find_element(By.XPATH, "//*[@id='forgot-password-modal']/div[2]/div/div[1]/div[4]/div/form/button")
        reset_password_button.click()
        sleep(10)

        toast_container = self.driver.find_element(By.XPATH, '//*[@id="forgot-password-modal"]/div[2]/div/div[1]/div[2]')
        actual_text = toast_container.text

        assert actual_text == expected_text

        self.driver.close()