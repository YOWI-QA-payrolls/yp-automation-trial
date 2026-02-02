import pytest
from pytest import skip
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from request_cookies import add_cookies
# from utils.set_site import Login
from utils.confirmation import Confirmation
from utils.create_leave import CreateLeave
from utils.date import Date
from utils.dropdown import Dropdown
from utils.filters import AdvanceFilter
from utils.get_data import EmployeeModuleTable, EmployeeTable, EmployeeTableLeave
from utils.pagination import TablePagination
from utils.record_per_page import RecordsPerPage
from utils.rightclick import RightClick

from utils.setup import driversetup, main_url
from utils.search import Search
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from itertools import chain
from utils.table import TableRecord

class Setup():

    def setup_method(self): 
        """Run this setup for this test class."""
        
        self.driver = driversetup()
        self.driver.maximize_window()
        target_url = main_url()
        url = "%s/dashboard/" % (target_url)
        self.driver.get(url)

        self.driver.delete_all_cookies()
        add_cookies(self)
        self.driver.refresh()
        
        self.driver.get("%s/requests/leaves/main_page/" % (target_url))
        sleep(5)
        
    def teardown_method(self, method):
        self.driver.quit()

class TestSearch(Setup):

    #@pytest.mark.skip(reason="passed")
    def test_search_entering_existing_data_lowercase(self, capsys, leave_table_name):
        """Test Search functionality inputting lowercase in the searchbox"""
        
        input_data = "wilde"
        
        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data

        sleep(5)
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys, leave_table_name, column_number='3')
        
        assert table_record_results == True , "It didn't display the existing data related to the inputted data."

    #@pytest.mark.skip(reason="passed")
    def test_search_entering_existing_data_uppercase(self, capsys,leave_table_name):
        """Test Search functionality inputting uppercase in the searchbox"""
        
        input_data = "WILDE"
        
        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data

        sleep(5)
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys,leave_table_name, column_number='3')
        
        assert table_record_results == True , "It didn't display the existing data related to the inputted data."

    # #@pytest.mark.skip(reason="passed")
    def test_entering_existing_employee_fullname(self, capsys,leave_table_name):
        """Test Search functionality entering employee fullname in the searchbox"""

        input_data = "sample1,sample1a v."
        
        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data

        sleep(5)
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys,leave_table_name, column_number='3')
        assert table_record_results[0] == input_data , "It didn't display the existing data related to the inputted data."
    

    # #@pytest.mark.skip(reason="passed")
    def test_entering_special_characters_specifically_parentheses_and_dash(self, capsys,leave_table_name):
        """Test Search functionality entering special characters in the searchbox"""

        input_data=")(-"

        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data

        sleep(5)
        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys,leave_table_name, column_number='3')
        assert table_record_results == True, "Special characters should be ignored since CHAPA No. and Employee Name are the only fileds which is searchable."
    

    def test_search_entering_valid_Chapa_or_Employee_ID(self, capsys,leave_table_name):
        """Test Search functionality entering chapa or employee ID in the searchbox"""

        input_data="1013"

        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data
        sleep(5)

        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys, leave_table_name, column_number='3')
        assert table_record_results == True ,"It didn't display existing data related to the inputted data."

    #@pytest.mark.skip(reason="passed")
    def test_search_entering_partial_valid_Chapa_or_Employee_ID(self, capsys, leave_table_name):
        """Test Search functionality entering partial valid chapa in the searchbox"""

        input_data = "785"

        self.driver.implicitly_wait(15)
        actual_data = Search.box_function(self, input_data)
        assert input_data == actual_data

        is_search_icon_clicked = Search.click_icon_button(self)
        assert is_search_icon_clicked == True

        table_record_results = Search.check_all_search_results(self, input_data, capsys, leave_table_name, column_number='3')
        assert table_record_results == True 

class TestAdvanceFilter(Setup):

    def test_choosing_advance_filter_status(self,capsys, leave_table_name):
        """Test Search functionality choosing "Recommended" option on Advance Filter's Status."""

        sleep(3)
        AdvanceFilter.button_click(self)
        sleep(3)

        status_selection = 'Recommended'
        status_field_data = AdvanceFilter.select_status_leave(self, status_selection, filter_no = 'ui-select-choices-3')
        assert status_field_data == status_selection

        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_leave_employee_status_recommended(self, page_count, leave_table_name)

        extracted_list = list(chain(*employee_list))
        with capsys.disabled():
            print(extracted_list)

        assert_lists = any(word in "Recommended" for word in extracted_list)
        assert assert_lists == True

    def test_choosing_advance_filter_type_of_leave(self, capsys):
        """Test Advanced Filter functionality choosing "Deductible against pay" option on Advance Filter's "Type of Leave"."""

        input_data= 'Vacation'

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_type_of_leave(self,input_data,filter_no='ui-select-choices-4')
        AdvanceFilter.click_leave_search_button(self)
        sleep(5)
        page_count = TableRecord.get_page_count(self)
            
        employee_list = []
        for page in range(page_count):
            table_row_count_request =  self.driver.find_elements(By.XPATH, "//*[@id='table']/tbody/tr/td[4]")

            if table_row_count_request == 0:
                raise Exception("the record is empty, no record to select")
            self.driver.implicitly_wait(20)
            for row in table_row_count_request:     
                table_row = row.text
                employee_list.append(table_row)

            TablePagination.next_button(self)

        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)
            print(employee_list)

        assert_lists = any(item in input_data for item in no_duplicate_employee_request)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_payroll_status_selecting_normal(self, capsys, leave_table_name):
        #Advance Filter
        """Test Search functionality choosing "Normal" option on Advance Filter's "Payroll Status"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'filters.payroll_status')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Normal")
        with capsys.disabled():
            print(employee_name)
            print(employee_list)

        assert_lists = any(word in employee_name for word in employee_list)

        assert assert_lists == True

    #@pytest.mark.skip(reason="no existing file")
    def test_choosing_advance_filter_payroll_status_selecting_confidential(self, capsys, leave_table_name):
        """Test Search functionality choosing "Confidential" option on Advance Filter's "Payroll Status"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_payroll_status(self,input_data="Confidential",request_type = 'filters.payroll_status')
        AdvanceFilter.click_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Confidential")
        with capsys.disabled():
            print(employee_name)
            print(employee_list)

        assert_lists = any(word in employee_name for word in employee_list)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_location(self, capsys, leave_table_name):
        """Test Search functionality choosing "CEBU" option on Advance Filter's "Location"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_location(self,input_location="CEBU",filter_no='ui-select-choices-6')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)
        sleep(3)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        # #Employee Module
        input_location = "CEBU"
        employee_name = EmployeeModuleTable.get_employee_location(self, capsys, input_location)
        with capsys.disabled():
            print(employee_name)

        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_location_direct(self, capsys, leave_table_name):
        """Test Search functionality choosing "DIRECT" option on Advance Filter's "Location"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_location(self,input_location="DIRECT",filter_no='ui-select-choices-6')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)
        sleep(3)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(employee_list)
            print(page_count)
            print(no_duplicate_employee_request)

        #Employee Module
        input_location = "DIRECT"
        employee_name = EmployeeModuleTable.get_employee_location(self, capsys, input_location)

        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed") 
    def test_choosing_advance_filter_division(self, capsys, leave_table_name):
        """Test Search functionality choosing "Division 2" option on Advance Filter's "Division"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_division(self,input_division="Division 2",filter_no='ui-select-choices-7')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)
        sleep(5)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(employee_list)
            print(page_count)
            print(no_duplicate_employee_request)

        #Division Module
        input_division="Division 2"
        employee_name = EmployeeModuleTable.get_employee_division(self, capsys, input_division)

        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_department(self, capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "Department"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_department(self, input_department = "Operations", filter_no='ui-select-choices-8')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)
        sleep(3)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        #Department Module
        input_department="Operations"
        employee_name = EmployeeModuleTable.get_employee_department(self, capsys,input_department)

        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_section(self, capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "Section"."""

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_section(self,input_section="Accounts Payable",filter_no='ui-select-choices-9')
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)
        sleep(3)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        #Section Module
        input_section="Accounts Payable"
        employee_name = EmployeeModuleTable.get_employee_section(self, capsys,input_section)

        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    @pytest.mark.skip(reason="no feature")
    def test_choosing_advance_filter_employee(self, capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "employee"."""

        AdvanceFilter.button_click(self)

        AdvanceFilter.select_employee(self,input_employee="10010 - Ackerman, Levi R.")
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        #Employee Module
        input_employee="10010 - Ackerman, Levi R."
        employee_name = EmployeeModuleTable.get_employee(self, capsys, input_employee)
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="no feature")
    def test_choosing_advance_filter_job_level(self,capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "Job Level"."""

        self.driver.implicitly_wait(10)
        AdvanceFilter.button_click(self)
        
        sleep(5)
        AdvanceFilter.select_job_level(self,input_job_level="Monthlies",request_type= 'filters.job_level')
        AdvanceFilter.click_leave_search_button(self)

        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        input_job_level="Monthlies"
        employee_name = EmployeeModuleTable.get_job_level(self,input_job_level)
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    # #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_selecting_multiple_location(self, capsys, leave_table_name):
        """Test Search functionality choosing "Cebu" and "Direct" option on Advance Filter's "Location"."""

        AdvanceFilter.button_click(self)
        
        multiple_location_selection = ["CEBU","DIRECT"]
        for input_location in multiple_location_selection:
            AdvanceFilter.select_location(self,input_location ,filter_no='ui-select-choices-6')
        
        AdvanceFilter.click_leave_search_button(self)
        sleep(5)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        
        employee_name = EmployeeModuleTable.get_multiple_employee_location(self, capsys, multiple_location_selection)
        with capsys.disabled():
            print(no_duplicate_employee_request)
            print(employee_name)

        
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_selecting_multiple_division(self,capsys, leave_table_name):
        """Test Search functionality choosing "Payroll" option on Advance Filter's "Division"."""

        AdvanceFilter.button_click(self)
        
        multiple_division_selection = ["Division 2","Division 1"]
        for input_division in multiple_division_selection:
            AdvanceFilter.select_division(self, input_division ,filter_no='ui-select-choices-7')
        
        AdvanceFilter.click_leave_search_button(self)
        sleep(5)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        employee_name = EmployeeModuleTable.get_multiple_employee_division(self,capsys, multiple_division_selection)
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    # #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_selecting_multiple_department(self, capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "Department"."""

        AdvanceFilter.button_click(self)
        
        multiple_department_selection = ["Operations","Direct Labor"]
        for input_department in multiple_department_selection:
            AdvanceFilter.select_department(self,input_department ,filter_no='ui-select-choices-8')
        
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        employee_name = EmployeeModuleTable.get_multiple_employee_department(self,capsys, multiple_department_selection)
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

    # #@pytest.mark.skip(reason="passed")
    def test_choosing_advance_filter_selecting_multiple_section(self, capsys, leave_table_name):
        """Test Search functionality choosing option on Advance Filter's "Section"."""

        AdvanceFilter.button_click(self)
        
        multiple_section_selection = ["Section 1","Accounts Payable"]
        for input_section in multiple_section_selection:
            AdvanceFilter.select_section(self,input_section ,filter_no='ui-select-choices-9')
        
        self.driver.implicitly_wait(10)
        AdvanceFilter.click_leave_search_button(self)
        sleep(3)
        page_count = TableRecord.get_page_count(self)

        employee_list = EmployeeTableLeave.get_employee_name(self, page_count, leave_table_name)
        no_duplicate_employee_request = list(dict.fromkeys(employee_list))
        with capsys.disabled():
            print(no_duplicate_employee_request)

        employee_name = EmployeeModuleTable.get_multiple_employee_section(self,capsys, multiple_section_selection)
        assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
        assert assert_lists == True

class TestRecordPerPage(Setup):

    @pytest.mark.skip(reason="passed , no documentation in testcase")
    def test_leave_records_per_page_clicking_dropdown(self, capsys):
        """Check results clicking "Records per page" drop-down."""

        input_option = '0'
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-select-match')]").click()
        sleep(10)
        record_page_option = self.driver.find_element(By.XPATH, "//*[@id='ui-select-choices-row-{}-']/a/div".format(input_option))
        record_per_page_display = record_page_option.is_displayed()
        with capsys.disabled():
            print(record_per_page_display)
        
        assert record_per_page_display == True
    

    # #@pytest.mark.skip(reason="passed")
    def test_leave_records_per_page_inputting_invalid_data(self,capsys, leave_table_name):
        """Check results inputing invalid data in "Records per page" drop-down."""
        
        self.driver.implicitly_wait(50)
        input_data = 'ABc123'
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-select-match')]").click()
        records_per_page_input = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[6]/div/input[1]")
        records_per_page_input.send_keys(input_data)
        records_per_page_input.send_keys(Keys.ENTER)

        sleep(20)
        record_page_count = self.driver.find_elements(By.XPATH, "//*[@id='"+(leave_table_name)+"']/tbody/tr")
        table_row_count = len(record_page_count)
        with capsys.disabled():
            print(table_row_count)

        assert table_row_count == 5
    

    @pytest.mark.skip(reason="passed , no documentation in testcase")
    def test_leave_records_per_page_changing_employees_per_page(self, capsys, leave_table_name):
        """Check results changing employees per page."""
        
        input_option = '0'

        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'ui-select-match')]").click()
        record_page_option = self.driver.find_element(By.XPATH,"//*[@id='ui-select-choices-row-{}-']/a/div".format(input_option))
        record_per_page_count = record_page_option.text
        record_page_option.click()
        with capsys.disabled():
            print(record_per_page_count)
        
        sleep(10)

        record_page_count = len(self.driver.find_elements(By.XPATH, "//*[@id='"+(leave_table_name)+"']/tbody/tr"))
        table_row_count = str(record_page_count)
        with capsys.disabled():
            print(table_row_count)

        assert record_per_page_count >= table_row_count
    

class TestCreateButton(Setup):
    def test_create_button(self):
        """Check response on clicking "Create" button under "leave" tab."""

        self.driver.implicitly_wait(10)
        create_button = self.driver.find_element(By.XPATH,"//button[contains(@class, 'btn-danger')]")
        create_button.click()
        sleep(3)

        add_leave_request_form = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]").is_displayed()
        assert add_leave_request_form  == True

class TestCreateLeaveRequest(Setup):

    input_data = "111 - QA, Employee 1"

    # #@pytest.mark.skip(reason="passed")
    def test_create_leave_wholeday(self):
        """Check results on requesting leave request wholeday."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_whole_day_radio_button(self)
        
        sleep(3)
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='09/20/2022',request_type='leave')
        sleep(2)
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='09/20/2022', request_type='leave')

        CreateLeave.input_reason_field(self, input_data = 'Automated wholeday leave testing', module = 'leave')

        sleep(5)
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')

        CreateLeave.click_leave_submit_button(self)

        sleep(3)

        expected_confirmation_dialog = "Continue?"

        dialog_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/h2")
        dialog_actual_text = dialog_box.text

        assert expected_confirmation_dialog == dialog_actual_text
        Confirmation.click_confirm_yes(self)
    
        sleep(0.5)

        expected_text =  "Leave request successfully submitted."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'Leave request successfully submitted.']")
        actual_text = success_message.text

        assert expected_text == actual_text       

    def test_create_leave_halfday(self):
        """Check results on requesting leave request wholeday."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_half_day_radio_button(self)

        sleep(5)
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        
        Date.create_request_popup_date_using_ngmodel(self, input_data='10/03/2022',request_type='leave')

        CreateLeave.input_time_from_hour(self,input_data = '8')
        CreateLeave.input_time_from_minute(self,input_data = '00')
        CreateLeave.input_time_to_hour(self,input_data = '11' )
        CreateLeave.input_time_to_minute(self,input_data = '00')

        CreateLeave.input_reason_field(self, input_data = 'Automated halfday leave testing', module = 'leave')

        CreateLeave.click_leave_submit_button(self)

        sleep(3)

        expected_confirmation_dialog = "Continue?"

        dialog_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/h2")
        dialog_actual_text = dialog_box.text

        assert expected_confirmation_dialog == dialog_actual_text
        Confirmation.click_confirm_yes(self)
        sleep(0.5)

        expected_text =  "Leave request successfully submitted."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'Leave request successfully submitted.']")
        actual_text = success_message.text

        assert expected_text == actual_text       

    def test_create_leave_wholeday_insufficient_credit(self):
        """Check results on creating Whole day leave request with insufficient leave credits."""
        
        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_whole_day_radio_button(self)
        
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Paternity')
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='09/22/2022',request_type='leave')
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='09/22/2022', request_type='leave')

        CreateLeave.input_reason_field(self, input_data = 'Automated wholeday leave testing', module = 'leave')

        CreateLeave.click_leave_submit_button(self)
        Confirmation.click_confirm_yes(self)

        expected_text =  "Not enough Paternity leave."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'Not enough Paternity leave.']")
        actual_text = success_message.text

        assert expected_text == actual_text       

    def test_create_leave_halfday_insufficient_credit(self):
        """Check results on creating Half day leave request with insufficient leave credits."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_half_day_radio_button(self)

        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Paternity')
      
        Date.create_request_popup_date_using_ngmodel(self, input_data='09/23/2022',request_type='leave')

        CreateLeave.input_time_from_hour(self,input_data = '8')
        CreateLeave.input_time_from_minute(self,input_data = '00')
        CreateLeave.input_time_to_hour(self,input_data = '11' )
        CreateLeave.input_time_to_minute(self,input_data = '00')
        
        CreateLeave.input_reason_field(self, input_data = 'Automated halfday leave testing', module = 'leave')

        CreateLeave.click_leave_submit_button(self)
        Confirmation.click_confirm_yes(self)

        expected_text =  "Not enough Paternity leave."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'Not enough Paternity leave.']")
        actual_text = success_message.text

        assert expected_text == actual_text       

    def test_create_leave_invalid_date_from_greater_than_date_to(self):
        """Check results on creating Whole day leave request with invalid "Date From" and "Date To".  ("Date From" is greater than "Date To")"""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_whole_day_radio_button(self)
        
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='10/21/2022',request_type='leave')
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='10/20/2022', request_type='leave')

        CreateLeave.input_reason_field(self, input_data = 'Automated wholeday leave testing', module = 'leave')

        CreateLeave.click_leave_submit_button(self)
        Confirmation.click_confirm_yes(self)

        expected_text =  "Not enough Sick Leave leave."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'Not enough Sick Leave leave.']")
        actual_text = success_message.text

        assert expected_text == actual_text       

    def test_create_leave_wholeday_no_reason(self):
        """Check results on creating Whole day leave request with no reason inputted on "Reason" field. """

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_whole_day_radio_button(self)
        
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='11/20/2022',request_type='leave')
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='11/20/2022', request_type='leave')

        CreateLeave.click_leave_submit_button(self)

        submit_button_status = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]").is_displayed()
        assert submit_button_status == True

    def test_create_leave_halfday_no_reason(self):
        """Check results on creating Whole day leave request with no reason inputted on "Reason" field. """
        
        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_selection = Dropdown.select_dropdown_option(self, self.input_data)
        CreateLeave.click_half_day_radio_button(self)

        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
      
        Date.create_request_popup_date_using_ngmodel(self, input_data='11/23/2022',request_type='leave')

        CreateLeave.input_time_from_hour(self,input_data = '8')
        CreateLeave.input_time_from_minute(self,input_data = '00')
        CreateLeave.input_time_to_hour(self,input_data = '11' )
        CreateLeave.input_time_to_minute(self,input_data = '00')

        CreateLeave.click_leave_submit_button(self)

        submit_button_status = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]").is_displayed()
        assert submit_button_status == True

    def test_create_leave_wholeday_on_restday(self):
        """Check results on requesting wholeday leave request on employee restday."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_input = CreateLeave.input_employee(self, employee = "111 - QA, Employee 1")
        CreateLeave.click_whole_day_radio_button(self)
        
        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='10/02/2022',request_type='leave')
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='10/02/2022', request_type='leave')

        expected_text =  "(Number of days leave exclude Holiday and Restday)"
        success_message =  self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[8]/small")
        actual_text = success_message.text

        assert expected_text == actual_text  

    def test_create_leave_halfday_on_restday(self):
        """Check results on requesting halfday leave request ."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_input = CreateLeave.input_employee(self, employee = "111 - QA, Employee 1")
        CreateLeave.click_half_day_radio_button(self)
      
        Date.create_request_popup_date_using_ngmodel(self, input_data='10/09/2022',request_type='leave')

        CreateLeave.input_time_from_hour(self,input_data = '8')
        CreateLeave.input_time_from_minute(self,input_data = '00')
        CreateLeave.input_time_to_hour(self,input_data = '11' )
        CreateLeave.input_time_to_minute(self,input_data = '00')

        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')

        sleep(0.5)

        expected_text =  "This leave application falls on a restday or holiday. Please change the selected date."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'This leave application falls on a restday or holiday. Please change the selected date.']")
        actual_text = success_message.text

        assert expected_text == actual_text  
    

    def test_create_leave_wholeday_on_holiday(self):
        """Check results on requesting wholeday leave request ."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_input = CreateLeave.input_employee(self, employee = "111 - QA, Employee 1")
        CreateLeave.click_whole_day_radio_button(self)
        
        Date.create_request_popup_date_from_using_ngmodel(self, input_data='10/23/2022',request_type='leave')
        Date.create_request_popup_date_to_using_ngmodel(self, input_data='10/23/2022', request_type='leave')

        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        CreateLeave.input_reason_field(self, input_data = 'Automated wholeday leave testing', module = 'leave')

        expected_text =  "(Number of days leave exclude Holiday and Restday)"
        success_message =  self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[8]/small")
        actual_text = success_message.text

        assert expected_text == actual_text    

    def test_create_leave_halfday_on_holiday(self):
        """Check results on requesting halfday leave request ."""

        self.driver.implicitly_wait(15)
        CreateLeave.click_create_button(self)

        CreateLeave.click_employee_dropdown(self)
        employee_input = CreateLeave.input_employee(self, employee = "111 - QA, Employee 1")
        CreateLeave.click_half_day_radio_button(self)

        Date.create_request_popup_date_using_ngmodel(self, input_data='10/30/2022',request_type='leave')

        CreateLeave.input_time_from_hour(self,input_data = '8')
        CreateLeave.input_time_from_minute(self,input_data = '00')
        CreateLeave.input_time_to_hour(self,input_data = '11' )
        CreateLeave.input_time_to_minute(self,input_data = '00')

        CreateLeave.click_type_of_leave_dropdown(self)
        leave_type_selection = Dropdown.select_dropdown_option(self, input_data = 'Sick Leave')
        
        sleep(0.5)

        expected_text =  "This leave application falls on a restday or holiday. Please change the selected date."
        success_message =  self.driver.find_element(By.XPATH,"//*[@aria-label = 'This leave application falls on a restday or holiday. Please change the selected date.']")
        actual_text = success_message.text

        assert expected_text == actual_text  

class TestPagination(Setup):

    # @pytest.mark.skip(reason="passed")
    def test_leave_pagination_using_next_button(self, capsys):
        """Check results changing page using next button."""

        self.driver.implicitly_wait(30)
        next_button = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Next')]")
        next_button.click()

        page_number = self.driver.find_element(By.XPATH,"//*[@class = 'pagination-page ng-scope active']")
        page = int(page_number.text)
        
        assert page == 1 or 2

    #@pytest.mark.skip(reason="passed")
    def test_leave_pagination_using_page_number(self, capsys):
        """Check results changing page using page number."""

        self.driver.implicitly_wait(30)
        input_page_number = 1
        xpath_page_number = str(input_page_number + 1)
        page_number = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/pagination/div/div[3]/ul/li[{}]/a".format(xpath_page_number))
        self.driver.execute_script("arguments[0].click();",page_number)

        page_number = self.driver.find_element(By.XPATH,"//*[@class = 'pagination-page ng-scope active']")
        page = int(page_number.text)
        if (page) == 1:     
            with capsys.disabled():
                print('opens first page')
        if (page) == 2:
            with capsys.disabled():
                print('It opens second page')
        else:
            with capsys.disabled():
                print('pagination button is not visible yet')

        assert page == input_page_number
    

class TestRightClick(Setup):

    pytest.mark.skip(reason="passed")
    def test_leave_records_right_clicking_request(self, leave_table_name):
        """Check results right-clicking a request."""
        
        self.driver.implicitly_wait(10)
        RightClick.first_row_leave(self)
        right_click_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[3]/ul").is_displayed()
        
        assert right_click_option == True
        

    #@pytest.mark.skip(reason="passed")
    def test_leave_records_clicking_ViewLogs_option(self):
        """Check results clicking "View Logs" option."""
        
        self.driver.implicitly_wait(10)
        employee_name= "ALPAY, KEVIN GIO J."
        RightClick.user(self,employee_name)
        viewlog_button = self.driver.find_element_by_link_text(link_text='View Logs')
        viewlog_button.click()

        header_title = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[2]/div[1]/h2")
        daily_logs_page = header_title.is_displayed()
        assert daily_logs_page == True

        sleep(5)
        employee_selected = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(employee_name))
        employee_view_logs = employee_selected.text
        assert employee_view_logs == employee_name

    #@pytest.mark.skip(reason="passed") 
    def test_leave_records_clicking_Attach_option(self):
        """Check results clicking "Attach" option."""
        
        self.driver.implicitly_wait(10)
        RightClick.user(self,employee_name='ALPAY, KEVIN GIO J.')
        attach_button = self.driver.find_element_by_link_text(link_text='Attach')
        attach_button.click()

        sleep(5)
        
        attachment_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div")
        is_attachment_displays = attachment_modal.is_displayed()
        assert is_attachment_displays == True


    #@pytest.mark.skip(reason="passed")
    def test_leave_records_clicking_Cancel_option(self):
        """Check results clicking "Cancel" Request for leave option."""
        
        self.driver.implicitly_wait(10)
        RightClick.first_row_leave(self)
        cancel_button = self.driver.find_element_by_link_text(link_text='Cancel')
        cancel_button.click()
        
        cancel_request_modal = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
        is_request_modal_displays = cancel_request_modal.is_displayed()
        assert is_request_modal_displays == True

        specify_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
        specify_reason.send_keys('Automated Cancel Request for leave')

        confirm_button = self.driver.find_element_by_class_name("confirm")
        confirm_button.click()

        leave_succesfully_cancelled_dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
        is_success_dialog_box_appeared = leave_succesfully_cancelled_dialog_box.is_displayed()
        assert is_success_dialog_box_appeared  == True

    #@pytest.mark.skip(reason="passed")
    def test_leave_records_clicking_Delete_option(self):
        """Check results clicking "Delete" option."""
        
        self.driver.implicitly_wait(10)
        sleep(5)
        RightClick.first_row_leave(self)
        delete_button = self.driver.find_element_by_link_text(link_text='Delete')
        delete_button.click()
        sleep(2)

        delete_request_modal = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
        is_request_modal_displays = delete_request_modal.is_displayed()
        assert is_request_modal_displays == True

        specify_reason = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]/fieldset/input")
        specify_reason.send_keys('Automated Delete Request for Leave')

        confirm_button = self.driver.find_element_by_class_name("confirm")
        confirm_button.click()

        leave_succesfully_deleted_dialog_box = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
        is_deleted_dialog_box = leave_succesfully_deleted_dialog_box.is_displayed()
        assert is_deleted_dialog_box == True
    

class TestSort(Setup):
    #@pytest.mark.skip(reason="passed")
    def test_leave_sort_by_clicking_sort_icon(self, capsys, leave_table_name):
        """Check results clicking sort icon by Employee name column"""

        self.driver.implicitly_wait(10)
        requested_date_latest = self.driver.find_element(By.XPATH, "//*[@id='{}']/tbody/tr[11]/td[1]".format(leave_table_name))
        
        latest_date = requested_date_latest.text
        with capsys.disabled():
            print(latest_date)

        employee_sort_icon = self.driver.find_element(By.XPATH, "//*[@id='{}']/thead/tr/th[2]/a/i".format(leave_table_name))
        self.driver.execute_script("arguments[0].click();",employee_sort_icon)

        bottommost_date = self.driver.find_element(By.XPATH, "//*[@id='{}']/tbody/tr[11]/td[1]".format(leave_table_name))
        bottom_date = bottommost_date.text
        with capsys.disabled():
            print(bottom_date)

        assert bottom_date >= latest_date
