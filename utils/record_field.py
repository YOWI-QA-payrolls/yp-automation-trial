from selenium.webdriver.common.by import By
from time import sleep


def checkbox(self):
    select_checkbox = self.driver.find_element(By.XPATH, '//*[@id="auto_approval"]')
    select_checkbox.click()
    sleep(3)
    is_checkbox_selected = select_checkbox.is_selected()

    return is_checkbox_selected


def record_row(self, record_xpath):
    select_record_row = self.driver.find_element(By.XPATH, record_xpath)
    select_record_row.click()
    sleep(3)

    approval_request_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    dialog_displayed = approval_request_dialog.is_displayed()

    return dialog_displayed


def click_calendar_icon(self):
    try:
        calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('date')\"]")
        calendar_icon.click()
        is_calendar_icon_clicked = True
    except Exception as error:
        print(error.__class__)
        is_calendar_icon_clicked = False

    return is_calendar_icon_clicked


def edit_date(self, new_date):
    date_input_box = self.driver.find_element(By.XPATH, "//*[@is-open=\"main.uibdates['date']\"]")
    date_input_box.clear()
    date_input_box.send_keys(new_date)
    actual_data = date_input_box.get_attribute('value')

    return actual_data


def change_number_of_hours(self, input_hours):
    input_box = self.driver.find_element(By.XPATH,
                                         "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div/div[1]/input")
    input_box.send_keys(input_hours)
    actual_data = input_box.get_attribute('value')

    return actual_data


def reviewed_record(self):
    click_reviewed_record = self.driver.find_element(By.XPATH, '//*[@id="reviewed"]')
    click_reviewed_record.click()
    is_radio_button_selected = click_reviewed_record.is_selected()

    return is_radio_button_selected

def recommend_record(self):
    click_reviewed_record = self.driver.find_element(By.XPATH, '//*[@id="recommended"]')
    click_reviewed_record.click()
    is_radio_button_selected = click_reviewed_record.is_selected()

    return is_radio_button_selected
    
def submit_button(self):
    click_submit_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[2]")
    click_submit_button.click()
    sleep(3)


def confirm_button(self):
    dialog_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]")
    dialog_box_popped_up = dialog_box.is_displayed()

    confirm_button_yes = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[6]/div[7]/button[2]')
    confirm_button_yes.click()
    sleep(1)

    return dialog_box_popped_up


def close_button(self):
    click_close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
    click_close_button.click()
    sleep(3)

    approval_request_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    dialog_closed = not approval_request_dialog.is_displayed()

    return dialog_closed

def not_endorse(self):
    click_not_endorse_record = self.driver.find_element(By.XPATH, '//*[@id="not_reviewed"]')
    click_not_endorse_record.click()
    is_radio_button_selected = click_not_endorse_record.is_selected()
    return is_radio_button_selected