from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from utils.dropdown import click_employee_dropdown

class CreateLeave():


    def click_create_button(self):
        """Create button in holiday request page"""
        create_button = self.driver.find_element(By.XPATH,"//button[contains(@class, 'btn-danger')]")
        create_button.click()

    def click_employee_dropdown(self):
        employee_selection = self.driver.find_element(By.XPATH, "//*[@ng-model = 'leave.employee']")
        sleep(3)
        employee_selection.click()

    def input_employee(self, employee):
        employee_name = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/input")
        employee_name.send_keys(employee)
        employee_name.send_keys(Keys.ENTER)
        sleep(3)

    def click_type_of_leave_dropdown(self):
        leave_type_dropdown = self.driver.find_element(By.XPATH, "//*[@placeholder='Type of Leave']")
        leave_type_dropdown.click()
        sleep(3)

    def click_whole_day_radio_button(self):
        whole_day = self.driver.find_element(By.XPATH, "//*[@id = 'whole_day']")
        whole_day.click()
        sleep(3)

    def click_half_day_radio_button(self):
        half_day = self.driver.find_element(By.XPATH, "//*[@id = 'half_day']")
        half_day.click()
        sleep(3)

    def input_reason_field(self, input_data, module):
        input_reason = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.reason']".format(module))
        input_reason.send_keys(input_data)
        sleep(5)

    def input_remarks(self, remarks):
        input_reason = self.driver.find_element(By.XPATH,"//*[@ng-model = 'holiday.remarks']")
        input_reason.send_keys(remarks)

        input_reason_data = input_reason.get_attribute('value')

        return input_reason_data

    def click_leave_submit_button(self):
        submit_button = self.driver.find_element(By.ID, 'leave_submit')
        self.driver.execute_script("arguments[0].click();", submit_button)
        sleep(3)

    def click_confirm_button(self):
        confirm_button = self.driver.find_element(By.CLASS_NAME, "confirm")
        confirm_button.click()
        sleep(0.5)

    def click_filter_button(self):
        filter_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/button")
        filter_button.click()

    def click_done_button(self):
        done_button = self.driver.find_element(By.XPATH,"//button[@class='btn btn-sm btn-success']")
        done_button.click()

    def click_select_all(self):
        select_all = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/button[1]/i")
        select_all.click()              

    def click_deselect_all(self):
        deselect_all = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/button[2]/i")
        deselect_all.click()

    def click_close_button(self):
        close_button =  self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[1]")
        close_button.click()

    def input_time_from_hour(self, input_data):
        hour = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[1]/input")
        hour.clear()
        hour.send_keys(input_data)

    def input_time_from_minute(self, input_data):
        minute = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[3]/input")
        minute.clear() 
        minute.send_keys(input_data)

    def input_time_to_hour(self, input_data):
        hour = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[1]/input")
        hour.clear()
        hour.send_keys(input_data)

    def input_time_to_minute(self, input_data):
        minute = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[3]/input")
        minute.clear()
        minute.send_keys(input_data)