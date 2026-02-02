from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium import webdriver
import sys
sys.setrecursionlimit(10000)

# def to_appear(self, element_variable_name):
#     element = element_variable_name.is_displayed()
#     if element == True:
#         pass
#         return True
#     else:
#         sleep(0.5)
#         to_appear(self, element_variable_name)

class AdvanceFilter():

    def to_appear(self, element_variable_name):
        element = element_variable_name.is_displayed()
        if element == True:
            pass
            return True
        elif element == False:
            sleep(0.2)
            AdvanceFilter.to_appear(self, element_variable_name)

    def button_click(self):
        """Opening Advance Filter"""
        
        advance_filter_button = self.driver.find_element(By.XPATH, "//*[@popover-title = 'Advance Filter']")
        AdvanceFilter.to_appear(self,advance_filter_button)
        advance_filter_button.click()
        sleep(3)
    
    def select_status(self, status_selection ,filter_no):
        """Status selection from advance filter"""

        deselect_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]")
        AdvanceFilter.to_appear(self,deselect_button)
        deselect_button.click()

        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        wait_element_appear(self, status_option)
        status_option.click()

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(status_selection))
        self.driver.execute_script("arguments[0].click();",select_option)

        status_field = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/ul/span/li/span")
        status_field_data = status_field.text

        return status_field_data

    def select_status_leave(self,input_data,filter_no):
        """Status selection from advance filter"""

        self.driver.implicitly_wait(10)
        sleep(1)
        deselect_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]/i")
        deselect_button.click()
        sleep(5)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)
        sleep(5)
        return input_data


    def select_payroll_status(self,input_data,request_type):
        """Payroll Status selection from advance filter"""

        self.driver.implicitly_wait(15)
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}']".format(request_type))
        select_payroll_status.click()
        sleep(3)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_type_of_leave(self,input_data,filter_no):
        """Location selection from advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()
        sleep(3)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_location_click(self,input_data,request_type): # not functioning
        """Location selection from advance filter"""

        status_option = self.driver.find_element(By.XPATH, "//*[@ng-model= '{}']".format(request_type))
        status_option.click()

        sleep(2)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_location(self, input_location, filter_no):
        """Location selection from advance filter"""

        self.driver.implicitly_wait(15)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()
        sleep(3)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_location))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_sub_location(self,input_sub_location,filter_no):
        """Location selection from advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()
        sleep(3)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_sub_location))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_cost_center(self,input_cost_center,filter_no):
        """Location selection from advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()
        sleep(3)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_cost_center))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_division(self,input_division,filter_no):
        """Division selection from advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
        status_option.click()
        sleep(5)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_division))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_department(self, input_department, filter_no ):
        """Department selection form advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= '{}']".format(filter_no))
        status_option.click()
        sleep(5)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_department))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_section(self, input_section, filter_no ):
        """Department selection form advance filter"""

        self.driver.implicitly_wait(10)
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= '{}']".format(filter_no))
        status_option.click()
        sleep(5)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_section))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_job_level(self,input_job_level,request_type): 

        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='{}']".format(request_type))
        select_payroll_status.click()

        sleep(1)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_job_level))
        self.driver.execute_script("arguments[0].click();",select_option)

    def select_employee(self,input_employee):
        sleep(3)
        
        select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[8]/div[2]/a/span[3]")
        self.driver.execute_script("arguments[0].click();",select_employee)
        self.driver.implicitly_wait(10)
        sleep(2)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_employee))
        self.driver.execute_script("arguments[0].click();",select_option)
        
    def select_employee_deduction_module(self,input_data):
        sleep(1)
        
        select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[2]")
        self.driver.execute_script("arguments[0].click();",select_employee)
        self.driver.implicitly_wait(10)
        sleep(2)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)
        

    def select_employee_employee_module(self,input_data):
        sleep(1)

        select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div[2]/a/span[1]")
        self.driver.execute_script("arguments[0].click();",select_employee)
        self.driver.implicitly_wait(10)
        sleep(2)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)
        
    def select_user(self, input_data, request_type):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='{}']".format(request_type))
        select_payroll_status.click()

        sleep(2)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)
        

    def check_show_inactive(self):
        
        element = self.driver.find_element(By.XPATH, "//*[@ng-model='include_inactive.value']")

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)

    def click_search_inputbox(self):
        advance_filter_search = self.driver.find_element_by_link_text('Search')
        advance_filter_search.click()

    def select_leave_search(self):
        advance_filter_search = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
        advance_filter_search.click()
    #This is new for standard search in all filter

    # def click_search_button(self, module_name):

    #     if(module_name=="overtime"):
    #         select= "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]"
    #     elif(module_name=="undertime"):
    #         select= "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]"
    #     else:
    #         print("No module found")

        # advance_filter_search = self.driver.find_element(By.XPATH, select)
        # advance_filter_search.click()

    def click_search_button(self):
        search_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
        AdvanceFilter.to_appear(self, search_button)
        search_button.click()           

    def click_reset_button(self):
        reset_button = self.driver.find_element(By.XPATH, "//button[text()='Reset']")
        wait_element_appear(self, reset_button)
        reset_button.click()

def wait_element_appear(self, element_variable_name):
    element = element_variable_name.is_displayed()
    if element == True:
       pass
       return True
       
    else:
        sleep(0.3)
        wait_element_appear(self, element_variable_name)


def advance_filter_function(self):
    advance_button = self.driver.find_element(By.XPATH, "//*[@popover-title ='Advance Filter']")
    """Opening Advance Filter"""
    
    advance_button = self.driver.find_element(By.XPATH, "//*[@popover-title = 'Advance Filter']")
    wait_element_appear(self,advance_button)
    advance_button.click()
    time.sleep(3)


def review_status_only(self):
    deselect_all = self.driver.find_element(By.XPATH,
                                            "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]")
    deselect_all.click()

    status = self.driver.find_element(By.XPATH,
                                      "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/ul/li/input")
    status.click()

    review_option = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/div/ul/li/ul/li[1]/div/div")
    review_option.click()
    time.sleep(5)


def advance_filter_function_status(self):
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-1']")
    status_option.click()
    status_option.send_keys(Keys.RETURN)

    time.sleep(15)

    self.driver.execute_script("$('.fa-check').click();")
    self.driver.execute_script("$('.fa-times').click();")


def advance_filter_function_payroll_status_normal(self):
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = 'ot_request.payroll_status']")
    select_payroll_status.click()
    time.sleep(3)
    normal_option = self.driver.find_element(By.XPATH, "//*[text()='Normal']")
    self.driver.execute_script("arguments[0].click();", normal_option)


def advance_filter_function_payroll_status_confidential(self):
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = 'ot_request.payroll_status']")
    select_payroll_status.click()
    time.sleep(3)
    normal_option = self.driver.find_element(By.XPATH, "//*[text()='Confidential']")
    self.driver.execute_script("arguments[0].click();", normal_option)


def advance_filter_function_location(self):
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-3]")
    status_option.click()
    status_option.send_keys(Keys.RETURN)

    time.sleep(5)

    self.driver.execute_script("$('.fa-check').click();")
    self.driver.execute_script("$('.fa-times').click();")


def advance_filter_function_division(self):
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-4]")
def advance_filter_function_status(self,input_data,filter_no):
    """Status selection from advance filter"""

    self.driver.implicitly_wait(10)
    sleep(1)
    deselect_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]")
    deselect_button.click()
    sleep(3)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    return input_data

def advance_filter_function_status_leave(self,input_data,filter_no):
    """Status selection from advance filter"""

    self.driver.implicitly_wait(10)
    sleep(1)
    deselect_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]/i")
    deselect_button.click()
    sleep(5)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    sleep(5)
    return input_data


def advance_filter_function_payroll_status(self,input_data,request_type):
    """Payroll Status selection from advance filter"""

    self.driver.implicitly_wait(15)
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}']".format(request_type))
    select_payroll_status.click()
    sleep(3)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_type_of_leave(self,input_data,filter_no):
    """Location selection from advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()
    sleep(3)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_location_click(self,input_data,request_type): # not functioning
    """Location selection from advance filter"""

    status_option = self.driver.find_element(By.XPATH, "//*[@ng-model= '{}']".format(request_type))
    status_option.click()

    sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_location(self,input_data,filter_no):
    """Location selection from advance filter"""

    self.driver.implicitly_wait(15)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()
    sleep(3)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_sub_location(self,input_data,filter_no):
    """Location selection from advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()
    sleep(3)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_cost_center(self,input_data,filter_no):
    """Location selection from advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()
    sleep(3)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_division(self,input_data,filter_no):
    """Division selection from advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns='{}']".format(filter_no))
    status_option.click()
    sleep(5)

    time.sleep(5)

    self.driver.execute_script("$('.fa-check').click();")
    self.driver.execute_script("$('.fa-times').click();")


def advance_filter_function_department(self, input_data):
    status_option = self.driver.find_element_by_xpath("//*[@aria-owns= 'ui-select-choices-5]")
    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_department(self, input_data, filter_no ):
    """Department selection form advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= '{}']".format(filter_no))
    status_option.click()
    sleep(5)

    time.sleep(5)

    self.driver.execute_script("$('.fa-check').click();")
    self.driver.execute_script("$('.fa-times').click();")


def advance_filter_function_job_level(self, input_data):
    select_payroll_status = self.driver.find_element_by_xpath("//*[@ng-model='ot_request.job_level']")
    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_section(self, input_data, filter_no ):
    """Department selection form advance filter"""

    self.driver.implicitly_wait(10)
    status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= '{}']".format(filter_no))
    status_option.click()
    sleep(5)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_job_level(self,input_data,request_type): 

    
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='{}']".format(request_type))
    select_payroll_status.click()
    time.sleep(3)
    normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
    self.driver.execute_script("arguments[0].click();", normal_option)


def advance_filter_function_employee(self):
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='ot_request.employee']")
    select_payroll_status.click()
    time.sleep(3)
    normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
    self.driver.execute_script("arguments[0].click();", normal_option)


def advance_filter_function_user(self, input_data):
    select_payroll_status = self.driver.find_element_by_xpath("//*[@ng-model='ot_request.user']")
    sleep(1)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

def advance_filter_function_employee(self,input_data):
    sleep(1)
    
    select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[8]/div[2]/a/span[3]")
    self.driver.execute_script("arguments[0].click();",select_employee)
    self.driver.implicitly_wait(10)
    sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    
def advance_filter_function_employee_deduction_module(self,input_data):
    sleep(1)
    
    select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[2]")
    self.driver.execute_script("arguments[0].click();",select_employee)
    self.driver.implicitly_wait(10)
    sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    

def advance_filter_function_employee_employee_module(self,input_data):
    sleep(1)

    select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div[2]/a/span[1]")
    self.driver.execute_script("arguments[0].click();",select_employee)
    self.driver.implicitly_wait(10)
    sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    
def advance_filter_function_employee_employee_module(self,input_data):
    time.sleep(1)

    select_employee = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div[2]/a/span[1]")
    self.driver.execute_script("arguments[0].click();",select_employee)
    self.driver.implicitly_wait(10)
    time.sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)

    
def advance_filter_function_user(self, input_data, request_type):
    select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='{}']".format(request_type))
    select_payroll_status.click()
    time.sleep(3)
    normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
    self.driver.execute_script("arguments[0].click();", normal_option)


def advance_filter_show_inactive(self, input_data):
    element = self.driver.find_element_by_xpath("//*[@ng-model='include_inactive.value']")
    sleep(2)

    select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    

def advance_filter_show_inactive(self):
    
    element = self.driver.find_element(By.XPATH, "//*[@ng-model='include_inactive.value']")

    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("arguments[0].click();", element)


def advance_filter_function_search(self):
    advance_filter_search = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
    advance_filter_search.click()
    time.sleep(3)


def advance_filter_function_leave_search(self):
    advance_filter_search = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
    advance_filter_search.click()
#This is new for standard search in all filter
def advance_filter_function_search(self, module_name):

    if(module_name=="overtime"):
        select= "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]"
    elif(module_name=="undertime"):
        select= "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/div[1]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]"
    else:
        print("No module found")

    advance_filter_search = self.driver.find_element(By.XPATH, select)
    advance_filter_search.click()

def advance_filter_function_reset(self):
    advance_filter_reset = self.driver.find_element(By.XPATH,
                                                    "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[2]")
    advance_filter_reset.click()
    time.sleep(3)


class jasson_filters():

    def advance_filter_function(self):
        try:
            advance_button = self.driver.find_element(By.XPATH, "//*[@popover-title ='Advance Filter']")
            advance_button.click()
            advance_button_clicked = True
        except Exception as error:
            print(error.__class__)
            advance_button_clicked = False
        
        time.sleep(3)

        return advance_button_clicked

    def recommended_status_only(self):
        deselect_all = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/button[2]")
        deselect_all.click()

        status = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/ul/li/input")
        status.click()

        recommended_option = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/div/ul/li/ul/li[3]/div/div")
        recommended_option.click()
        time.sleep(5)

        status_input_field = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/ul")
        actual_status = status_input_field.text

        return actual_status

    def advance_filter_function_status(self):
        
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-1']")
        status_option.click()
        status_option.send_keys(Keys.RETURN)

        time.sleep(15)
        
        self.driver.execute_script("$('.fa-check').click();")
        self.driver.execute_script("$('.fa-times').click();")

    def advance_filter_function_payroll_status_normal(self):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = 'ot_request.payroll_status']")
        select_payroll_status.click()
        time.sleep(3)
        normal_option = self.driver.find_element(By.XPATH, "//*[text()='Normal']")
        self.driver.execute_script("arguments[0].click();",normal_option)

    def advance_filter_function_payroll_status_confidential(self):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model = 'ot_request.payroll_status']")
        select_payroll_status.click()
        time.sleep(3)
        normal_option = self.driver.find_element(By.XPATH, "//*[text()='Confidential']")
        self.driver.execute_script("arguments[0].click();",normal_option)

    def advance_filter_function_location(self):
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-3]")
        status_option.click()
        status_option.send_keys(Keys.RETURN)

        time.sleep(5)
        
        self.driver.execute_script("$('.fa-check').click();")
        self.driver.execute_script("$('.fa-times').click();")

    def advance_filter_function_division(self):
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-4]")
        status_option.click()
        status_option.send_keys(Keys.RETURN)

        time.sleep(5)
        
        self.driver.execute_script("$('.fa-check').click();")
        self.driver.execute_script("$('.fa-times').click();")

    def advance_filter_function_department(self):
        status_option = self.driver.find_element(By.XPATH, "//*[@aria-owns= 'ui-select-choices-5]")
        status_option.click()
        status_option.send_keys(Keys.RETURN)

        time.sleep(5)
        
        self.driver.execute_script("$('.fa-check').click();")
        self.driver.execute_script("$('.fa-times').click();")

    def advance_filter_function_job_level(self):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='ot_request.job_level']")
        select_payroll_status.click()
        time.sleep(3)
        normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
        self.driver.execute_script("arguments[0].click();",normal_option)

    def advance_filter_function_employee(self):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='ot_request.employee']")
        select_payroll_status.click()
        time.sleep(3)
        normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
        self.driver.execute_script("arguments[0].click();",normal_option)
        
    def advance_filter_function_user(self):
        select_payroll_status = self.driver.find_element(By.XPATH, "//*[@ng-model='ot_request.user']")
        select_payroll_status.click()
        time.sleep(3)
        normal_option = self.driver.find_element(By.XPATH, "//*[text()='Hourlies']")
        self.driver.execute_script("arguments[0].click();",normal_option)
        

    def advance_filter_show_inactive(self):
        
        element = self.driver.find_element(By.XPATH, "//*[@ng-model='include_inactive.value']")

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)

    def advance_filter_function_search(self):
        try:
            advance_filter_search = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
            advance_filter_search.click()
            search_button_clicked = True
        except Exception as error:
            print(error.__class__)
            search_button_clicked = False
        time.sleep(3)

        return search_button_clicked


    def advance_filter_function_reset(self):
        advance_filter_reset = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[2]")
        advance_filter_reset.click()
        time.sleep(3)
        advance_filter_reset = self.driver.find_element(By.XPATH, "//*[text()='Reset']")
        advance_filter_reset.click()
