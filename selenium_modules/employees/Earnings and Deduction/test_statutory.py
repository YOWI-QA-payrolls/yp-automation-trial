import pytest
from time import sleep
from selenium import webdriver
from utils.set_site import LogIn
from selenium.webdriver.common.by import By
from utils.filters import AdvanceFilter
from utils.search import Search
from utils.table import TableRecord
from utils.pagination import TablePagination
from utils.confirmation import Confirmation
import requests

class Setup():
    """Earnings and Deduction Statutory test cases."""
    
    def setup_method(self): 
        """Run this setup for this test class."""
        self.driver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        url = "https://yp.yahshuasupport.com/dashboard/"
        self.driver.get(url)
          
        LogIn.login(self)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text("Employees").click()
        sleep(5)
        earnings_and_deduction_page = self.driver.find_element(By.XPATH, "//*[@id='employee_income_deduction']/a")
        self.driver.execute_script("arguments[0].click();",earnings_and_deduction_page)
          
        statutory_submodule = self.driver.find_element(By.XPATH, "//*[@id='employee_statutory']/a")
        self.driver.execute_script("arguments[0].click();",statutory_submodule)
          
    def teardown_method(self):
          self.driver.quit()  
          
          
class TestViewBy(Setup):  
          
    # @pytest.mark.skip(reason="PASSED")               
    def test_View_by_Dropdown_button(self):
        """Check response when clicking View by dropdown button under Statutory """
        
        self.driver.implicitly_wait(25)
        view_by_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a")
        view_by_button.click()
        
        view_by_dropdown_list = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/div/ul").is_displayed()
        assert view_by_dropdown_list == True
        
        self.driver.close()
        
    def test_Summary_View_by_Option(self,capsys):
        """Check response when clicking Summary options under View By"""
        
        view_by_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a")
        view_by_button.click()
        
        view_by_dropdown_list = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/div/ul").is_displayed()
        assert view_by_dropdown_list == True
        
        select_option = self.driver.find_element(By.XPATH, "//*[text()='Summary']")
        self.driver.execute_script("arguments[0].click();",select_option)
        
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-success")
        search_button.click()   
        
        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Summary"
            
        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True                                
        
        self.driver.close()
        
    def test_Detailed_View_by_Option(self,capsys):
        """Check response when clicking Detailed options under View By"""
        
        
        view_by_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a")
        view_by_button.click()
        
        view_by_dropdown_list = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/div/ul").is_displayed()
        assert view_by_dropdown_list == True
        
        select_option = self.driver.find_element(By.XPATH, "//*[text()='Detailed']")
        self.driver.execute_script("arguments[0].click();",select_option)
        
        search_button = self.driver.find_element(By.CLASS_NAME, "btn-success")
        search_button.click()
        
        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Detailed"
        
        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True
        
        self.driver.close()
        
        
class TestStatutoryType(Setup):
        
    # @pytest.mark.skip(reason="PASSED")
    def test_clicking_input_box(self):
        """Check response when clicking Input Box under Statutory"""
        
        statutory_type_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/ul/li/input")
        statutory_type_input_box.click()
        
        statutory_type_options = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/div").is_displayed()
        assert statutory_type_options == True
        
        self.driver.close()
        
    def test_clicking_select_all(self):
        """Check response when clicking Select All under Statutory"""
        
        select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/button[1]/i")
        select_all_button.click()
        
        statutory_type_options = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/ul/li/input")
        statutory_type_options.get_attribute('value')
        
        assert statutory_type_options != "All"
        
        self.driver.close()
        
    def test_clicking_deselect_all(self):
        """Check response when clicking Deselect All under Statutory"""
        
        select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/button[1]/i")
        select_all_button.click()
        
        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/button[2]/i")
        deselect_all_button.click()
        
        statutory_type_options = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/ul/li/input")
        return_default_value = statutory_type_options.get_attribute("placeholder")
        
        assert return_default_value == "All"
        
        self.driver.close()
        
    def test_clicking_specific_statutory_type(self):
        """Check response on clicking specific Statutory Type"""
        
        input_data = "PAGIBIG"
        
        statutory_type_input_box = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/ul/li/input")
        statutory_type_input_box.click()
        
        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
        select_option.click()
        
        search_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[7]/div/button")
        search_button.click()
        
        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True

        self.driver.close()
        
    def test_clicking_multiple_statutory_type(self):
        """Check response on clicking multiple Statutory Type""" 
        
        multiple_location_selection = ["PAGIBIG", "SSS", "PHILHEALTH"]
        
        for input_data in multiple_location_selection:
            regular_deduction_type = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[6]/div/ul/li/input")
            regular_deduction_type.click()

            select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_data))
            select_option.click()
        
        search_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[7]/div/button")
        search_button.click()
        
        sleep (5)
        
        summary_table_record = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]")
        is_table_record_displays = summary_table_record.is_displayed()

        assert is_table_record_displays == True

        self.driver.close()
        
        
class TestSearch(Setup):
        
    # @pytest.mark.skip(reason="PASSED")
    def test_searching_chapa_number(self,capsys):
        """Check response on searching Chapa number""" 
        
        input_data = "193"
          
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data
        
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True
        
        page_count = TableRecord.get_page_count(self)
        
        chapa_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_elements(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]/tbody/tr[1]/th[1]")
            
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
        """Check  "Statutory Type" buttons functionality""" 
        
        input_data = "EDGARDO"
          
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data
        
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        page_count = TableRecord.get_page_count(self)
        employee_name_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_elements(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]/tbody/tr[1]/th[2]")

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
        
        
class TestAdvanceFilter(Setup):
        
    def test_clicking_advance_filter(self):
        
        AdvanceFilter.button_click(self)
        
        advance_filter_popup = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div").is_displayed()
        AdvanceFilter.to_appear(self, advance_filter_popup)
        is_advance_filter_popup_displayed = advance_filter_popup.is_displayed()
        
        assert is_advance_filter_popup_displayed == True

        self.driver.close()
        
    def test_advance_filter_payroll_status_dropdown_button(self):
        """Check response "Payroll Status" dropdown button.""" 

        AdvanceFilter.button_click(self)

        advance_filter_popup = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div").is_displayed()
        assert advance_filter_popup == True

        AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'filter.payroll_status')
        
        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/abbr")
        x_icon.click()

        payroll_status_option = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/span[1]").text
        
        assert payroll_status_option =="ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_location(self):
        """Check response "Location" input box.""" 

        AdvanceFilter.button_click(self)
        
        input_location="CDO"
        AdvanceFilter.select_location(self,input_location,filter_no='ui-select-choices-4')
        
        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()

        select_all_button =  self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[1]")
        select_all_button.click()
        sleep(10)
        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[2]")
        deselect_all_button.click()

        location_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = location_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_division(self):
        """Check response "Division" input box.""" 

        AdvanceFilter.button_click(self)
        
        input_division="A"
        AdvanceFilter.select_division(self,input_division,filter_no='ui-select-choices-5')
        
        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()

        select_all_button =  self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[1]")
        select_all_button.click()
        sleep(10)
        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[2]")
        deselect_all_button.click()

        division_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = division_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_department(self):
        """Check response "Department" input box.""" 

        AdvanceFilter.button_click(self)

        input_department="Operations"
        AdvanceFilter.select_department(self,input_department,filter_no='ui-select-choices-6')
 
        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()


        select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[2]")
        deselect_all_button.click()

        department_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = department_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_section(self):
        """Check response "Section" input box.""" 

        AdvanceFilter.button_click(self)

        input_section="Section 1"
        AdvanceFilter.select_section(self,input_section,filter_no='ui-select-choices-7')
        
        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True
      
        x_icon.click()

        select_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[2]")
        deselect_all_button.click()

        location_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = location_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_job_level(self):
        """Check response "Section" input box.""" 

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_job_level(self,input_data="Monthlies",request_type= 'filter.job_level')

        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/abbr")
        x_icon.click()

    
        self.driver.close()
        
    def test_advance_filter_inputting_employee(self):
        """Check response "Job Level" input box.""" 

        AdvanceFilter.button_click(self)

        input_job_level="Monthlies"
        AdvanceFilter.select_job_level(self,input_job_level,request_type= 'filter.job_level')

        x_icon = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/abbr")
        x_icon.click()
        
        job_level_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()
        
    def test_advance_filter_inputting_search(self):
        """Check response "Search" button.""" 

    

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

        job_level_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text
    
        assert return_default_value == "ALL"

        employee_inputbox = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[1]")
        return_default_value = employee_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()
        
        
class TestCaretButton(Setup):
    
    # @pytest.mark.skip(reason="PASSED")    
    def test_statutory_caret_dropdown_button(self): 
        """Check response "Caret" dropdown button.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        assert is_caret_dropdown_displays == True
        
        self.driver.close()
        
    def test_statutory_caret_dropdown_export_button(self): 
        """Check response "Export" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        assert is_caret_dropdown_displays == True
        
        export_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[1]/a")
        export_selection.click()
        
        get_url = requests.get("https://yp.yahshuasupport.com/export/common_tables/employee_contributions?fields={%22employeeid%22:{%22display%22:%22Employee%20ID%22,%22sort%22:1,%22selected%22:true,%22default%22:true,%22uneditable%22:true,%22value%22:%22employeeid%22},%22lastname%22:{%22display%22:%22Last%20Name%22,%22sort%22:2,%22selected%22:true,%22value%22:%22lastname%22},%22firstname%22:{%22display%22:%22First%20Name%22,%22sort%22:3,%22selected%22:true,%22value%22:%22firstname%22},%22middlename%22:{%22display%22:%22Middle%20Name%22,%22sort%22:4,%22selected%22:true,%22value%22:%22middlename%22},%22total_employee_contributions%22:{%22display%22:%22Total%22,%22sort%22:6,%22selected%22:true,%22default%22:true,%22value%22:%22total_employee_contributions%22}}&filters=%7B%22employee%22%3Anull%2C%22records_per_page%22%3A10%2C%22contribution_type%22%3A%5B%5D%2C%22view_by%22%3A%22Detailed%22%2C%22pagination%22%3A%7B%22limit%22%3A10%2C%22current_page%22%3A1%2C%22total_records%22%3A225%2C%22total_pages%22%3A23%2C%22limit_options_orig%22%3A%5B20%2C50%2C100%2C150%5D%2C%22limit_options%22%3A%5B20%2C50%2C100%2C150%2C225%5D%7D%2C%22show_hide_column%22%3Atrue%2C%22show_inactive%22%3Afalse%2C%22typee%22%3A%22Contribution%22%2C%22type_ids%22%3A%5B%5D%7D&email=false&view_by=%22Detailed%22")

        assert 200 == get_url.status_code
        
        self.driver.close()
        
    def test_statutory_caret_dropdown_import_button(self): 
        """Check response "Import" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        assert is_caret_dropdown_displays == True
        
        import_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[2]/a")
        import_selection.click()
        
        get_url = requests.get("https://yp.yahshuasupport.com/settings/imports/#import_employee_contribution")

        assert 200 == get_url.status_code
        
        self.driver.close()
        
        
    def test_statutory_caret_dropdown_print_button(self): 
        """Check response "Print" dropdown option.""" 

        caret_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        is_caret_dropdown_displays = caret_dropdown.is_displayed()
        caret_dropdown.click()
        
        print_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[4]/a")
        print_selection.click()
        
        get_url = requests.get("https://yp.yahshuasupport.com/employees/additional_pay_and_deductions/contributions/prints/?filters=%7B%22employee%22:null,%22records_per_page%22:10,%22contribution_type%22:[],%22view_by%22:%22Detailed%22,%22pagination%22:%7B%22limit%22:10,%22current_page%22:1,%22total_records%22:225,%22total_pages%22:23,%22limit_options_orig%22:[20,50,100,150],%22limit_options%22:[20,50,100,150,225]%7D,%22show_hide_column%22:true,%22show_inactive%22:false,%22typee%22:%22Contribution%22,%22type_ids%22:[]%7D&columns=%7B%22employeeid%22:%7B%22display%22:%22Employee%20ID%22,%22sort%22:1,%22selected%22:true,%22default%22:true,%22uneditable%22:true,%22value%22:%22employeeid%22%7D,%22lastname%22:%7B%22display%22:%22Last%20Name%22,%22sort%22:2,%22selected%22:true,%22value%22:%22lastname%22%7D,%22firstname%22:%7B%22display%22:%22First%20Name%22,%22sort%22:3,%22selected%22:true,%22value%22:%22firstname%22%7D,%22middlename%22:%7B%22display%22:%22Middle%20Name%22,%22sort%22:4,%22selected%22:true,%22value%22:%22middlename%22%7D,%22total_employee_contributions%22:%7B%22display%22:%22Total%22,%22sort%22:6,%22selected%22:true,%22default%22:true,%22value%22:%22total_employee_contributions%22%7D%7D&contribution_view_by=Detailed&name=&inactive=false&print=yes")
        
        assert 200 == get_url.status_code
         
        self.driver.close()
        
    def test_statutory_caret_dropdown_delete_button(self): 
        """Check response "Delete" dropdown option.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()
        
        delete_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/ul/li[6]/a")
        delete_selection.click()
        
        notification_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[11]")
        assert notification_box == True
        
        yes_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[11]/div[7]/button[2]")
        yes_button.click()
        
        self.driver.close()
        
        
class TestRecordPerPage(Setup):
        
    def test_records_per_page_statutory(self,capsys):
        """Check response Records per Page dropdown button"""
        
        input_option = '2'
        sleep(5)
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-select-match')]").click()
        sleep(5)
        record_page_option = self.driver.find_element(By.XPATH, "//*[@id='ui-select-choices-row-{}-']/a/div".format(input_option))
        record_per_page_count = record_page_option.text
        record_page_option.click()
        with capsys.disabled():
            print(record_per_page_count)
            
        sleep(5)
        
        record_page_count = len(self.driver.find_elements(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[1]/tbody/tr"))
        table_row_count = str(record_page_count)
        with capsys.disabled():
            print(table_row_count)

        assert record_per_page_count >= table_row_count

        self.driver.close()
        
        
class TestStatutoryRecord(Setup):
              
    def test_table_record_detatils_statutory(self):
        """Check response Table Record details"""

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        add_statutory_type = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[1]/a")
        is_add_statutory_type_displays = add_statutory_type.is_displayed()

        assert is_add_statutory_type_displays == True

        self.driver.close()
        
    def test_statutory_clicking_add_statutory_type_button_under_table_record(self, capsys):
        """Check "ADD Statutory Type" button functionality under "Record Table"."""

        sleep(5)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[2]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        add_statutory_type_button = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[1]/a")
        is_add_statutory_type_displays = add_statutory_type_button.is_displayed()
        add_statutory_type_button.click()

        assert is_add_statutory_type_displays == True

        sleep(5)
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            with capsys.disabled():
                print(self.driver.current_url)

        expected_payment_list_url = "https://yp.yahshuasupport.com/settings/payments/miscellaneous/#statutory"
        actual_payment_list_url = self.driver.current_url
        
        assert expected_payment_list_url == actual_payment_list_url
        self.driver.close()
        
    def test_statutory_create_button_under_table_record(self):
        """Check "Create" button functionality under "Record Table".""" 

        input_statutory_type = "SSS"

        sleep(3)

        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        create_button = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[2]/button")
        create_button.click()
        
        statutory_type = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[1]/div[1]/a/span[1]")
        statutory_type.click()

        select_option = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(input_statutory_type))
        select_option.click()
        
        calculator_button = self.driver.find_element(By.XPATH, "//*[@id='calculate_new']")
        calculator_button.click()

        total_amount = self.driver.find_element(By.XPATH, "//*[@id='contribution_amount_select']").is_displayed
        
        assert total_amount == True
        
        save_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[4]/div/button[2]")
        save_button.click()
        
        expected_text = 'Employee Statutory successfully added.'
        success_message = self.driver.find_element(By.XPATH, "//*[@aria-label = 'Employee Statutory successfully added.']")
        actual_text = success_message.text

        assert expected_text == actual_text , "Check if the record is already created."

        self.driver.close()
        
    def test_statutory_delete_button_under_table_record(self):
        """Check "Create" button functionality under "Record Table".""" 
        
        first_row_employee_selection = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[10]/div/table[1]/tbody/tr[1]/th[2]/a")
        first_row_employee_selection.click()

        statutory_record = self.driver.find_element(By.XPATH , "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div[5]/table[1]/tbody/tr/td/div[3]")
        statutory_record.click()
        
        delete_icon = self.driver.find_element(By.XPATH , "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/table/tbody/tr/td/div[4]/div/button[5]")
        delete_icon.click()
        
        Confirmation.click_yes(self)
        sleep(0.5)

        expected_text = 'Employee Deduction successfully deleted.'
        success_message = self.driver.find_element(By.XPATH, "//*[@aria-label = 'Employee Deduction successfully deleted.']")
        actual_text = success_message.text

        assert expected_text == actual_text

        self.driver.close()
        
    
        
            
            