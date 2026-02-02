from selenium.webdriver.common.by import By
from time import sleep


def dropdown(self):
    auto_approval_dropdown = self.driver.find_element(By.XPATH, "//*[@aria-label='Select box select']")
    auto_approval_dropdown.click()
    sleep(3)

    option_1 = self.driver.find_element(By.XPATH, "//*[@ng-if='$select.open']").is_displayed()
    if option_1 is True: is_option_displayed = True

    return is_option_displayed


def review_option(self):
    review_option_click = self.driver.find_element(By.XPATH, "//*[@ng-if='$select.open']")
    review_option_click.click()
    sleep(3)

    auto_approval = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[6]/div/a/span[2]")
    actual_text = auto_approval.get_attribute('textContent')

    return actual_text


def review_button(self):
    try:
        auto_approval_review_button = self.driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-0-"]')
        auto_approval_review_button.click()
        sleep(3)
        is_review_button_clicked = True
    except Exception as error:
        print(error.__class__)
        is_review_button_clicked = False

    return is_review_button_clicked
