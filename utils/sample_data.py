import requests
import pytest
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DataSetup():

    def add_location(self, sample_location):
        "Add sample data for location in the miscellaneous list on company setting"
        
        sleep(5)
        for data in sample_location:
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[5]/div[2]/div[4]/div/button')
            create_button.click()
            sleep(3)
            
            input_name =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/input')
            input_name.click()
            input_name.send_keys(data)
            sleep(5)

            save_button =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button[2]')
            save_button.click()

    def add_department(self, sample_department, sample_location):
        "Add sample data for department in the miscellaneous list on company settings"

        sleep(5)
        for data,location in zip(sample_department, sample_location):
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[6]/div/button')
            create_button.click()
            sleep(3)
            
            input_name =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/input')
            input_name.click()
            input_name.send_keys(data)
            sleep(5)

            input_location = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div/ul/li/input')
            input_location.click()

            select_location = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(location))
            self.driver.execute_script("arguments[0].click();",select_location)
            sleep(5)

            save_button =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button')
            save_button.click()

    def add_section(self,sample_section, sample_department):
        "Add sample data for section in the miscellaneous list on company settings"

        sleep(5)
        for data,department in zip(sample_section, sample_department):
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[9]/div[2]/div[6]/div/button')
            create_button.click()
            sleep(3)
            
            input_name =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/input')
            input_name.click()
            input_name.send_keys(data)
            sleep(5)

            input_department = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div/ul/li/input')
            input_department.click()

            select_department = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(department))
            self.driver.execute_script("arguments[0].click();",select_department)
            sleep(5)

            save_button =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button[2]')
            save_button.click()

    def add_position(self, sample_position, sample_department):
        "Add sample data for position in the miscellaneous list on company setting"

        sleep(5)
        for data,department in zip(sample_position, sample_department):
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[4]/div/button')
            create_button.click()
            sleep(3)
            
            input_name =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/input')
            input_name.click()
            input_name.send_keys(data)
            sleep(5)

            input_department = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/ul/li/input')
            input_department.click()

            select_department = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(department))
            self.driver.execute_script("arguments[0].click();",select_department)
            sleep(5)

            save_button =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button[2]')
            save_button.click()

    def add_division(self, sample_division):
        "Add sample data for division in the miscellaneous list on company settings"

        sleep(5)
        for data in sample_division:
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[8]/div[2]/div[4]/div/button')
            create_button.click()
            sleep(3)
            
            input_name =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div/input')
            input_name.click()
            input_name.send_keys(data)
            sleep(5)

            save_button =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button[2]')
            save_button.click()

    def add_holidays(self, sample_holiday, sample_location):
        "Add sample data for holidays in the miscellaneous list on payments settings"

        holiday_data_name = ["Sept4(SUN)","Sept11(SUN)","Sept18(SUN)","Sept25(SUN)","Sept7(WED)","Sept14(WED)","Sept21(WED)","Sept28(WED)","Oct2(SUN)","Oct9(SUN)","Oct16(SUN)","Oct25(SUN)"]

        holiday_type_data = ["Special holiday","Regular holiday"]

        for name, holiday in zip(holiday_data_name, sample_holiday):

            create_button = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[2]/div[8]/div[2]/div[4]/div/button")
            create_button.click()

            sleep(3)

            holiday_name = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/input")
            holiday_name.send_keys(name)

            holiday_date = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/p[1]/input")
            holiday_date.send_keys(holiday)

            holiday_type = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/div[1]/a/span[1]")
            holiday_type.click()

            select_holiday = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(holiday_type_data[1]))
            self.driver.execute_script("arguments[0].click();",select_holiday)

            sleep(5)

            for data in sample_location:
                location_selection = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div[1]/ul/li/input")
                location_selection.click()
                select_holiday = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(data))
                self.driver.execute_script("arguments[0].click();",select_holiday)

            sleep(5)

            repeat_yearly_checkbox = self.driver.find_element(By.ID, "active")
            repeat_yearly_checkbox.click()

            save_button = self.driver.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div[1]/ul/li/input")
            save_button.click()  


    def add_schedule(self):
        "Add sample data for schedule in the miscellaneous list on payments settings"

        create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[1]/div[12]/div[2]/div[5]/div/button')
        create_button.click()

        sleep(3)

        schedule_code = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[1]/input")
        schedule_code.send_keys("qa_schedule")

        hours_per_day =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[2]/div[1]/input")
        hours_per_day.click()
        hours_per_day.send_keys("8")

        time_in_hr =  self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[1]/input")
        time_in_hr.send_keys("8")

        time_in_min = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[3]/input")
        time_in_min.send_keys("00")
       
        time_out_hr = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[1]/input")
        time_out_hr.send_keys("17")
       
        time_out_min = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[3]/input")
        time_out_min.send_keys("30")
        
        # default value of checkbox is true
        # monday_checkbox = self.driver.find_element(By.ID, "monday")
        # monday_checkbox.click()
       
        # tuesday_checkbox = self.driver.find_element(By.ID, "tuesday")
        # tuesday_checkbox.click(7)
       
        # wednesday_checkbox = self.driver.find_element(By.ID, "wednesday")
        # wednesday_checkbox.click()
       
        # thursday_checkbox = self.driver.find_element(By.ID, "thursday")
        # thursday_checkbox.click()
       
        # friday_checkbox = self.driver.find_element(By.ID, "friday")
        # friday_checkbox.click()
       
        # saturday_checkbox = self.driver.find_element(By.ID, "saturday")
        # saturday_checkbox.click()
       
        department_select_all = self.driver.find_element(By.XPATH, " //*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[8]/button[1]")
        department_select_all.click()
       
        location_select_all = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[10]/button[1]")
        location_select_all.click()
       
        section_select_all = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/fieldset/form/div[12]/button[1]")
        section_select_all.click()
       
        # active_button = self.driver.find_element(By.ID, "active")
        # active_button.click()
       
        save_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[2]")
        save_button.click()

        sleep(10)

    def add_users(self):
        "Add sample data for user in the user accounts"

        fullname = ['Recommend1', 'Approver1', 'Intern1']
        email = ['recommend@ypo.com','qaapprover@ypo.com','qaintern@ypo.com']
        password = ['QArecommend123#','QAapprover123#','QAintern123#']

        for fullname2,email2,password2 in zip(fullname, email, password):
            
            create_button = self.driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[2]/div[2]/div/div/div/button')
            create_button.click()

            sleep(10)

            fullname_input = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/input')
            fullname_input.send_keys(fullname2)

            email_input = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/input')
            email_input.send_keys(email2)

            password_input = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/input')
            password_input.send_keys(password2)

            confirm_password_input =  self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[5]/input')
            confirm_password_input.send_keys(password2)


            location_select_all = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[6]/button[1]')
            location_select_all.click()

            division_select_all = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[7]/button[1]')
            division_select_all.click()

            department_select_all = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[8]/button[1]')
            department_select_all.click()

            section_select_all = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[9]/button[1]')
            section_select_all.click()

            job_level_select_all = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[2]/div/div[2]/form/div[10]/button[1]')
            job_level_select_all.click()

            sleep(3)

            save_button = self.driver.find_element(By.XPATH,'//*[@id="page-top"]/div[1]/div/div/div/div[3]/div/button[2]')
            save_button.click()