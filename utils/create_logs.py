from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class CreateLogs:

    def click_create_button(self):
        create_button = self.driver.find_element(By.XPATH, "//*[@class='btn btn-danger']")
        create_button.click()
        sleep(2)

    def input_date(self, date):
        date_field = self.driver.find_element(By.XPATH, "//*[@name='date_from']")
        date_field.clear()
        date_field.send_keys(date)

        date_field_data = date_field.get_attribute('value') 

        return date_field_data

    def input_employee(self, employee):
        employee_dropdown = self.driver.find_element(By.XPATH, "//*[@placeholder='Select...']")
        employee_dropdown.click()
        employee_field = self.driver.find_element(By.XPATH, "//*[@aria-activedescendant='ui-select-choices-row-2-0']")
        employee_field.send_keys(employee)
        field_data = employee_field.get_attribute('value')
        employee_field.send_keys(Keys.RETURN)

        return field_data
    
    def input_reason(self, reason):
        reason_field = self.driver.find_element(By.XPATH, "//*[@name='reason']")
        reason_field.clear()
        reason_field.send_keys(reason)

        return reason_field.get_attribute('value')

    def input_log_type(self, log_type):
        log_type_dropdown = self.driver.find_element(By.XPATH, "//*[@ng-model='timesheet.log_type']")
        log_type_dropdown.click()
        log_type_field = self.driver.find_element(By.XPATH, "//*[@aria-activedescendant='ui-select-choices-row-3-0']")
        log_type_field.send_keys(log_type)
        log_type_data = log_type_field.get_attribute('value')
        log_type_field.send_keys(Keys.RETURN)

        return log_type_data

    def input_time_hour(self, hour):
        time_hh = self.driver.find_element(By.XPATH, "//*[@ng-model='hours']")
        time_hh.clear()
        sleep(1)
        time_hh.send_keys(hour)

        return time_hh.get_attribute('value')

    def input_time_minutes(self, minutes):
        time_mm = self.driver.find_element(By.XPATH, "//*[@ng-model='minutes']")
        time_mm.clear()
        time_mm.send_keys(minutes)
        sleep(2)

        return time_mm.get_attribute('value')

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, "//*[@ng-click='create();main.reset_filter_employees();']")
        save_button.click()