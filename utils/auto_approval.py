from selenium.webdriver.common.by import By
from time import sleep

def dropdown(self):
    auto_approval = self.driver.find_element(By.XPATH, "//*[@aria-label='Select box select']")
    auto_approval.click()
    sleep(3)

    option_1 = self.driver.find_element(By.XPATH, "//*[@ng-if='$select.open']").is_displayed()
    if option_1 is True: is_option_displayed = True

    return is_option_displayed


def approve_option(self):
    approve_option = self.driver.find_element(By.XPATH, "//*[@ng-if='$select.open']")
    approve_option.click()
    sleep(3)

    auto_approval = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[6]/div/a/span[2]")
    actual_text = auto_approval.get_attribute('textContent')

    return actual_text


def apply_button(self):
    apply_button = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/button[1]")
    apply_button.click()
    sleep(3)

    confirmation_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
    is_displayed = confirmation_dialog.is_displayed()

    return is_displayed


def confirm_button(self):
    confirm_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]/div[7]/button[2]")
    confirm_button.click()
    sleep(1)
