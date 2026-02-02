from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class CreateOfficialBusiness():

    def click_create_button(self):
        """Create button in holiday request page"""
        create_button = self.driver.find_element(By.XPATH,"//button[contains(@class, 'btn-danger')]")
        create_button.click()

    def input_employee(self, employee):
        """input employee in the employee inputbox"""

        employee_selection = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div/div/a")
        employee_selection.click()
        sleep(5)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(employee))
        self.driver.execute_script("arguments[0].click();",select_option)
        self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]").click()

    def input_hour(self, hour):
        input_hour = self.driver.find_element(By.XPATH,"//*[@ng-model = 'official_business.hours']")
        input_hour.send_keys(hour)
        input_hour.send_keys(Keys.TAB)
    
        input_hour_data = input_hour.get_attribute('value')

        return input_hour_data

    def input_minute(self, minute):
        input_minute = self.driver.find_element(By.XPATH,"//*[@ng-model = 'official_business.minutes']")
        input_minute.send_keys(minute)

        input_minute_data = input_minute.get_attribute('value')

        return input_minute_data

    def input_reason(self, reason):
        input_reason = self.driver.find_element(By.XPATH,"//*[@ng-model = 'official_business.reason']")
        input_reason.send_keys(reason)

        input_reason_data = input_reason.get_attribute('value')

        return input_reason_data

    def input_remarks(self, remarks):
        input_remarks = self.driver.find_element(By.XPATH,"//*[@ng-model = 'official_business.remarks']")
        input_remarks.send_keys(remarks)

        input_remarks_data = input_remarks.get_attribute('value')

        return input_remarks_data

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

    def click_wholeday_button(self):
        wholeday_button = self.driver.find_element(By.XPATH,"//*[@id='whole_day']")
        wholeday_button.click()

    def click_hours_button(self):
       hours_button = self.driver.find_element(By.XPATH,"//*[@id='hours']")
       hours_button.click()

    def input_date(self, date):
        input_date = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[1]/p[1]/input')
        input_date.clear()
        input_date.send_keys(date)

        input_date_data = input_date.get_attribute('value')

        return input_date_data

    def input_time_from(self, hour, minute):
        input_hour = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/input')
        input_hour.send_keys(hour)

        input_hour_data = input_hour.get_attribute('value')

        input_minute = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/input')
        input_minute.send_keys(hour)

        input_minute_data = input_minute.get_attribute('value')

        return input_hour_data, input_minute_data

    def input_time_to(self, hour, minute):
        input_hour = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/input')
        input_hour.send_keys(hour)

        input_hour_data = input_hour.get_attribute('value')

        input_minute = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[3]/div/table/tbody/tr[2]/td[3]/input')
        input_minute.send_keys(minute)

        input_minute_data = input_minute.get_attribute('value')

        return input_hour_data, input_minute_data