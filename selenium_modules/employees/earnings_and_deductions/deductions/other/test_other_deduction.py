from pytest import skip
from time import sleep, time
from request_cookies import add_cookies
# from utils.set_site import Login
from utils.filters import AdvanceFilter, wait_element_appear
from utils.get_data import EmployeeTable, EmployeeModuleTable
from utils.pagination import TablePagination
from utils.table import TableRecord
from utils.search import Search
from utils.confirmation import Confirmation
from utils.setup import driversetup
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class Setup():

    def setup_method(self): 
        """Run this setup for this test class."""
        
        self.driver = driversetup()
        self.driver.maximize_window()
        url = "https://yp.yahshuasupport.com/dashboard/"
        self.driver.get(url)

        self.driver.delete_all_cookies()
        add_cookies(self)
        self.driver.refresh()

        self.driver.get("https://yp.yahshuasupport.com/employees/additional_pay_and_deductions/other_deduction/main_page/")

        
    def teardown_method(self, method):
        self.driver.quit()

class TestOtherDeduction(Setup):
    """Request leave test cases.""" 

    def test_clicking_viewby_button(self):
        """This test is under Check "View By" dropdown options functionality"""
        
        view_by_dropdown = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/a")
        view_by_dropdown.click()

        view_by_dropdown_options = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/div").is_displayed()
        
        assert  view_by_dropdown_options == True

        self.driver.close()

    def test_clicking_viewby_summary_option(self):
        """ Check response on clicking "Summary" options under "View By" dropdown button in the "Recurring Deductions" . """
        
        view_by_dropdown = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/a")
        view_by_dropdown.click()

        view_by_dropdown_options = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/div").is_displayed()
        assert  view_by_dropdown_options == True

        select_option = self.driver.find_element(By.XPATH, "//*[text()='Summary']")
        self.driver.execute_script("arguments[0].click();",select_option)

        sleep(3)
        
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-success")
        search_button.click()

        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Summary" 

        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]")
        is_table_record_displayed  = wait_element_appear(self,summary_table_record)
        
        assert is_table_record_displayed == True

        self.driver.close()

    def test_clicking_viewby_detailed_option(self):
        """ Check response on clicking "Detailed" options under "View By" dropdown button in the "Recurring Deductions" ."""
        
        view_by_dropdown = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/a")
        view_by_dropdown.click()

        view_by_dropdown_options = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/div").is_displayed()
        assert  view_by_dropdown_options == True

        select_option = self.driver.find_element(By.XPATH, "//*[text()='Detailed']")
        self.driver.execute_script("arguments[0].click();",select_option)

        sleep(3)
        
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-success")
        search_button.click()

        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Detailed" 

        sleep(10)

        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]")
        is_table_record_displayed  = wait_element_appear(self,summary_table_record)

        assert is_table_record_displayed == True

        self.driver.close()

    #@pytest.mark.skip(reason="no calendar date from feature")
    def test_clicking_calendar_icon_and_selecting_date_on_date_from(self):
        """Check "Date From" functionality ."""

        date_input = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[3]/span/tabletoolsdaterange2/p/input[1]")
        wait_element_appear(self, date_input)
        date_input.clear()

        date_input.send_keys("05/30/2022")
        
        check_date_input = date_input.get_attribute('value')

        assert check_date_input == "05/30/2022"

        self.driver.close()

    #@pytest.mark.skip(reason="no calendar date to feature")
    def test_clicking_calendar_icon_and_selecting_date_on_date_to(self):
        """Check "Date To" functionality""" 

        date_input = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[3]/span/tabletoolsdaterange2/p/input[2]")
        wait_element_appear(self, date_input)
        date_input.clear()
       
        date_input.send_keys("05/30/2022")
        
        check_date_input = date_input.get_attribute('value')

        assert check_date_input == "05/30/2022"

        self.driver.close()

    def test_clicking_input_box(self):
        """Check response on clicking input box under "Other Deduction Type".""" 

        other_deduction_type_input = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/ul/li/input")
        other_deduction_type_input.click()

        other_deduction_type_input_options = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/div")
        is_other_deduction_type_input_options_displayed = wait_element_appear(self, other_deduction_type_input_options)

        assert  is_other_deduction_type_input_options_displayed == True

        self.driver.close()

    def test_clicking_select_all_button(self):
            """Check response on clicking "Select All" button under "Other Deduction Type"""

            select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/button[1]")
            wait_element_appear(self, select_all_button)
            select_all_button.click()
        
            other_deduction_type_options = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/ul/li/input")
            other_deduction_type_options.get_attribute('value')

            assert other_deduction_type_options != "All"
            
            self.driver.close()

    def test_clicking_deselect_all_button(self):
        """Check response on clicking "Deselect All" button under "Other Deduction Type"""

        select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/button[1]")
        select_all_button.click()

        sleep(3)
        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/button[2]")
        deselect_all_button.click()

        other_deduction_type_options = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/ul/li/input")
        return_default_value = other_deduction_type_options.get_attribute('placeholder')

        assert return_default_value == "ALL"
        

        self.driver.close()

    def test_clicking_specific_other_deduction_type(self):
        """Check response on clicking specific Other Deduction Type""" 

        input_data = "Reversed Leave" 

        other_deduction_type = self.driver.find_element(By.XPATH,  "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/ul/li/input")
        other_deduction_type.click()

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        select_option.click()

        search_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[7]/div/button")
        search_button.click()

        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True

        self.driver.close()

    def test_clicking_multiple_other_deduction_type(self):
        """Check response on clicking multiple Other Deduction Type""" 

        other_deduction_type = ["Reversed Leave","Donation","Personal Loan"]

        for input_data in other_deduction_type:
            other_deduction_type = self.driver.find_element(By.XPATH,  "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[6]/div/ul/li/input")
            wait_element_appear(self, other_deduction_type)
            other_deduction_type.click()

            select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
            select_option.click()
            sleep(2)

        search_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[7]/div/button")
        search_button.click()

        sleep(5)

        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True
        
        self.driver.close()

class  TestSearchOtherDeduction(Setup):
    def test_searching_chapa_number(self, capsys):
        """Check response on searching Chapa number""" 

        input_data = "9003"
          
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data
        
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        page_count = TableRecord.get_page_count(self)

        chapa_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_elements_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[1]")

            if table_row_count_request == 0:
                raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(20)
            for row in table_row_count_request:     
                table_row = row.text
                chapa_list.append(table_row)

            TablePagination.next_button(self)

        no_duplicate_employee_request = list(dict.fromkeys(chapa_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)
            print(chapa_list)

        assert_lists = any(item in input_data for item in no_duplicate_employee_request)
        assert assert_lists == True

        self.driver.close()

    def test_searching_employee_name(self, capsys):
        """Check  "Regular Deduction Type" buttons functionality""" 

        input_data = "Mariafe"
          
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data
        
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        page_count = TableRecord.get_page_count(self)
        employee_name_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_elements_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[9]/div/table[1]/tbody/tr[1]")

            if table_row_count_request == 0:
                raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(20)
            for row in table_row_count_request:     
                table_row = row.text
                employee_name_list.append(table_row)

            TablePagination.next_button(self)

        no_duplicate_employee_request = list(dict.fromkeys(employee_name_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)
            print(employee_name_list)

        assert input_data in no_duplicate_employee_request[0]

        self.driver.close()
    
    def test_searching_with_no_entry(self, capsys):
        """Check "Advance Filter" button functionality""" 

        actual_page = 16

        Search.box_function(self,input_data= "")
        Search.click_icon_button(self)

        page_count = TableRecord.get_page_count(self)
        assert page_count == actual_page

        self.driver.close()

class TestAdvanceFilter(Setup):
    """Request leave Advance Fitler test cases."""

    def test_clicking_advance_filter(self):
        """Check response when clicking "Advance Filter" button""" 

        AdvanceFilter.button_click(self)
                                
        advance_filter_popup = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]")
        AdvanceFilter.to_appear(self, advance_filter_popup)
        is_advance_filter_popup_displayed = advance_filter_popup.is_displayed()

        assert is_advance_filter_popup_displayed == True

        self.driver.close()

    def test_advance_filter_payroll_status_dropdown_button(self):
        """Check response "Payroll Status" dropdown button.""" 

        AdvanceFilter.button_click(self)

        advance_filter_popup = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]").is_displayed()
        assert advance_filter_popup == True

        AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'filter.payroll_status')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/abbr")
        x_icon.click()

        payroll_status_option = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/span[1]").text
        
        assert payroll_status_option =="ALL"

        self.driver.close()

    def test_advance_filter_inputting_location(self):
        """Check response "Location" input box.""" 

        AdvanceFilter.button_click(self)

        input_location="DAVAO"
        AdvanceFilter.select_location(self,input_location,filter_no='ui-select-choices-4')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()

        select_all_button =  self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[1]")
        select_all_button.click()
        sleep(5)
        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[2]")
        deselect_all_button.click()

        location_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = location_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_division(self):
        """Check response "Division" input box.""" 

        AdvanceFilter.button_click(self)

        input_division="Division 1"
        AdvanceFilter.select_division(self,input_division,filter_no='ui-select-choices-5')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()

        select_all_button =  self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/button[1]")
        select_all_button.click()

        sleep(5)

        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/button[2]")
        deselect_all_button.click()

        division_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/div/ul/li/input")
        return_default_value = division_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_department(self):
        """Check response "Department" input box.""" 

        AdvanceFilter.button_click(self)

        input_department="Operations"
        AdvanceFilter.select_department(self,input_department,filter_no='ui-select-choices-6')
 
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()


        select_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[2]")
        deselect_all_button.click()

        department_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/li/input")
        return_default_value = department_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_section(self):
        """Check response "Section" input box.""" 

        AdvanceFilter.button_click(self)

        input_section="Accounts Payable"
        AdvanceFilter.select_section(self,input_section,filter_no='ui-select-choices-7')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
        x_icon.click()

        select_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/button[2]")
        deselect_all_button.click()

        section_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/div/ul/li/input")
        return_default_value = section_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_job_level(self, capsys):
        """Check response "Section" input box.""" 

        AdvanceFilter.button_click(self)
        sleep(5)

        input_job_level="Monthlies"
        AdvanceFilter.select_job_level(self,input_job_level,request_type= 'filter.job_level')

        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/abbr")
        x_icon.click()

        sleep(3)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        actual_data = self.soup.find('table', class_ = 'sticky-thead').find('thead').find('tr').find('th')
        with capsys.disabled():
            print(actual_data)
              
        self.driver.close()

    def test_advance_filter_inputting_employee(self):
        """Check response "Employee" input box.""" 

        AdvanceFilter.button_click(self)
        sleep(5)

        input_employee="IMC-2020_253 - ALPAY, KEVIN GIO J."
        AdvanceFilter.select_employee_deduction_module(self,input_employee)

        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/abbr")
        x_icon.click()

        employee_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[1]")
        return_default_value = employee_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_reset_button(self):
        """Check response "Reset" button.""" 

        AdvanceFilter.button_click(self)
        sleep(5)

        input_job_level="Monthlies"
        AdvanceFilter.select_job_level(self,input_job_level,request_type= 'filter.job_level')
        AdvanceFilter.select_employee_deduction_module(self,input_data="asfsa - Abanales, Joenel")
        AdvanceFilter.click_reset_button(self)
        sleep(5)

        job_level_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text
    
        assert return_default_value == "ALL"

        employee_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[1]")
        return_default_value = employee_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

class TestCaretButton(Setup):
    def test_regular_dedecution_caret_dropdown_button(self): 
        """Check response "Caret" dropdown button.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()

        assert is_caret_dropdown_displays == True

        self.driver.close()

    
    def test_regular_dedecution_caret_dropdown_create_button(self, capsys): 
        """Check response "Create" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        assert is_caret_dropdown_displays == True

        create_option = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[3]/a")
        create_option.click()
        sleep(1)


        self.driver.close()


    def test_regular_dedecution_caret_dropdown_export_button(self, capsys): 
        """Check response "Export" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        assert is_caret_dropdown_displays == True

        export_option = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[3]/a")
        export_option.click()
        sleep(1)

        get_url = requests.get("https://yp.yahshuasupport.com/export/common_tables/employee_other_deductions?fields={}&filters=%7B%22records_per_page%22%3A10%2C%22view_by%22%3A%22Summary%22%2C%22typee%22%3A%22Other%20Deduction%22%2C%22date_from%22%3A%222022-08-16%22%2C%22date_to%22%3A%222022-08-16%22%2C%22type_ids%22%3A%5B%5D%2C%22pagination%22%3A%7B%22limit%22%3A10%2C%22current_page%22%3A1%2C%22total_records%22%3A157%2C%22total_pages%22%3A16%2C%22limit_options_orig%22%3A%5B20%2C50%2C100%2C150%5D%2C%22limit_options%22%3A%5B20%2C50%2C100%2C150%2C157%5D%7D%2C%22show_hide_column%22%3Atrue%2C%22show_inactive%22%3Afalse%7D&email=false&view_by=%22Summary%22")

        assert 200 == get_url.status_code

        self.driver.close()

    def test_regular_dedecution_caret_dropdown_import_regular_button(self): 
        """Click "Import Regular" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()

        assert is_caret_dropdown_displays == True

        import_regular = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[4]/a")
        import_regular.click()

        get_url = requests.get("https://yp.yahshuasupport.com/settings/imports/#import_employee_other_additional_deduction")

        assert 200 == get_url.status_code

        self.driver.close()

    def test_regular_dedecution_caret_dropdown_print_button(self): 
        """Check response "Print" dropdown button.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()

        assert is_caret_dropdown_displays == True

        print_option = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[6]/a")
        print_option.click()

        get_url = requests.get("https://yp.yahshuasupport.com/employees/additional_pay_and_deductions/other_deductions/prints/?filters=%7B%22records_per_page%22:10,%22view_by%22:%22Summary%22,%22typee%22:%22Other%20Deduction%22,%22date_from%22:%222022-08-16%22,%22date_to%22:%222022-08-16%22,%22type_ids%22:[],%22pagination%22:%7B%22limit%22:10,%22current_page%22:1,%22total_records%22:157,%22total_pages%22:16,%22limit_options_orig%22:[20,50,100,150],%22limit_options%22:[20,50,100,150,157]%7D,%22show_hide_column%22:true,%22show_inactive%22:false%7D&print=yes&columns=&deduction_view_by=Summary&name=&inactive=false")

        assert 200 == get_url.status_code

        self.driver.close()

class TestRecordPerPage(Setup):
    def test_regular_dedecution_record_per_page_clicking_dropdown(self,capsys):
        """Check "Record Per Page" dropdown button functionality"""

        input_option = '2'
        sleep(5)
        self.driver.find_element_by_xpath("//div[contains(@class, 'ui-select-match')]").click()
        sleep(5)
        record_page_option = self.driver.find_element_by_xpath("//*[@id='ui-select-choices-row-{}-']/a/div".format(input_option))
        record_per_page_count = record_page_option.text
        record_page_option.click()
        with capsys.disabled():
            print(record_per_page_count)
        
        sleep(5)

        record_page_count = len(self.driver.find_elements_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[1]/tbody/tr"))
        table_row_count = str(record_page_count)
        with capsys.disabled():
            print(table_row_count)

        assert record_per_page_count >= table_row_count

        self.driver.close()

class TestOtherDeductionRecord(Setup):
    def test_other_dedecution_table_record(self):
        """Check "Table Record" functionality """

        sleep(3)
        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        add_earnings_type = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[1]/a")
        is_add_earnings_type_displays = add_earnings_type.is_displayed()

        assert is_add_earnings_type_displays == True

        self.driver.close()

    def test_other_dedecution_clicking_add_other_deductions_type_button_under_table_record(self, capsys):
        """Check "ADD Earnings Type" button functionality under "Record Table"."""

        sleep(5)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        add_other_dedictions_type_button = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[1]/a")
        is_add_earnings_type_displays = add_other_dedictions_type_button.is_displayed()
        add_other_dedictions_type_button.click()

        assert is_add_earnings_type_displays == True

        sleep(5)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            with capsys.disabled():
                print(self.driver.current_url)

        expected_payment_list_url = "https://yp.yahshuasupport.com/settings/payments/miscellaneous/#other_deductions"
        actual_payment_list_url = self.driver.current_url
        
        assert expected_payment_list_url == actual_payment_list_url
        self.driver.close()

    def test_other_dedecution_create_button_under_table_record(self):
        """Check "Create" button functionality under "Record Table".""" 

        input_deduction_type = "Personal Loan"

        sleep(3)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        create_button = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[2]/button")
        create_button.click()

        sleep(3)

        other_deduction_type = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[2]/div[1]/a/span[1]")
        other_deduction_type.click()

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_deduction_type))
        select_option.click()

        sleep(3)

        total_amount = self.driver.find_element(By.ID, 'otherdeduction_amount_select')
        total_amount.send_keys("500")

        sleep(3)

        date_input = self.driver.find_element(By.XPATH , "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[1]/p/input")
        date_input.clear()
        date_input.send_keys("08/18/2022")
        check_date_input = date_input.get_attribute('value')
        assert check_date_input == "08/18/2022"

        input_remarks = self.driver.find_element(By.XPATH , "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[4]/textarea")
        input_remarks.send_keys("Automated Testing Creating other Deduction")

        sleep(3)

        save_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[6]/div/button")
        save_button.click()

        sleep(0.5)

        expected_text = 'Other Deductions successfully added.'
        success_message = self.driver.find_element_by_xpath("//*[@aria-label = 'Other Deductions successfully added.']")
        actual_text = success_message.text

        assert expected_text == actual_text , "Check if the record is already created."

        sleep(3)

        self.driver.close()

    def test_other_dedecution_edit_button_under_table_record(self):
        """Check response "Edit functionality under "Record Table".""" 

        sleep(3)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        sleep(3)

        deduction_record = self.driver.find_element(By.XPATH ,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[5]/table[1]/tbody/tr/td")
        deduction_record.click()

        sleep(5)

        total_amount = self.driver.find_element(By.XPATH,'//*[@id="otherdeduction_amount_selected_2022-08-17"]')
        total_amount.click()
        total_amount.clear()
        total_amount.send_keys("5000")

        save_button = self.driver.find_element(By.XPATH, "//*[@id='otherdeduction_save_button_2022-08-17']")
        save_button.click()

        sleep(0.5)

        expected_text = 'Other Deductions successfully edited.'
        success_message = self.driver.find_element_by_xpath("//*[@aria-label = 'Other Deductions successfully edited.']")
        actual_text = success_message.text

        expected_text == actual_text

        self.driver.close()

    def test_other_dedecution_delete_button_under_table_record(self):
        """Check "Create" button functionality under "Record Table".""" 

        sleep(3)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        sleep(5)

        deduction_record = self.driver.find_element(By.XPATH ,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[5]/table[1]/tbody/tr/td")
        deduction_record.click()

        sleep(3)

        delete_icon = self.driver.find_element(By.XPATH ,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td/div[5]/button[2]")
        delete_icon.click()

        sleep(5)

        Confirmation.click_confirm_yes(self)
        sleep(0.5)

        expected_text = 'Other Deductions successfully deleted.'
        success_message = self.driver.find_element_by_xpath("//*[@aria-label = 'Other Deductions successfully deleted.']")
        actual_text = success_message.text

        assert expected_text == actual_text

        self.driver.close()

