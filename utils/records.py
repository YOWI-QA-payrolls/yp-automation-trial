from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def select_all(self):
    select_all_checkbox = self.driver.find_element(By.ID, 'auto_approval')
    select_all_checkbox.click()
    sleep(3)
    is_checkbox_selected = select_all_checkbox.is_selected()

    return is_checkbox_selected

def click_record_row(self, record_xpath):
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

def edit_date(self, input_date_xpath):
    selected_date = self.driver.find_element(By.XPATH, input_date_xpath)
    selected_date.click()

    date_input_box = self.driver.find_element(By.XPATH , "//*[@is-open=\"main.uibdates['date']\"]")
    actual_data = date_input_box.get_attribute('value')
    
    return actual_data

def change_number_of_hours(self, input_hours):
    input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div/div[1]/input")
    input_box.send_keys(input_hours)
    actual_data = input_box.get_attribute('value')

    return actual_data

def approve_record(self):
    approve_record = self.driver.find_element(By.ID, 'approved_applied')
    approve_record.click()
    is_radio_button_selected = approve_record.is_selected()

    return is_radio_button_selected

def submit_button(self):
    submit_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[2]")
    submit_button.click()
    sleep(3)

def confirm_yes_button(self):
    dialog_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]")
    dialog_box_popped_up = dialog_box.is_displayed()

    yes_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/div[7]/button[2]")
    yes_button.click()
    sleep(1)

    return dialog_box_popped_up

def close_button(self):
    close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
    close_button.click()
    sleep(3)

    approval_request_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    dialog_closed = not approval_request_dialog.is_displayed()

    return dialog_closed

def per_page_dropdown(self):
    records_per_page_dropdown = self.driver.find_element(By.XPATH, "//*[@aria-label='Select box activate']")
    records_per_page_dropdown.click()
    sleep(3)

    option_1 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[3]").is_displayed()
    option_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[4]").is_displayed()
    option_3 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[5]").is_displayed()

    if option_1 and option_2 and option_3 is True : is_option_displayed = True

    return is_option_displayed
    
def per_page_option_5(self):    
    try:
        option_five = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[3]/a")
        option_five.click()
        option_clicked = True
        sleep(3)
    except Exception:
        print(Exception)
        option_clicked = False

    records_per_page_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[7]/div/div/span/span[2]")
    actual_text = records_per_page_dropdown.get_attribute('textContent')

    return [option_clicked, actual_text]

def ob_change_number_of_day(self, no_of_ob_days):
    input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/span/div/div[1]/span/input")
    input_box.send_keys(no_of_ob_days)

    actual_data = input_box.get_attribute('value')
    return actual_data

def ob_click_calendar_icon(self):
    try:
        calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(key+1)\"]")
        calendar_icon.click()
        is_calendar_icon_clicked = True
    except Exception as error:
        print(error.__class__)
        is_calendar_icon_clicked = False

    return is_calendar_icon_clicked

def ob_edit_date(self, input_date_xpath):
    selected_date = self.driver.find_element(By.XPATH, input_date_xpath)
    selected_date.click()

    date_input_box = self.driver.find_element(By.XPATH , "//*[@is-open=\"main.uibdates[key+1]\"]")
    actual_data = date_input_box.get_attribute('value')

    return actual_data

def ob_edit_time_from(self, input_time_from):             
    hours_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/input")
    hours_input_box.clear()
    hours_input_box.send_keys(input_time_from[0])

    minutes_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/input")
    minutes_input_box.clear()
    minutes_input_box.send_keys(input_time_from[1])
    sleep(3)

    actual_hours = hours_input_box.get_attribute('value')
    actual_minutes = minutes_input_box.get_attribute('value')

    return [actual_hours, actual_minutes]

def ob_edit_time_to(self, input_time_to):
    hours_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input")
    hours_input_box.clear()
    hours_input_box.send_keys(input_time_to[0])

    minutes_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[3]/div/table/tbody/tr[2]/td[3]/input")
    minutes_input_box.clear()
    minutes_input_box.send_keys(input_time_to[1])
    sleep(3)

    actual_hours = hours_input_box.get_attribute('value')
    actual_minutes = minutes_input_box.get_attribute('value')

    return [actual_hours, actual_minutes]

def leave_edit_time_from(self, input_time_from):             
    hours_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[1]/input")
    hours_input_box.clear()
    hours_input_box.send_keys(input_time_from[0])

    minutes_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[3]/input")
    minutes_input_box.clear()
    minutes_input_box.send_keys(input_time_from[1])
    sleep(3)

    actual_hours = hours_input_box.get_attribute('value')
    actual_minutes = minutes_input_box.get_attribute('value')

    return [actual_hours, actual_minutes]

def leave_edit_time_to(self, input_time_to):
    hours_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[1]/input")
    hours_input_box.clear()
    hours_input_box.send_keys(input_time_to[0])

    minutes_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[3]/input")
    minutes_input_box.clear()
    minutes_input_box.send_keys(input_time_to[1])
    sleep(3)

    actual_hours = hours_input_box.get_attribute('value')
    actual_minutes = minutes_input_box.get_attribute('value')

    return [actual_hours, actual_minutes]