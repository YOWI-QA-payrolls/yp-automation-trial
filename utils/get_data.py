from math import ceil
from webbrowser import get
from utils.filters import AdvanceFilter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.pagination import TablePagination
from utils.table import TableRecord

def get_employee_location(self ,capsys, input_location):
    """Get employee's list of the filtered location under Employee Information Location Module"""

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_location_module = self.driver.find_element(By.XPATH,"//*[@id='employeelocation']/a")
    self.driver.execute_script("arguments[0].click();",employee_location_module)

    sleep(10)
    AdvanceFilter.button_click(self)
    AdvanceFilter.select_location(self,input_data=input_location,filter_no='ui-select-choices-2')
    self.driver.implicitly_wait(5)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_multiple_employee_location(self ,capsys, input_location):
    """Get employee's list of the filtered multiple location under Employee Information Location Module"""
    
    self.driver.implicitly_wait(5)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_location_module = self.driver.find_element(By.XPATH,"//*[@id='employeelocation']/a")
    self.driver.execute_script("arguments[0].click();",employee_location_module)

    AdvanceFilter.button_click(self)
    for selection in input_location:
        AdvanceFilter.select_location(self,input_data = selection ,filter_no='ui-select-choices-2')
          
    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_employee_division(self, capsys, input_division):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_division_module = self.driver.find_element(By.XPATH,"//*[@id='employeedivision']/a")
    self.driver.execute_script("arguments[0].click();",employee_division_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_division(self,input_data=input_division,filter_no='ui-select-choices-3')
    self.driver.implicitly_wait(5)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)
    sleep(10)
    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button(self)

    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_multiple_employee_division(self ,capsys, input_division):
    
    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_division_module = self.driver.find_element(By.XPATH,"//*[@id='employeedivision']/a")
    self.driver.execute_script("arguments[0].click();",employee_division_module)

    AdvanceFilter.button_click(self)
    for selection in input_division:
        AdvanceFilter.select_division(self,input_data = selection ,filter_no='ui-select-choices-3')
          
    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.drivser.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button()

    return employee_name

def get_employee_department(self ,capsys, input_department):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_deparment_module = self.driver.find_element(By.XPATH,"//*[@id='employee_department']/a")
    self.driver.execute_script("arguments[0].click();",employee_deparment_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_department(self,input_data=input_department,filter_no='ui-select-choices-4')
    self.driver.implicitly_wait(5)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button()

    return employee_name

def get_multiple_employee_department(self ,capsys, input_department):
    
    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_department_module = self.driver.find_element(By.XPATH,"//*[@id='employee_department']/a")
    self.driver.execute_script("arguments[0].click();",employee_department_module)

    AdvanceFilter.button_click(self)
    for selection in input_department:
        AdvanceFilter.select_department(self,input_data = selection ,filter_no='ui-select-choices-4')
          
    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button(self)

    return employee_name

def get_employee_section(self ,capsys, input_section):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_section_module = self.driver.find_element(By.XPATH,"//*[@id='employeesection']/a")
    self.driver.execute_script("arguments[0].click();",employee_section_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_section(self,input_data=input_section,filter_no='ui-select-choices-5')
    
    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)
    sleep(5)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_multiple_employee_section(self ,capsys, input_section):
    
    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_section_module = self.driver.find_element(By.XPATH,"//*[@id='employeesection']/a")
    self.driver.execute_script("arguments[0].click();",employee_section_module)

    AdvanceFilter.button_click(self)
    for selection in input_section:
        AdvanceFilter.select_section(self,input_data = selection ,filter_no='ui-select-choices-5')
          
    search_button = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button(self)

    return employee_name

def get_employee(self ,capsys, input_employee):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_chapa_module = self.driver.find_element(By.XPATH,"//*[@id='employee_chapa']/a")
    self.driver.execute_script("arguments[0].click();",employee_chapa_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_employee_employee_module(self,input_data=input_employee)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[1]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_employee_undertime(self ,capsys, input_employee):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_chapa_module = self.driver.find_element(By.XPATH,"//*[@id='employee_chapa']/a")
    self.driver.execute_script("arguments[0].click();",employee_chapa_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_employee_employee_module(self,input_data=input_employee)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[1]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

def get_job_level(self, capsys, input_job_level):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_chapa_module = self.driver.find_element(By.XPATH,"//*[@id='employeeinfo']/a")
    self.driver.execute_script("arguments[0].click();",employee_chapa_module)
    
    AdvanceFilter.button_click(self)
    sleep(2)
    AdvanceFilter.select_job_level(self,input_data=input_job_level,request_type= 'filter.job_level')
    search_button = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[2]/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[12]/button[1]")
    search_button.click()

    sleep(5)

    page_count = get_table_record_page_count(self, capsys)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[7]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button(self)

    return employee_name
 
def get_employee_payroll_status(self ,capsys, payroll_status):

    self.driver.get("https://yp.yahshuasupport.com/employees/information/informations/main_page/")
    sleep(5)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_payroll_status(self,input_data=payroll_status,request_type='filter.payroll_status')
    
    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[12]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)
    sleep(5)
    
    page_count = TableRecord.get_page_count(self)

    employee_name = []
    for pages in range(1,int(page_count)+1):
        table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
        self.driver.implicitly_wait(10)
        for row in range(1,table_row_count_request+1):
            table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[7]")
            table_row = table_row.text
            employee_name.append(table_row)

        TablePagination.next_button(self)

    return employee_name

def get_table_record_page_count(self,capsys):
    total_records = self.driver.find_element(By.XPATH, "//*[@ng-hide=\"main.current_module == 'dashboard'\"]")
    table_records = total_records.text
    cut_text_get_value = table_records.split(" : ")
    total_records = int(cut_text_get_value[1]) / 10
    page_count = ceil(total_records)

    return page_count

def get_employee_undertime(self ,capsys, input_employee):

    self.driver.implicitly_wait(10)
    employees_module = self.driver.find_element_by_link_text("Employees")
    employees_module.click()

    employee_information = self.driver.find_element(By.XPATH,"//*[@id='information_list']/a/span")
    self.driver.execute_script("arguments[0].click();",employee_information)

    employee_chapa_module = self.driver.find_element(By.XPATH,"//*[@id='employee_chapa']/a")
    self.driver.execute_script("arguments[0].click();",employee_chapa_module)

    AdvanceFilter.button_click(self)
    AdvanceFilter.select_employee_employee_module(self,input_data=input_employee)

    search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
    self.driver.execute_script("arguments[0].click();",search_button)

    table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='tablee']/tbody/tr"))
    employee_name = []
    for row in range(1,table_row_count+1):
        employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='tablee']/tbody/tr["+ str(row) +"]/td[1]")
        employee = employee_name_column.text
        employee_name.append(employee)
    with capsys.disabled():
        print(employee_name)

    return employee_name

class EmployeeTable():

    def get_employee_status_recommended(self, page_count, table_name):
        """Get employee status of the records in the table"""

        employee_list = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id ='"+(table_name)+"']/tbody/tr"))
            for row in range(1,table_row_count_request+1):
                    self.driver.implicitly_wait(15)
                    table_row = self.driver.find_element(By.XPATH,"//*[@id ='"+(table_name)+"']/tbody/tr["+ str(row) +"]/td[9]")
                    table_row = table_row.text
                    separated_text = table_row.split("\n")
                    try :
                        employee_list.append(separated_text[1])
                    except IndexError:
                        break
            TablePagination.next_button(self)

        return employee_list

    def get_employee_name(self, page_count, table_name):
        """Get employee name of the records in the table"""

        employee_list = []
        for pages in range(1,int(page_count)+1):
            table_row_count =  self.driver.find_element(By.XPATH,"//*[@id='"+(table_name)+"']/tbody/tr")
            table_row_count_request =  len(table_row_count)
            if table_row_count_request ==0:
                 raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(10)
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='"+(table_name)+"']/tbody/tr["+ str(row) +"]/td[3]")
                table_row = table_row.text
                employee_list.append(table_row)
            TablePagination.next_button(self)

        return employee_list

class EmployeeModuleTable():

    def get_employee_payroll_status(self ,capsys, payroll_status):
        """Get the employee payroll status im Employee Information Profile Module"""

        self.driver.get("https://yp.yahshuasupport.com/employees/information/informations/main_page/")
        sleep(5)

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_payroll_status(self,input_data=payroll_status,request_type='filter.payroll_status')
        
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[12]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)
        sleep(5)
        
        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[7]")
                table_row = table_row.text
                employee_name.append(table_row)
            TablePagination.next_button(self)

        return employee_name

    def get_employee_location(self ,capsys, input_location):
        """get all the records from table of Employee module > Information > Location Sub Module to check if employee in the records does exist in the request"""
    
        self.driver.implicitly_wait(10)
        self.driver.get("https://yp.yahshuasupport.com/employees/information/locations/main_page/")

        sleep(10)
        AdvanceFilter.button_click(self)
        sleep(5)
        AdvanceFilter.select_location(self, input_location, filter_no='ui-select-choices-2')
        self.driver.implicitly_wait(5)

        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
        employee_name = []
        for row in range(1,table_row_count+1):
            employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            employee = employee_name_column.text
            employee_name.append(employee)
        with capsys.disabled():
            print(employee_name)

        return employee_name

    def get_employee_division(self, capsys, input_division):
        """get all the records from table of Employee module > Information > Division Sub Module to check if employee in the records does exist in the request"""

        self.driver.implicitly_wait(10)
        self.driver.get("https://yp.yahshuasupport.com/employees/information/divisions/main_page/")

        sleep(10)
        AdvanceFilter.button_click(self)
        sleep(5)
        AdvanceFilter.select_division(self, input_division, filter_no='ui-select-choices-3')
        
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
                table_row = table_row.text
                employee_name.append(table_row)

            TablePagination.next_button()

        with capsys.disabled():
            print(employee_name)

        return employee_name
        
    def get_employee_department(self ,capsys, input_department):

        self.driver.implicitly_wait(10)
        self.driver.get("https://yp.yahshuasupport.com/employees/information/departments/main_page/")

        sleep(10)
        AdvanceFilter.button_click(self)
        sleep(5)
        AdvanceFilter.select_division(self, input_department, filter_no='ui-select-choices-4')

        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
                table_row = table_row.text
                employee_name.append(table_row)

        TablePagination.next_button()

        return employee_name
        
    def get_employee_section(self ,capsys, input_section):

        self.driver.implicitly_wait(10)
        self.driver.get("https://yp.yahshuasupport.com/employees/information/sections/main_page/")

        sleep(10)
        AdvanceFilter.button_click(self)
        sleep(5)

        AdvanceFilter.select_section(self,input_section,filter_no='ui-select-choices-5')
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)
        sleep(5)

        table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
        employee_name = []
        for row in range(1,table_row_count+1):
            employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            employee = employee_name_column.text
            employee_name.append(employee)
        with capsys.disabled():
            print(employee_name)

        return employee_name

    def get_employee(self ,capsys, input_employee):
        
        self.driver.get('https://yp.yahshuasupport.com/employees/information/chapa/main_page/')
        self.driver.implicitly_wait(10)

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_employee_employee_module(self, input_employee)
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
        employee_name = []
        for row in range(1,table_row_count+1):
            employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[1]")
            employee = employee_name_column.text
            employee_name.append(employee)
        with capsys.disabled():
            print(employee_name)

        return employee_name

#Multiple selection

    def get_multiple_employee_location(self ,capsys, multiple_locaton_selection):
        """Get employee's list of the filtered multiple location under Employee Information Location Module"""
        
        self.driver.get('https://yp.yahshuasupport.com/employees/information/locations/main_page/')
        self.driver.implicitly_wait(10)
        sleep(10)

        AdvanceFilter.button_click(self)
        for input_location in multiple_locaton_selection:
            AdvanceFilter.select_location(self, input_location,filter_no='ui-select-choices-2')
            
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        table_row_count = len(self.driver.find_element(By.XPATH,"//table[@id='table']/tbody/tr"))
        employee_name = []
        for row in range(1,table_row_count+1):
            employee_name_column = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
            employee = employee_name_column.text
            employee_name.append(employee)
        with capsys.disabled():
            print(employee_name)

        return employee_name

    def get_multiple_employee_division(self ,capsys, multiple_division_selection):
    
        self.driver.get('https://yp.yahshuasupport.com/employees/information/divisions/main_page/')
        self.driver.implicitly_wait(10)

        sleep(10)
        AdvanceFilter.button_click(self)
        for input_division in multiple_division_selection:
            AdvanceFilter.select_division(self,input_division ,filter_no='ui-select-choices-3')
            
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            if table_row_count_request ==0:
                    raise Exception("the record is empty, no record to select")
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
                table_row = table_row.text
                employee_name.append(table_row)

            TablePagination.next_button(self)

        return employee_name

    def get_multiple_employee_department(self ,capsys, multiple_department_selection):
    
        self.driver.get('https://yp.yahshuasupport.com/employees/information/departments/main_page/')
        self.driver.implicitly_wait(10)

        sleep(10)
        AdvanceFilter.button_click(self)
        for input_department in multiple_department_selection:
            AdvanceFilter.select_department(self,input_department ,filter_no='ui-select-choices-4')
            
        search_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[9]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            if table_row_count_request ==0:
                    raise Exception("the record is empty, no record to select")
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
                table_row = table_row.text
                employee_name.append(table_row)

            TablePagination.next_button(self)

        return employee_name

    def get_multiple_employee_section(self ,capsys, multiple_section_selection):
        
        self.driver.get(' https://yp.yahshuasupport.com/employees/information/sections/main_page/')
        self.driver.implicitly_wait(10)
        
        sleep(10)
        AdvanceFilter.button_click(self)
        for input_section in multiple_section_selection:
            AdvanceFilter.select_section(self,input_section, filter_no='ui-select-choices-5')
            
        search_button = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[11]/button[1]")
        self.driver.execute_script("arguments[0].click();",search_button)

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            if table_row_count_request ==0:
                    raise Exception("the record is empty, no record to select")
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[2]")
                table_row = table_row.text
                employee_name.append(table_row)

            TablePagination.next_button(self)

        return employee_name

    def get_job_level(self, input_job_level):

        self.driver.get('https://yp.yahshuasupport.com/employees/information/informations/main_page/')
        self.driver.implicitly_wait(10)
    
        sleep(10)
        AdvanceFilter.button_click(self)
        sleep(2)
        AdvanceFilter.select_job_level(self, input_job_level,request_type= 'filter.job_level')
        search_button = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div[2]/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[12]/button[1]")
        search_button.click()

        sleep(5)

        page_count = TableRecord.get_page_count(self)

        employee_name = []
        for pages in range(1,int(page_count)+1):
            table_row_count_request =  len(self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr"))
            self.driver.implicitly_wait(10)
            for row in range(1,table_row_count_request+1):
                table_row = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr["+ str(row) +"]/td[7]")
                table_row = table_row.text
                employee_name.append(table_row)

            TablePagination.next_button(self)

        return employee_name

class EmployeeTableLeave():

    def get_leave_employee_status_recommended(self, page_count, table_name):
        employee_list = []
        for pages in range(page_count):
            table_row_count_request =  self.driver.find_element(By.XPATH,"//*[@id ='"+(table_name)+"']/tbody/tr/td[11]/span[2]/b")
            
            if table_row_count_request == 0:
                raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(20)
            for row in table_row_count_request:
                self.driver.implicitly_wait(20)
                table_row = row.text
                separated_text = table_row.split("\n")
                try :
                    employee_list.append(separated_text)
                except IndexError:
                    break
            TablePagination.next_button(self)   

        return employee_list

    def get_employee_name(self, page_count, table_name):
        """Get employee name of the records in the table"""

        employee_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr/td[3]")

            if table_row_count_request == 0:
                raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(20)
            for row in table_row_count_request:     
                table_row = row.text
                employee_list.append(table_row)
            TablePagination.next_button(self)
            

        return employee_list


    
