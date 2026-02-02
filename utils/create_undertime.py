from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class CreateUndertime():

    def click_create_button(self):
        create_button = self.driver.find_element(By.XPATH,"//button[contains(@class, 'btn-danger')]")
        create_button.click()

    def input_employee(self, employee):
        employee_input = self.driver.find_element(By.XPATH,"//*[@aria-owns = 'ui-select-choices-1']")
        sleep(3)
        employee_input.send_keys(employee)
        employee_input.send_keys(Keys.TAB)
        employee_input_data = employee_input.get_attribute('value')

        return employee_input_data

    def input_hour(self, hour):
        input_hour = self.driver.find_element(By.XPATH,"//*[@ng-model = 'undertime.hours']")
        input_hour.send_keys(hour)
        input_hour.send_keys(Keys.TAB)
    
        input_hour_data = input_hour.get_attribute('value')

        return input_hour_data

    def input_minute(self, minute):
        input_minute = self.driver.find_element(By.XPATH,"//*[@ng-model = 'undertime.minutes']")
        input_minute.send_keys(minute)

        input_minute_data = input_minute.get_attribute('value')

        return input_minute_data

    def input_reason(self, reason):
        input_reason = self.driver.find_element(By.XPATH,"//*[@ng-model = 'undertime.reason']")
        input_reason.send_keys(reason)

        input_reason_data = input_reason.get_attribute('value')

        return input_reason_data

    def input_remarks(self, remarks):
        input_reason = self.driver.find_element(By.XPATH,"//*[@ng-model = 'undertime.remarks']")
        input_reason.send_keys(remarks)

        input_reason_data = input_reason.get_attribute('value')

        return input_reason_data

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[2]")
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