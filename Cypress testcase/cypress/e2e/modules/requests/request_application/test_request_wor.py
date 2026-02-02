from datetime import datetime
import pytest
from pytest import skip
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys
# from utils.set_site import Login
from utils.toast_container import Notification
from request_cookies import add_cookies
from utils.create_restday import CreateRestday
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

class Setup():

     def setup_method(self): 
          """Run this setup for this test class."""
          
          self.driver = driversetup()
          self.driver.maximize_window()
          target_url = main_url()
          url = "%s/dashboard/" % (target_url)
          self.driver.get(url)

          self.driver.delete_all_cookies()
          self.driver.refresh()
          add_cookies(self)
          self.driver.refresh()
          
          self.driver.get("https://yp.yahshuasupport.com/requests/undertime_overtime_request/main_page/#/workonrestday_request")
          sleep(10)
          
     def teardown_method(self, method):
          self.driver.quit()

class TestSearch(Setup):

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_existing_data_lowercase(self, capsys, restday_table_name):
          """Test Search functionality inputting lowercase in the searchbox"""
          
          input_data = "widle"
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,restday_table_name, column_number='3')
          
          assert table_record_results == True , "It didn't display the existing datas related to the inputted data."

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_existing_data_uppercase(self, capsys,restday_table_name):
          """Test Search functionality inputting uppercase in the searchbox"""
          
          input_data = "MONITORING"
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,restday_table_name, column_number='3')
          
          assert table_record_results == True , "It didn't display the existing datas related to the inputted data."

     # #@pytest.mark.skip(reason="passed")
     def test_entering_existing_employee_fullname(self, capsys,restday_table_name):
          """Test Search functionality entering employee fullname in the searchbox"""

          input_data = "sample1,sample1a v."
          
          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,restday_table_name, column_number='3')
          assert table_record_results[0] == input_data , "It didn't display the existing datas related to the inputted data."
     

     # #@pytest.mark.skip(reason="passed")
     def test_entering_special_characters_specifically_parentheses_and_dash(self, capsys,restday_table_name):
          """Test Search functionality entering special characters in the searchbox"""

          input_data=")(-"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          sleep(5)
          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys,restday_table_name, column_number='3')
          assert table_record_results == True, "Special characters should be ignored since CHAPA No. and Employee Name are the only fileds which is searchable."
     

     def test_search_entering_valid_Chapa_or_Employee_ID(self, capsys,restday_table_name):
          """Test Search functionality entering chapa or employee ID in the searchbox"""

          input_data="1013"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data
          sleep(5)

          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys, restday_table_name, column_number='3')
          assert table_record_results == True ,"It didn't display existing data related to the inputted data."

     #@pytest.mark.skip(reason="passed")
     def test_search_entering_partial_valid_Chapa_or_Employee_ID(self, capsys, restday_table_name):
          """Test Search functionality entering partial valid chapa in the searchbox"""

          input_data = "785"

          self.driver.implicitly_wait(15)
          actual_data = Search.box_function(self, input_data)
          assert input_data == actual_data

          is_search_icon_clicked = Search.click_icon_button(self)
          assert is_search_icon_clicked == True

          table_record_results = Search.check_all_search_results(self, input_data, capsys, restday_table_name, column_number='3')
          assert table_record_results == True 

class TestAdvanceFilter(Setup):

     def test_choosing_advance_filter_status(self,capsys, restday_table_name):
          """Test Search functionality choosing "Recommended" option on Advance Filter's Status."""

          AdvanceFilter.button_click(self)

          status_selection = 'Recommended'
          status_field_data = AdvanceFilter.select_status(self, status_selection, filter_no = 'ui-select-choices-1')
          assert status_field_data == status_selection

          AdvanceFilter.click_search_button(self)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_status_recommended(self, page_count, restday_table_name)
          with capsys.disabled():
               print(employee_list)

          assert_lists = any(word in "Recommended" for word in employee_list)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_payroll_status_selecting_normal(self, capsys, restday_table_name):
          #Advance Filter
          """Test Search functionality choosing "Normal" option on Advance Filter's "Payroll Status"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'restday_request.payroll_status')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Normal")
          with capsys.disabled():
               print(employee_name)
               print(employee_list)

          assert_lists = any(word in employee_name for word in employee_list)

          assert assert_lists == True

     # #@pytest.mark.skip(reason="not needed")
     def test_choosing_advance_filter_payroll_status_selecting_confidential(self, capsys, restday_table_name):
          """Test Search functionality choosing "Confidential" option on Advance Filter's "Payroll Status"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_payroll_status(self,input_data="Confidential",request_type = 'restday_request.payroll_status')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          employee_name = EmployeeModuleTable.get_employee_payroll_status(self,capsys, payroll_status= "Confidential")
          with capsys.disabled():
               print(employee_name)
               print(employee_list)

          assert_lists = any(word in employee_name for word in employee_list)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_location(self, capsys, restday_table_name):
          """Test Search functionality choosing "DIRECT" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_location(self,input_location="DIRECT",filter_no='ui-select-choices-3')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          # #Employee Module
          input_location = "DIRECT"
          employee_name = EmployeeModuleTable.get_employee_location(self, capsys, input_location)
          with capsys.disabled():
               print(employee_name)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_location_davao(self, capsys, restday_table_name):
          """Test Search functionality choosing "Davao" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_location(self,input_location="DAVAO",filter_no='ui-select-choices-3')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Employee Module
          input_location = "DAVAO"
          employee_name = EmployeeModuleTable.get_employee_location(self, capsys, input_location)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed") 
     def test_choosing_advance_filter_division(self, capsys, restday_table_name):
          """Test Search functionality choosing "Division 1" option on Advance Filter's "Division"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_division(self,input_division="Division 1",filter_no='ui-select-choices-4')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Division Module
          input_division="Division 1"
          employee_name = EmployeeModuleTable.get_employee_division(self, capsys, input_division)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_department(self, capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "Department"."""

          AdvanceFilter.button_click(self)
          AdvanceFilter.select_department(self, input_department = "Operations", filter_no='ui-select-choices-5')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Department Module
          input_department="Operations"
          employee_name = EmployeeModuleTable.get_employee_department(self, capsys,input_department)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_section(self, capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "Section"."""

          AdvanceFilter.button_click(self)
          
          AdvanceFilter.select_section(self,input_section="Accounts Payable",filter_no='ui-select-choices-6')
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Section Module
          input_section="Accounts Payable"
          employee_name = EmployeeModuleTable.get_employee_section(self, capsys,input_section)

          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_employee(self, capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "employee"."""

          AdvanceFilter.button_click(self)

          AdvanceFilter.select_employee(self,input_employee="10010 - Ackerman, Levi R.")
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          #Employee Module
          input_employee="10010 - Ackerman, Levi R."
          employee_name = EmployeeModuleTable.get_employee(self, capsys, input_employee)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_job_level(self,capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "Job Level"."""

          self.driver.implicitly_wait(10)
          AdvanceFilter.button_click(self)
          
          sleep(5)
          AdvanceFilter.select_job_level(self,input_job_level="Monthlies",request_type= 'restday_request.job_level')
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          input_job_level="Monthlies"
          employee_name = EmployeeModuleTable.get_job_level(self,input_job_level)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_location(self, capsys, restday_table_name):
          """Test Search functionality choosing "Davao" and "Laguna" option on Advance Filter's "Location"."""

          AdvanceFilter.button_click(self)
          
          multiple_location_selection = ["DAVAO","LAGUNA"]
          for input_location in multiple_location_selection:
               AdvanceFilter.select_location(self,input_location ,filter_no='ui-select-choices-3')
          
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          
          employee_name = EmployeeModuleTable.get_multiple_employee_location(self, capsys, multiple_location_selection)
          with capsys.disabled():
               print(no_duplicate_employee_request)
               print(employee_name)

          
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_division(self,capsys, restday_table_name):
          """Test Search functionality choosing "Payroll" option on Advance Filter's "Division"."""

          AdvanceFilter.button_click(self)
          
          multiple_division_selection = ["Division 2","Division 1"]
          for input_division in multiple_division_selection:
               AdvanceFilter.select_division(self, input_division ,filter_no='ui-select-choices-4')
          
          AdvanceFilter.click_search_button(self)
          sleep(5)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_division(self,capsys, multiple_division_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_department(self, capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "Department"."""

          AdvanceFilter.button_click(self)
          
          multiple_department_selection = ["Operations","Direct Labor"]
          for input_department in multiple_department_selection:
               AdvanceFilter.select_department(self,input_department ,filter_no='ui-select-choices-5')
          
          AdvanceFilter.click_search_button(self)
          sleep(3)
          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_department(self,capsys, multiple_department_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

     # #@pytest.mark.skip(reason="passed")
     def test_choosing_advance_filter_selecting_multiple_section(self, capsys, restday_table_name):
          """Test Search functionality choosing option on Advance Filter's "Section"."""

          AdvanceFilter.button_click(self)
          
          multiple_section_selection = ["Section 1","Accounts Payable"]
          for input_section in multiple_section_selection:
               AdvanceFilter.select_section(self,input_section ,filter_no='ui-select-choices-6')
          
          self.driver.implicitly_wait(10)
          AdvanceFilter.click_search_button(self)

          page_count = TableRecord.get_page_count(self)

          employee_list = EmployeeTable.get_employee_name(self, page_count, restday_table_name)
          no_duplicate_employee_request = list(dict.fromkeys(employee_list))
          with capsys.disabled():
               print(no_duplicate_employee_request)

          employee_name = EmployeeModuleTable.get_multiple_employee_section(self,capsys, multiple_section_selection)
          assert_lists = any(item in no_duplicate_employee_request for item in employee_name)
          assert assert_lists == True

class TestCreateButton(Setup):

     def test_create_button(self):
          """Check response on clicking "Create" button under "restday" tab."""

          self.driver.implicitly_wait(10)
          create_button = self.driver.find_element(By.XPATH,"//button[contains(@class, 'btn-danger')]")
          create_button.click()
          sleep(3)

          add_restday_request_form = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]").is_displayed()
          assert add_restday_request_form  == True

class TestCreateRestdayRequest(Setup):

     employee = "111 - QA, Employee 1"

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_on_scheduled_workday(self):

          """Check results on requesting restday request on schdeduled workday."""

          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)
          sleep(5)

          employee_input_data = CreateRestday.input_employee(self, self.employee)

          Date.request_popup_date_from(self, input_data='09/04/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='09/04/2022', request_type='restday')

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          reason = 'Automated restday testing'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateRestday.click_confirm_button(self)
          
          expected_text = 'Successfully saved!'
          success_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Successfully saved!']")
          actual_text = success_message.text
          assert expected_text == actual_text, "Requested date is not in the list of restdays. Please check."

          #Delete record
          self.driver.implicitly_wait(10)
          sleep(5)
          
          employee_name = "QA, Employee 1"
          RightClick.user(self,employee_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          delete_reason.send_keys('Automated Testing')

          confirm_button = self.driver.find_element(By.CLASS_NAME,"confirm")
          confirm_button.click()

          ok_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/div[7]/button[2]")
          ok_button.click()
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_on_rest_day(self):
          """Check results on requesting restday request on restday."""
          
          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)
          sleep(5)

          employee_input_data = CreateRestday.input_employee(self, self.employee)

          Date.request_popup_date_from(self, input_data='09/11/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='09/11/2022', request_type='restday')

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          reason = 'restday Automated testing RD'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateRestday.click_confirm_button(self)
          sleep(0.5)
          
          expected_text = 'Successfully saved!'
          success_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Successfully saved!']")
          actual_text = success_message.text
          assert expected_text == actual_text, "Please change the date from and date to if already requested"

          #Delete record
          employee_name = "QA, Employee 1"
          RightClick.user(self,employee_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          delete_reason.send_keys('Automated Testing')

          confirm_button = self.driver.find_element(By.CLASS_NAME,"confirm")
          confirm_button.click()

          ok_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/div[7]/button[2]")
          ok_button.click()
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_invalid_date(self):
          """Check results on requesting restday request with invalid date."""

          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)

          employee_input_data = CreateRestday.input_employee(self, self.employee)

          Date.request_popup_date_from(self, input_data='04/03/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='04/02/2022', request_type='restday')

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          reason = 'Automated restday testing Invalid date.'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_text = 'Invalid date.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Invalid date.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_incomplete_reasonfield(self):
          """Check results on requesting restday request with incomplete fields(Reason field)."""

          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)
          
          employee_input_data = CreateRestday.input_employee(self, self.employee)

          Date.request_popup_date_from(self, input_data='04/02/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='04/02/2022', request_type='restday')

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          CreateRestday.click_submit_button(self)

          expected_text = 'Please indicate a Reason.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Please indicate a Reason.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_incomplete_hours_field(self):
          """Check results on requesting restday request with incomplete fields(Hours field)."""

          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)
          
          employee_input_data = CreateRestday.input_employee(self, self.employee)

          Date.request_popup_date_from(self, input_data='04/02/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='04/02/2022', request_type='restday')

          reason = 'Automated restday testing RD'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_text = 'Please indicate correct Hours/Minutes.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Please indicate correct Hours/Minutes.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_incomplete_employee_field(self):
          """Check results on requesting restday request with incomplete fields(Employee Field)."""
          
          self.driver.implicitly_wait(25)
          CreateRestday.click_create_button(self)
          sleep(5)

          Date.request_popup_date_from(self, input_data='04/02/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='04/02/2022', request_type='restday')

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          reason = 'Automated restday testing'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_text = 'Please select Employee.'
          error_message = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Please select Employee.']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     

     # @pytest.mark.skip(reason="passed")
     def test_create_restday_duplicate_request(self):
          """Check results on requesting restday request with already requested date(Duplicate request)."""

          self.driver.implicitly_wait(25)
          
          CreateRestday.click_create_button(self)
          sleep(5)

          Date.request_popup_date_from(self, input_data='07/24/2022',request_type='restday')
          Date.request_popup_date_to(self, input_data='07/24/2022', request_type='restday')

          employee_input_data = CreateRestday.input_employee(self, self.employee)

          hour = '1'
          input_hour_data = CreateRestday.input_hour(self, hour)
          assert hour == input_hour_data

          minute = '30'
          input_minute_data = CreateRestday.input_minute(self, minute)
          assert minute == input_minute_data

          reason = 'Automated restday testing'
          input_reason_data = CreateRestday.input_reason(self, reason)
          assert reason == input_reason_data

          CreateRestday.click_submit_button(self)

          expected_confirmation_dialog = "Continue?"
          dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[6]/h2")
          dialog_actual_text = dialog_box.text
          assert expected_confirmation_dialog == dialog_actual_text
          
          CreateRestday.click_confirm_button(self)
          
          expected_text = 'Date: 2022-07-24 already requested for QA, Employee 1'
          error_message = self.driver.find_element(By.XPATH,"//*[@class = 'toast-title']")
          actual_text = error_message.text
          
          assert expected_text == actual_text
     
class TestAddRestdayRequest(Setup):

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_funnel_button(self):
          """Check results on clicking funnel button."""

          self.driver.implicitly_wait(20)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)

          expected_text = "Filter Employee"
          filter_popup = self.driver.find_element(By.XPATH,"//*[@ng-if = 'uibTitle']")
          actual_text = filter_popup.text

          assert expected_text == actual_text
     

     # #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_location(self, capsys):
          """Check results on filtering "Location" in "Employee" field."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)
          
          location_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[1]/div/ul/li/input")
          location_option.click()

          location_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('CEBU'))
          self.driver.execute_script("arguments[0].click();",location_option)

          CreateRestday.click_done_button(self)
          sleep(3)
          CreateRestday.click_select_all(self)
          
          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]
          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)
          
          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= EmployeeModuleTable.get_employee_location(self,capsys, input_location="CEBU")
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_division(self,capsys):
          """Check results on filtering "Division" in "Employee" field."""

          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)

          division_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[2]/div/ul/li/input")
          division_option.click()

          select_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('Division 2'))
          self.driver.execute_script("arguments[0].click();",select_option)

          sleep(3)
          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]  

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= EmployeeModuleTable.get_employee_division(self,capsys, input_division="Division 2")
          assert_lists = any(item in employee_name for item in employee_list)
          assert assert_lists == True
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_department(self, capsys):
          """Check results after choosing an option on Advance Filter's "Department"."""

          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)

          department_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[3]/div/ul/li/input")
          department_option.click()

          select_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('Admin'))
          self.driver.execute_script("arguments[0].click();",select_option)

          sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)

          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= EmployeeModuleTable.get_employee_department(self,capsys, input_department="Admin")
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_section(self, capsys):
          """Check the results after choosing an option on Advance Filter's "Section"."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)
          sleep(3)

          section_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[4]/div/ul/li/input")
          section_option.click()
          sleep(2)

          select_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('Section 2'))
          self.driver.execute_script("arguments[0].click();",select_option)

          sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)
          
          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]

          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)

          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= EmployeeModuleTable.get_employee_section(self,capsys, input_section="Section 2")
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_job_level(self,capsys):
          """Check the results after choosing an option on Advance Filter's "Job Level"."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          sleep(5)
          CreateRestday.click_filter_button(self)

          sleep(3)
          job_level_caret = self.driver.find_element_by_xpath("//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[5]/div/a/span[3]")
          job_level_caret.click()

          select_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('Monthlies'))
          self.driver.execute_script("arguments[0].click();",select_option)

          sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]
          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               employee_list.append(employee_text)

          with capsys.disabled():
               print(employee_list)

          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name = EmployeeModuleTable.get_job_level(self, input_job_level="Monthlies")
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True
     

     # #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_payroll_status(self, capsys):
          """Check results after choosing "Confidential" option on Advance Filter's "Payroll Status"."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)
          
          sleep(3)

          payroll_status_caret = self.driver.find_element_by_xpath("//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[6]/div/a/span[3]/b")
          payroll_status_caret.click()
          
          select_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format('Normal'))
          self.driver.execute_script("arguments[0].click();",select_option)

          sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]
          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               employee_list.append(employee_text)

          close_button =  self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[1]")
          self.driver.execute_script("arguments[0].click();",close_button)

          assert_lists = any(word in "Recommended" for word in employee_list)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_selecting_multiple_location(self,capsys):
          """Check the results after selecting MULTIPLE options on Advance Filter's "Location"."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)

          multiple_locaton_selection = ["DAVAO","LAGUNA"]
          for location_input in multiple_locaton_selection:
               
               location_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[1]/div/ul/li/input")
               location_option.click()
               sleep(3)

               selection_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format(location_input))
               self.driver.execute_script("arguments[0].click();",selection_option)
               sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]

          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)
          
          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name = EmployeeModuleTable.get_multiple_employee_location(self, capsys,multiple_locaton_selection)
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_selecting_multiple_divison(self, capsys):
          """Check the results after selecting MULTIPLE options on Advance Filter's "Division"."""

          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)
          
          multiple_division_selection = ["Division 2","Division 1"]
          for division_input in multiple_division_selection:
               
               division_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[2]/div/ul/li/input")
               division_option.click()
               sleep(3)

               selection_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format(division_input))
               selection_option.click()
               sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]
          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)
          
          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= employee_name = EmployeeModuleTable.get_multiple_employee_division(self, capsys,multiple_division_selection)
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_selecting_multiple_department(self,capsys):
          """Check the results after selecting MULTIPLE options on Advance Filter's "Department"."""
          
          self.driver.implicitly_wait(50)
          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)

          multiple_department_selection = ["Operations","Direct Labor"]
          for department_input in multiple_department_selection:
               
               department_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[3]/div/ul/li/input")
               department_option.click()
               sleep(3)

               selection_option = self.driver.find_element(By.XPATH,"//*[text()='{}']".format(department_input))
               selection_option.click()
               sleep(3)

          CreateRestday.click_done_button(self)
          CreateRestday.click_select_all(self)

          employee_list = []
          employee_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/small")
          employee_count = employee_option.text
          cut_text_get_value = employee_count[employee_count.index("(") + 1:employee_count.rindex(")")]
          with capsys.disabled():
               print(cut_text_get_value)

          for row in range(1,int(cut_text_get_value)+1):
               employee = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[4]/div/ul/span/li["+ str(row) +"]/span/span")
               employee_text = employee.text
               separated_text = employee_text.split(" - ")
               try :
                    employee_list.append(separated_text[1])
               except IndexError:
                    employee_list.append(separated_text[0])

          with capsys.disabled():
               print(employee_list)
          
          CreateRestday.click_close_button(self)

          sleep(3)
          employee_name= employee_name = EmployeeModuleTable.get_multiple_employee_department(self, capsys,multiple_department_selection)
          assert_lists = any(item in employee_list for item in employee_name)
          assert assert_lists == True
     

     #@pytest.mark.skip(reason="passed")
     def test_create_restday_filter_reset_button(self):
          """Check result on clicking "Reset" button."""
          
          self.driver.implicitly_wait(50)
          sleep(5)

          CreateRestday.click_create_button(self)
          CreateRestday.click_filter_button(self)
          CreateRestday.click_select_all(self)

          reset_button = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/div[3]/filteremployee/div/div[2]/div/div/div/div[8]/button[2]")
          reset_button.click()                              
          sleep(3)

          assert reset_button == reset_button

class TestPagination(Setup):

     # @pytest.mark.skip(reason="passed")
     def test_restday_pagination_using_next_button(self, capsys):
          """Check results changing page using next button."""

          self.driver.implicitly_wait(30)
          next_button = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Next')]")
          next_button.click()

          page_number = self.driver.find_element(By.XPATH,"//*[@class = 'pagination-page ng-scope active']")
          page = int(page_number.text)
          
          assert page == 1 or 2

     #@pytest.mark.skip(reason="passed")
     def test_restday_pagination_using_page_number(self, capsys):
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
     def test_restday_records_per_page_clicking_dropdown(self, capsys):
          """Check results clicking "Records per page" drop-down."""

          input_data= '50'

          self.driver.implicitly_wait(30)

          record_per_page_display = RecordsPerPage.by_inputting(self, input_data)
          sleep(10)    
          assert record_per_page_display == input_data
     

     # #@pytest.mark.skip(reason="passed")
     def test_restday_records_per_page_inputting_invalid_data(self,capsys, restday_table_name):
          """Check results inputing invalid data in "Records per page" drop-down."""

          input_data = 'ABc123'
          self.driver.implicitly_wait(10)
          
          self.driver.find_element(By.XPATH,"//div[contains(@class, 'ui-select-match')]").click()

          records_per_page_input = self.driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[7]/div/input[1]")
          records_per_page_input.send_keys(input_data)
          records_per_page_input.send_keys(Keys.ENTER)

          sleep(10)
          record_page_count = self.driver.find_elements_by_xpath("//*[@id='"+(restday_table_name)+"']/tbody/tr")
          table_row_count = len(record_page_count)
          with capsys.disabled():
               print(table_row_count)

          assert table_row_count == 5
     

     #@pytest.mark.skip(reason="passed")
     def test_restday_records_per_page_changing_employees_per_page(self, capsys, restday_table_name):
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

          record_page_count = len(self.driver.find_elements_by_xpath("//*[@id='"+(restday_table_name)+"']/tbody/tr"))
          table_row_count = str(record_page_count)
          with capsys.disabled():
               print(table_row_count)

          assert record_per_page_count >= table_row_count

class TestRightClick(Setup):

     pytest.mark.skip(reason="passed")
     def test_restday_records_right_clicking_request(self, restday_table_name):
          """Check results right-clicking a request."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, restday_table_name)
          right_click_option = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[3]/ul").is_displayed()
          
          assert right_click_option == True
          

     #@pytest.mark.skip(reason="passed")
     def test_restday_records_clicking_ViewLogs_option(self):
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

     #@pytest.mark.skip(reason="passed") 
     def test_restday_records_clicking_Attach_option(self):
          """Check results clicking "Attach" option."""
          
          self.driver.implicitly_wait(10)
          employee_name = "QA, Employee 1"
          RightClick.user(self,employee_name)
          attach_button = self.driver.find_element(By.LINK_TEXT,'Attach')
          attach_button.click()

          sleep(5)
          
          attachment_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[1]/div/div")
          is_attachment_displays = attachment_modal.is_displayed()
          assert is_attachment_displays == True

     #@pytest.mark.skip(reason="passed")
     def test_restday_records_clicking_Cancel_option(self, restday_table_name):
          """Check results clicking "Cancel" Request for Undertime option."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, restday_table_name)
          cancel_button = self.driver.find_element(By.LINK_TEXT,'Cancel')
          cancel_button.click()
          
          cancel_request_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_request_modal_displays = cancel_request_modal.is_displayed()
          assert is_request_modal_displays == True

          specify_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          specify_reason.send_keys('Automated Cancel Request for Undertime')

          confirm_button = self.driver.find_element(By.CLASS_NAME,"confirm")
          confirm_button.click()

          restday_succesfully_cancelled_dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_success_dialog_box_appeared = restday_succesfully_cancelled_dialog_box.is_displayed()
          assert is_success_dialog_box_appeared  == True

     #@pytest.mark.skip(reason="passed")
     def test_restday_records_clicking_Delete_option(self, restday_table_name):
          """Check results clicking "Delete" option."""
          
          self.driver.implicitly_wait(10)
          RightClick.first_row(self, restday_table_name)
          delete_button = self.driver.find_element(By.LINK_TEXT,'Delete')
          delete_button.click()
          sleep(2)

          delete_request_modal = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_request_modal_displays = delete_request_modal.is_displayed()
          assert is_request_modal_displays == True

          specify_reason = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]/fieldset/input")
          specify_reason.send_keys('Automated Delete Request for Undertime')

          confirm_button = self.driver.find_element(By.CLASS_NAME,"confirm")
          confirm_button.click()

          restday_succesfully_deleted_dialog_box = self.driver.find_element(By.XPATH,"//*[@id='page-top']/div[4]")
          is_deleted_dialog_box = restday_succesfully_deleted_dialog_box.is_displayed()
          assert is_deleted_dialog_box == True

class TestSort(Setup):
     #@pytest.mark.skip(reason="passed")
     def test_undertime_sort_by_clicking_sort_icon(self, capsys, restday_table_name):
          """Check results clicking sort icon by Employee name column"""

          self.driver.implicitly_wait(10)
          sleep(5)
          requested_date_latest = self.driver.find_element(By.XPATH,"//*[@id='"+(restday_table_name)+"']/tbody/tr[1]/td[1]")
          latest_date = requested_date_latest.text
          
          sort_icon = self.driver.find_element(By.XPATH,"//*[@id='"+(restday_table_name)+"']/thead/tr/th[1]/a/i")
          self.driver.execute_script("arguments[0].click();",sort_icon)

          bottommost_date = self.driver.find_element(By.XPATH,"//*[@id='"+(restday_table_name)+"']/tbody/tr[1]/td[1]")
          bottom_date = bottommost_date.text

          assert bottom_date <= latest_date

