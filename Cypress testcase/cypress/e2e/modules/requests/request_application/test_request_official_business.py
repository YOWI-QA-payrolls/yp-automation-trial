from math import ceil
import pytest
from pytest import skip
from selenium import webdriver
from time import sleep, time
# from utils.set_site import Login
from request_cookies import add_cookies
from utils.create_officialbusiness import CreateOfficialBusiness
from utils.record_per_page import RecordsPerPage
from utils.rightclick import RightClick
from utils.search import Search
from utils.filters import AdvanceFilter
from utils.get_data import EmployeeTable
from utils.pagination import TablePagination
from utils.table import TableRecord
from utils.get_data import EmployeeModuleTable
from utils.date import Date
from utils.setup import driversetup, main_url

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

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

          self.driver.get("https://yp.yahshuasupport.com/requests/undertime_overtime_request/main_page/#/officialbusiness_request")
          sleep(10)
          
     def teardown_method(self, method):
          self.driver.quit()

class TestSearch(Setup):

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_existing_data_lowercase(self, capsys, official_business_table_name):
          """Test Search functionality inputting lowercase in the searchbox"""
          
          input_data = "monitoring"
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,official_business_table_name, column_number='3')
          
          assert table_record_results == True , "It didn't display the existing datas related to the inputted data."

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_existing_data_uppercase(self, capsys,official_business_table_name):
          """Test Search functionality inputting uppercase in the searchbox"""
          
          input_data = "MONITORING"
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,official_business_table_name, column_number='3')
          
          assert table_record_results == True , "It didn't display the existing datas related to the inputted data."

     # #@pytest.mark.skip(reason="passed")
     def test_entering_existing_employee_fullname(self, capsys,official_business_table_name):
          """Test Search functionality entering employee fullname in the searchbox"""

          input_data = "sample1,sample1a v."
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,official_business_table_name, column_number='3')
          assert table_record_results[0] == input_data , "It didn't display the existing datas related to the inputted data."
     

     # #@pytest.mark.skip(reason="passed")
     def test_entering_special_characters_specifically_parentheses_and_dash(self, capsys,official_business_table_name):
          """Test Search functionality entering special characters in the searchbox"""

          input_data=")(-"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,official_business_table_name, column_number='3')
          assert table_record_results == True, "Special characters should be ignored since CHAPA No. and Employee Name are the only fileds which is searchable."
     

     def test_search_entering_valid_Chapa_or_Employee_ID(self, capsys,official_business_table_name):
          """Test Search functionality entering chapa or employee ID in the searchbox"""

          input_data="1013"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data
          sleep(5)

          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys, official_business_table_name, column_number='3')
          assert table_record_results == True ,"It didn't display existing data related to the inputted data."

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_partial_valid_Chapa_or_Employee_ID(self, capsys, official_business_table_name):
          """Test Search functionality entering partial valid chapa in the searchbox"""

          input_data = "785"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys, official_business_table_name, column_number='3')
          assert table_record_results == True 

class TestAdvanceFilter(Setup):

     def test_choosing_advance_filter_status(self,capsys, official_business_table_name):
          """Test Search functionality choosing "Recommended" option on Advance Filter's Status."""

          AdvanceFilter.button_click(self)

          status_selection = 'Recommended'
          status_field_data = AdvanceFilter.select_status(self, status_selection, filter_no = 'ui-select-choices-1')
          assert status_field_data == status_selection

          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_status_recommended(self, page_count, official_business_table_name)
          with capsys.disabled():
               print(employee_list)

          assert_lists = any(word in "Recommended" for word in employee_list)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_payroll_status_selecting_normal(self, capsys, official_business_table_name):
          #Advance Filter
          """Test Search functionality choosing "Normal" option on Advance Filter's "Payroll Status"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'ob_request.payroll_status')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Normal")
          with capsys.disabled():
               print(employee_name)
               print(employee_list)

          assert_lists = any(word in employee_name for word in employee_list)

          assert assert_lists == True

     @pytest.mark.skip(reason="no existing file")
     def test_choosing_advance_filter_payroll_status_selecting_confidential(self, capsys, official_business_table_name):
          """Test Search functionality choosing "Confidential" option on Advance Filter's "Payroll Status"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_payroll_status(self,input_data="Confidential",request_type = 'ob_request.payroll_status')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Confidential")
          with capsys.disabled():
               print(employee_name)
               print(employee_list)

          assert_lists = any(word in employee_name for word in employee_list)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_location(self, capsys, official_business_table_name):
          """Test Search functionality choosing "CEBU" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_location(self,input_location="CEBU",filter_no='ui-select-choices-3')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
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
     def test_choosing_advance_filter_location_davao(self, capsys, official_business_table_name):
          """Test Search functionality choosing "Davao" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_location(self,input_location="DAVAO",filter_no='ui-select-choices-3')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Employee Module
          input_location = "DAVAO"
          employee_name = EmployeeModuleTable.get_employee_location(self, capsys, input_location)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed") 
     def test_choosing_advance_filter_division(self, capsys, official_business_table_name):
          """Test Search functionality choosing "Division 1" option on Advance Filter's "Division"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_division(self,input_division="Division 1",filter_no='ui-select-choices-4')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Division Module
          input_division="Division 1"
          employee_name = EmployeeModuleTable.get_employee_division(self, capsys, input_division)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_department(self, capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "Department"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_department(self, input_department = "Operations", filter_no='ui-select-choices-5')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Department Module
          input_department="Operations"
          employee_name = EmployeeModuleTable.get_employee_department(self, capsys,input_department)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_section(self, capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "Section"."""

          AdvanceFilter.button_click(self)
          
          AdvanceFilter.select_section(self,input_section="Accounts Payable",filter_no='ui-select-choices-6')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Section Module
          input_section="Accounts Payable"
          employee_name = EmployeeModuleTable.get_employee_section(self, capsys,input_section)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     @pytest.mark.skip(reason="no feature")
     def test_choosing_advance_filter_employee(self, capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "employee"."""

          AdvanceFilter.button_click(self)

          AdvanceFilter.select_employee(self,input_employee="10010 - Ackerman, Levi R.")
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Employee Module
          input_employee="10010 - Ackerman, Levi R."
          employee_name = EmployeeModuleTable.get_employee(self, capsys, input_employee)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     @pytest.mark.skip(reason="no feature")
     def test_choosing_advance_filter_job_level(self,capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "Job Level"."""

          self.driver.implicitly_wait(10)
          AdvanceFilter.button_click(self)
          
          sleep(5)
          AdvanceFilter.select_job_level(self,input_job_level="Monthlies",request_type= 'restday_request.job_level')
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          input_job_level="Monthlies"
          employee_name = EmployeeModuleTable.get_job_level(self,input_job_level)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_location(self, capsys, official_business_table_name):
          """Test Search functionality choosing "Davao" and "Laguna" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          
          multiple_location_selection = ["DAVAO","LAGUNA"]
          for input_location in multiple_location_selection:
               AdvanceFilter.select_location(self,input_location ,filter_no='ui-select-choices-3')
          
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          
          employee_name = EmployeeModuleTable.get_multiple_employee_location(self, capsys, multiple_location_selection)
          with capsys.disabled():
               print(no_duplicate_employee_request)
               print(employee_name)

          
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_division(self,capsys, official_business_table_name):
          """Test Search functionality choosing "Payroll" option on Advance Filter's "Division"."""

          AdvanceFilter.button_click(self)
          
          multiple_division_selection = ["Division 2","Division 1"]
          for input_division in multiple_division_selection:
               AdvanceFilter.select_division(self, input_division ,filter_no='ui-select-choices-4')
          
          AdvanceFilter.click_search_button(self)
          sleep(5)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_division(self,capsys, multiple_division_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_department(self, capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "Department"."""

          AdvanceFilter.button_click(self)
          
          multiple_department_selection = ["Operations","Direct Labor"]
          for input_department in multiple_department_selection:
               AdvanceFilter.select_department(self,input_department ,filter_no='ui-select-choices-5')
          
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_department(self,capsys, multiple_department_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_section(self, capsys, official_business_table_name):
          """Test Search functionality choosing option on Advance Filter's "Section"."""

          AdvanceFilter.button_click(self)
          
          multiple_section_selection = ["Section 1","Accounts Payable"]
          for input_section in multiple_section_selection:
               AdvanceFilter.select_section(self,input_section ,filter_no='ui-select-choices-6')
          
          self.driver.implicitly_wait(10)
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, official_business_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_section(self,capsys, multiple_section_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

class TestCreateOfficialBusinessRequest(Setup):

     employee = "333 - QA, Employee 3"

     #@pytest.mark.skip(reason="passed")
     def test_create_business_on_scheduled_workday(self):
          """Check results on requesting official business request on schdeduled workday."""

          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)

          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)

          CreateOfficialBusiness.click_wholeday_button(self)

          Date.create_request_popup_date_from_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')
          Date.create_request_popup_date_to_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')

          reason = 'Automated official business testing'
          input_reason_data = CreateOfficialBusiness.input_reason(self, reason)
          assert reason == input_reason_data

          CreateOfficialBusiness.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateOfficialBusiness.click_confirm_button(self)
          
          expected_text = 'Official business request successfully submitted.'
          success_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Official business request successfully submitted.']")
          actual_text = success_message.text
          assert expected_text == actual_text, "Requested date is not in the list of restdays. Please check."

          #Delete record
          self.driver.implicitly_wait(10)
          sleep(5)

          employee_name = "QA, Employee 3"
          RightClick.user(self,employee_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          delete_reason.send_keys('Automated Testing')

          confirm_button = self.driver.find_element(By.CLASS_NAME, "confirm")
          confirm_button.click()

          ok_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/div[7]/button[2]")
          ok_button.click()
     
     def test_create_business_requesting_hours(self):
          """Check results on requesting official business hours."""

          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)

          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)

          CreateOfficialBusiness.click_hours_button(self)

          date = "09/19/2022"
          input_date_data = CreateOfficialBusiness.input_date(self, date)
          assert date == input_date_data

          hour = '8'
          minute = '00' 
          input_hour_data , input_minute_data = CreateOfficialBusiness.input_time_from(self, hour, minute)
          assert hour == input_hour_data
          assert minute == input_minute_data

          sleep(3)

          hour = '12'
          minute = '00' 
          input_hour_data , input_minute_data = CreateOfficialBusiness.input_time_to(self, hour, minute)
          assert hour == input_hour_data
          assert minute == input_minute_data

          sleep(3)

          reason = 'Automated official business testing'
          input_reason_data = CreateOfficialBusiness.input_reason(self, reason)
          assert reason == input_reason_data

          CreateOfficialBusiness.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateOfficialBusiness.click_confirm_button(self)
          
          expected_text = 'Official business request successfully submitted.'
          success_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Official business request successfully submitted.']")
          actual_text = success_message.text
          assert expected_text == actual_text, "Requested date is not in the list of restdays. Please check."

          #Delete record
          self.driver.implicitly_wait(10)
          sleep(5)

          employee_name = "QA, Employee 3"
          RightClick.user(self,employee_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          delete_reason.send_keys('Automated Testing')

          confirm_button = self.driver.find_element(By.CLASS_NAME, "confirm")
          confirm_button.click()

          ok_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/div[7]/button[2]")
          ok_button.click()

     #@pytest.mark.skip(reason="passed")
     def test_create_official_business_invalid_date(self):
          """Check results on requesting restday request with invalid date."""

          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)

          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)

          CreateOfficialBusiness.click_wholeday_button(self)
          sleep(2)

          Date.create_request_popup_date_from_using_ngmodel(self, input_data='05/27/2022', request_type='official_business')
          Date.create_request_popup_date_to_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')

          reason = 'Automated official business testing Invalid date but autocorrect date.'
          input_reason_data = CreateOfficialBusiness.input_reason(self, reason)
          assert reason == input_reason_data

          CreateOfficialBusiness.click_submit_button(self)

          sleep(3)
          
          CreateOfficialBusiness.click_confirm_button(self)

          expected_text = 'Official business request successfully submitted.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Official business request successfully submitted.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text," It didn't autocorrect the date so it has an error"

     #@pytest.mark.skip(reason="passed")
     def test_create_official_business_incomplete_reasonfield(self):
          """Check results on requesting business request with incomplete fields(Reason field)."""

          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)
          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)
          sleep(5)
          CreateOfficialBusiness.click_wholeday_button(self)

          Date.create_request_popup_date_from_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')
          Date.create_request_popup_date_to_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')

          sleep(2)
          CreateOfficialBusiness.click_submit_button(self)

          expected_text = 'Please indicate a Reason.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Please indicate a Reason.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     
     #@pytest.mark.skip(reason="passed")
     def test_create_official_business_incomplete_hours_field(self):
          """Check results on requesting official busines request with incomplete fields(Hours field)."""

          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)
          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)
          sleep(3)
          CreateOfficialBusiness.click_hours_button(self)

          reason = 'Automated official busines testing RD'
          input_reason_data = CreateOfficialBusiness.input_reason(self, reason)
          assert reason == input_reason_data
          sleep(2)
          CreateOfficialBusiness.click_submit_button(self)

          expected_text = 'Please indicate Time From.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Please indicate Time From.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     
     #@pytest.mark.skip(reason="passed")
     def test_create_official_business_incomplete_employee_field(self):
          """Check results on requesting business request with incomplete fields(Employee Field)."""
          
          self.driver.implicitly_wait(25)
          CreateOfficialBusiness.click_create_button(self)
          sleep(3)
          CreateOfficialBusiness.click_submit_button(self)

          sleep(3)
          modal_window = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]")
          is_modal_window_dispalayed = modal_window.is_displayed()

          assert is_modal_window_dispalayed == True
     
     # @pytest.mark.skip(reason="passed")
     def test_create_official_buiness_duplicate_request(self):
          """Check results on requesting official buiness request with already requested date(Duplicate request)."""

          self.driver.implicitly_wait(25)
          
          CreateOfficialBusiness.click_create_button(self)
          sleep(5)
          employee_input_data = CreateOfficialBusiness.input_employee(self, self.employee)

          CreateOfficialBusiness.click_wholeday_button(self)
          sleep(2)

          Date.create_request_popup_date_from_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')
          Date.create_request_popup_date_to_using_ngmodel(self, input_data='05/26/2022', request_type='official_business')

          reason = 'Automated business testing'
          input_reason_data = CreateOfficialBusiness.input_reason(self, reason)
          assert reason == input_reason_data

          CreateOfficialBusiness.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateOfficialBusiness.click_confirm_button(self)
          
          expected_text = 'Date already requested.'
          success_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Date already requested.']")
          actual_text = success_message.text
          
          assert expected_text == actual_text
     
class TestPagination(Setup):

     # @pytest.mark.skip(reason="passed")
     def test_business_pagination_using_next_button(self, capsys):
          """Check results changing page using next button."""

          self.driver.implicitly_wait(30)
          next_button = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Next')]")
          next_button.click()

          page_number = self.driver.find_element(By.XPATH,"//*[@class = 'pagination-page ng-scope active']")
          page = int(page_number.text)
          
          assert page == 1 or 2

     #@pytest.mark.skip(reason="passed")
     def test_business_pagination_using_page_number(self, capsys):
          """Check results changing page using page number."""

          self.driver.implicitly_wait(30)
          input_page_number = 1
          xpath_page_number = str(input_page_number + 1)
          page_number = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[9]/pagination/div/div[3]/ul/li[{}]/a".format(xpath_page_number))
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
     
class TestRecordPerPage(Setup):

     #@pytest.mark.skip(reason="passed")
     def test_business_records_per_page_clicking_dropdown(self, capsys):
          """Check results clicking "Records per page" drop-down."""

          input_data= '50'

          self.driver.implicitly_wait(30)

          record_per_page_display = RecordsPerPage.by_inputting(self, input_data)
          sleep(10)    
          assert record_per_page_display == input_data
     

     # #@pytest.mark.skip(reason="passed")
     def test_business_records_per_page_inputting_invalid_data(self,capsys, official_business_table_name):
          """Check results inputing invalid data in "Records per page" drop-down."""

          input_data = 'ABc123'
          self.driver.implicitly_wait(10)
          
          self.driver.find_element(By.XPATH,"//div[contains(@class, 'ui-select-match')]").click()

          records_per_page_input = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[7]/div/input[1]")
          records_per_page_input.send_keys(input_data)
          records_per_page_input.send_keys(Keys.ENTER)

          sleep(10)
          record_page_count = self.driver.find_elements_by_xpath("//*[@id='"+(official_business_table_name)+"']/tbody/tr")
          table_row_count = len(record_page_count)
          with capsys.disabled():
               print(table_row_count)

          assert table_row_count == 5
     

     #@pytest.mark.skip(reason="passed")
     def test_business_records_per_page_changing_employees_per_page(self, capsys, official_business_table_name):
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

          record_page_count = len(self.driver.find_elements_by_xpath("//*[@id='"+(official_business_table_name)+"']/tbody/tr"))
          table_row_count = str(record_page_count)
          with capsys.disabled():
               print(table_row_count)

          assert record_per_page_count >= table_row_count
     
class TestDateFilter(Setup):

     # @pytest.mark.skip(reason="passed")
     def test_official_business_date_filter_result_filtering_date(self, capsys, official_business_table_name):
          """Check results filtering the date."""

          self.driver.implicitly_wait(30)
          sleep(15)
          date_from = Date.from_input(self, input_data= '07/23/2022')
          date_to = Date.to_input(self, input_data='07/23/2022')
          
          search_date = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[2]/tabletoolsdaterange2/p/span[4]/i")
          search_date.click()
          sleep(2)

          page_count = TableRecord.get_page_count(self)
          with capsys.disabled():
               print(page_count)

          effectivity_date = []
          for pages in page_count:
               for row in pages:
                    table_row = self.driver.find_element(By.XPATH,"//*[@id='"+(official_business_table_name)+"']/tbody/tr["+ str(row) +"]/td[4]")
                    table_row = table_row.text
                    effectivity_date.append(table_row)
                    assert date_from <= effectivity_date <= date_to 
               TablePagination.next_button(self)

class TestRightClick(Setup):

     pytest.mark.skip(reason="passed")
     def test_business_records_right_clicking_request(self, official_business_table_name):
          """Check results right-clicking a request."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, official_business_table_name)
          right_click_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[3]/ul").is_displayed()
          
          assert right_click_option == True
          

     @pytest.mark.skip(reason="no feature")
     def test_business_records_clicking_ViewLogs_option(self):
          """Check results clicking "View Logs" option."""
          
          self.driver.implicitly_wait(10)
          employee_name= "Cruz, Jelly Y."
          RightClick.user(self,employee_name)
          viewlog_button = self.driver.find_element(By.LINK_TEXT,'View Logs')
          viewlog_button.click()

          header_title = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[2]/div[1]/h2")
          daily_logs_page = header_title.is_displayed()
          assert daily_logs_page == True

          sleep(5)
          employee_selected = self.driver.find_element(By.XPATH, "//*[text()='{}']".format(employee_name))
          employee_view_logs = employee_selected.text
          assert employee_view_logs == employee_name

     @pytest.mark.skip(reason="no feature")
     def test_business_records_clicking_Attach_option(self):
          """Check results clicking "Attach" option."""
          
          self.driver.implicitly_wait(10)
          RightClick.user(self,employee_name='Cruz, Jelly Y.')
          attach_button = self.driver.find_element(By.LINK_TEXT,'Attach')
          attach_button.click()

          sleep(5)
          
          attachment_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div")
          is_attachment_displays = attachment_modal.is_displayed()
          assert is_attachment_displays == True

     #@pytest.mark.skip(reason="passed")
     def test_business_records_clicking_Cancel_option(self, official_business_table_name):
          """Check results clicking "Cancel" Request for Official Business option."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, official_business_table_name)
          cancel_button = self.driver.find_element(By.LINK_TEXT,'Cancel')
          cancel_button.click()
          
          cancel_request_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_request_modal_displays = cancel_request_modal.is_displayed()
          assert is_request_modal_displays == True

          specify_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          specify_reason.send_keys('Automated Cancel Request for Official Business')

          confirm_button = self.driver.find_element(By.CLASS_NAME, "confirm")
          confirm_button.click()

          business_succesfully_cancelled_dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_success_dialog_box_appeared = business_succesfully_cancelled_dialog_box.is_displayed()
          assert is_success_dialog_box_appeared  == True

     #@pytest.mark.skip(reason="passed")
     def test_business_records_clicking_Delete_option(self, official_business_table_name):
          """Check results clicking "Delete" option."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, official_business_table_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_request_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_request_modal_displays = delete_request_modal.is_displayed()
          assert is_request_modal_displays == True

          specify_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          specify_reason.send_keys('Automated Delete Request for Undertime')

          confirm_button = self.driver.find_element(By.CLASS_NAME, "confirm")
          confirm_button.click()

          business_succesfully_deleted_dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_deleted_dialog_box = business_succesfully_deleted_dialog_box.is_displayed()
          assert is_deleted_dialog_box == True
     
class TestSort(Setup):
     #@pytest.mark.skip(reason="passed")
     def test_undertime_sort_by_clicking_sort_icon(self, capsys, official_business_table_name):
          """Check results clicking sort icon by Employee name column"""

          self.driver.implicitly_wait(10)
          sleep(5)
          requested_date_latest = self.driver.find_element(By.XPATH,"//*[@id='"+(official_business_table_name)+"']/tbody/tr[1]/td[1]")
          latest_date = requested_date_latest.text
          
          sort_icon = self.driver.find_element(By.XPATH,"//*[@id='"+(official_business_table_name)+"']/thead/tr/th[1]/a/i")
          self.driver.execute_script("arguments[0].click();",sort_icon)

          bottommost_date = self.driver.find_element(By.XPATH,"//*[@id='"+(official_business_table_name)+"']/tbody/tr[1]/td[1]")
          bottom_date = bottommost_date.text

          assert bottom_date <= latest_date
