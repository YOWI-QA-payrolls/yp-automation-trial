import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup
from datetime import date as datetime
from selenium.webdriver.common.keys import Keys
from utils.set_site import admin_set_site as set_site

from utils import prompt,pagination
from utils.create_logs import CreateLogs
from utils.employee_per_page import EmployeePerPage
from utils.gear_icon import GearIcon
from utils.drop_down_arrow import Dropdown
from utils.export import Export
from utils.print import Print
from utils.date import approver_date
from utils.search import Search as search

class Setup():
	def setup_method(self):
		self.driver_service = Service(ChromeDriverManager().install())
		self.driver = webdriver.Chrome(service=self.driver_service)
		self.driver.set_window_size(width=1552, height=849)
		url = "https://yp.yahshuasupport.com/signin/?login=yes"
		self.driver.get(url)
		set_site.login(self)
		self.samplename = "EJP"

		timesheets = self.driver.find_element(By.ID,'timesheets')
		dailylogs = self.driver.find_element(By.ID,'daily_logs')

		timesheets.click()
		dailylogs.click()

	def teardown_method(self):
		self.driver.quit()

class TestSearch(Setup):
	def test_search_entering_lower(self, capsys):
		''' Check results after entering an existing data in lower case  - M2-TS2-TC1  '''
		
		input_data = "sample"
		
		actual_data = search.box_function(self, input_data)
		is_search_icon_clicked = search.click_icon_button(self)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		# actual_data = "jokes"
		actual_data = self.soup.find('table',{'id':'table'}).find('tbody').find('tr').find('td', class_="align_left ng-binding").text.strip().lower()
		# with capsys.disabled():
		# 	print(actual_data)

		assert input_data in actual_data
		assert is_search_icon_clicked == True

		self.driver.close()

	def test_search_entering_upper(self, capsys):
		''' Check results after entering an existing data in upper case  - M2-TS2-TC2  '''
		
		input_data = "SAMPLE"
		
		actual_data = search.box_function(self, input_data)
		is_search_icon_clicked = search.click_icon_button(self)
		displayed_relevant_result = search.check_all_search_results(self, input_data)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		actual_data = self.soup.find('table',{'id':'table'}).find('tbody').find('tr').find('td', class_="align_left ng-binding").text.strip().upper()

		assert input_data in actual_data
		assert is_search_icon_clicked == True

		self.driver.close()


	def test_search_entering_fullname(self, capsys):
		''' Check results after entering existing data fullname  - M2-TS2-TC3  '''
		
		input_data = "Sample, Sample1"
		
		actual_data = search.box_function(self, input_data)
		is_search_icon_clicked = search.click_icon_button(self)
		displayed_relevant_result = search.check_all_search_results(self, input_data)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		actual_data = self.soup.find('table',{'id':'table'}).find('tbody').find('tr').find('td', class_="align_left ng-binding").text.strip()
		with capsys.disabled():
			print(actual_data)

		assert input_data in actual_data
		assert is_search_icon_clicked == True

		self.driver.close()

	def test_search_entering_specialchar(self, capsys):
		''' Check results after entering special characters  - M2-TS2-TC4  '''
		
		input_data = "("
		
		actual_data = search.box_function(self, input_data)
		is_search_icon_clicked = search.click_icon_button(self)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		actual_data = self.soup.find('pagination').find('span').text.strip()
		# with capsys.disabled():
		# 	print(actual_data)

		total_records = 'Total records : 0'

		assert total_records == actual_data
		assert is_search_icon_clicked == True

		self.driver.close()

	def test_search_entering_chapa(self, capsys):
		''' Check results after entering valid chapa no.  - M2-TS2-TC5  '''
		
		input_data = "123"
		
		actual_data = search.box_function(self, input_data)
		is_search_icon_clicked = search.click_icon_button(self)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		actual_datas = self.soup.find('table',{'id':'table'}).find('tbody').find('tr').find_all('td')
		actual_data = actual_datas[3].text.strip()
		
		assert input_data == actual_data
		assert is_search_icon_clicked == True

		self.driver.close()

class TestCreate(Setup):
	def test_create_button(self, capsys):
		''' Check create button finctionality  - M2-TS3-TC1  '''
		
		dialog_name = "Create Timesheet"
		create_button = self.driver.find_element(By.XPATH, "//*[@class='btn btn-danger']")
		
		create_button.click()
		sleep(2)
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		get_dialog = self.soup.find('h3',{'class':'panel-title'})
		actual_dialog = get_dialog.text.strip()

		assert dialog_name == actual_dialog

		self.driver.close()


	def test_create_timein(self, capsys):
		''' Check results creating time in logs - M2-TS4-TC1  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		employee = "QA, Employee 1"
		employee_field_data = CreateLogs.input_employee(self, employee)
		assert employee == employee_field_data
		sleep(1)

		reason = "Test create time in automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		log_type = "IN"
		log_type_data = CreateLogs.input_log_type(self, log_type)
		assert log_type == log_type_data

		time_in_hh = "8"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		CreateLogs.click_save_button(self) 
		expected_notif = "Timesheet successfully added." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

		self.driver.close()


	def test_create_timeout(self, capsys):
		''' Check results creating time out logs - M2-TS4-TC2  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		employee = "QA, Employee 1"
		employee_field_data = CreateLogs.input_employee(self, employee)
		assert employee == employee_field_data

		reason = "Test create time out automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		log_type = "OUT"
		log_type_data = CreateLogs.input_log_type(self, log_type)
		assert log_type == log_type_data

		time_in_hh = "17"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		CreateLogs.click_save_button(self) 

		expected_notif = "Timesheet successfully added." 
		actual_success_notif = prompt.text(self)
		assert expected_notif == actual_success_notif

		self.driver.close()

	def test_create_no_employee(self, capsys):
		''' Check results creating logs with empty employee field- M2-TS4-TC3  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		reason = "Test create logs with no incomplete data automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		log_type = "IN"
		log_type_data = CreateLogs.input_log_type(self, log_type)
		assert log_type == log_type_data

		time_in_hh = "8"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		CreateLogs.click_save_button(self) 
		expected_notif = "Please specify Employee." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

		self.driver.close()

	def test_create_no_reason(self, capsys):
		''' Check results creating logs with no reason- M2-TS4-TC4  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		employee = "123 - Sample, Sample1"
		employee_field_data = CreateLogs.input_employee(self, employee)
		assert employee == employee_field_data

		reason = ""
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data		

		log_type = "IN"
		log_type_data = CreateLogs.input_log_type(self, log_type)
		assert log_type == log_type_data

		time_in_hh = "8"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		CreateLogs.click_save_button(self) 
		expected_notif = "Please indicate Reason." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

		self.driver.close()

	def test_create_no_logtype(self, capsys):
		''' Check results creating logs with no log type- M2-TS4-TC5  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		employee = "123 - Sample, Sample1"
		employee_field_data = CreateLogs.input_employee(self, employee)
		assert employee == employee_field_data

		reason = "test no log type"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data		

		time_in_hh = "8"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		CreateLogs.click_save_button(self) 
		expected_notif = "Please indicate Log Type." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

		self.driver.close()

	def test_create_no_time(self, capsys):
		''' Check results creating logs with no time - M2-TS4-TC5  '''

		CreateLogs.click_create_button(self)

		date = datetime.today().strftime("%m/%d/%Y")
		date_field_data = CreateLogs.input_date(self, date)
		assert date == date_field_data 

		employee = "123 - Sample, Sample1"
		employee_field_data = CreateLogs.input_employee(self, employee)
		assert employee == employee_field_data

		reason = "Test create time out automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		log_type = "OUT"
		log_type_data = CreateLogs.input_log_type(self, log_type)
		assert log_type == log_type_data

		CreateLogs.click_save_button(self) 

		expected_notif = "Please indicate Time." 
		actual_success_notif = prompt.text(self)
		assert expected_notif == actual_success_notif

		self.driver.close()

class TestEmployePerPage(Setup):
	def test_employee_per_page(self, capsys):
		''' Test employee per page drop-down functionality. M2-TS9-TC1'''

		EmployeePerPage.click_employee_per_page(self)
		EmployeePerPage.employee_per_page_options(self)

		expected_records_in_page = '1'

		records_in_page = EmployeePerPage.records_in_page(self) 

		assert expected_records_in_page == records_in_page

class TestColumns(Setup):

	def test_columns_filter_select_all(self, capsys):
		''' Check results clicking select all check box '''

		GearIcon.click_gear_icon(self)

		GearIcon.click_select_all_check_box(self)

		select_all_checked = self.driver.find_element(By.XPATH, "//*[@id='select_all']").is_selected()
		assert select_all_checked == True

		department = 'Department'
		location = 'Location'
		remarks = 'Remarks'

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		columns = self.soup.find('thead').find('tr').find_all("th")
		department_column = columns[11].text.strip()
		location_column = columns[12].text.strip()
		remarks_column = columns[13].text.strip()

		assert department == department_column
		assert location == location_column
		assert remarks == remarks_column

	def test_columns_filter_check_all(self, capsys):
		''' Check results checking all check box '''

		GearIcon.click_gear_icon(self)

		RFID_checkbox = self.driver.find_element(By.XPATH, "//*[@class='row']/div[3]/div/input")
		RFID_checkbox.click()
		RFID = self.driver.find_element(By.XPATH, "//*[@class='row']/div[3]/div/input").is_selected()
		assert RFID == True

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		columns = self.soup.find('thead').find('tr').find_all("th")
		
		RFID_label = "RFID"
		RFID_column = columns[2].text.strip()
		assert RFID_column == RFID_label
		sleep(2)

		department_checkbox = self.driver.find_element(By.XPATH, "//*[@class='row']/div[12]/div/input")
		department_checkbox.click()
		department = self.driver.find_element(By.XPATH, "//*[@class='row']/div[12]/div/input").is_selected()
		assert department == True

		department_label = "Department"
		department_column = columns[11].text.strip()
		assert department_label == department_column 
		sleep(2)

		location_checkbox = self.driver.find_element(By.XPATH, "//*[@class='row']/div[13]/div/input")
		location_checkbox.click()
		location = self.driver.find_element(By.XPATH, "//*[@class='row']/div[13]/div/input").is_selected()
		assert location == True

		location_label = "Location"
		location_column = columns[12].text.strip()
		assert location_label == location_column 
		sleep(2)

		remarks_checkbox = self.driver.find_element(By.XPATH, "//*[@class='row']/div[14]/div/input")
		remarks_checkbox.click()
		remarks = self.driver.find_element(By.XPATH, "//*[@class='row']/div[14]/div/input").is_selected()
		assert remarks == True

		remarks_label = "Remarks"
		remarks_column = columns[13].text.strip()
		assert remarks_label == remarks_column 

		select_all_checked = self.driver.find_element(By.XPATH, "//*[@id='select_all']").is_selected()
		assert select_all_checked == True

class TestFilters(Setup):
	def test_pagination(self, capsys):
		''' Check results changing pagination using next button '''

		next = next_button(self)

	def test_pagination(self, capsys):
		''' Check results changing pagination using page number '''

		next = page_two(self)

class TestArrowDropdown(Setup):

	def test_export(self,capsys):
		''' Check export button functionality '''

		Export.click_export_button(self)

		export_button = self.driver.find_element(By.XPATH, "//*[@class='dropdown-menu pull-right']/li/a").is_selected()

	def test_print(self,capsys):
		''' Check print button functionality '''

		Print.click_print_button(self)

	def test_resave_logs(self,capsys):
		''' Check resave logs button functionality '''

		Dropdown.click_dropdown_arrow(self)

		resave_logs_button = self.driver.find_element(By.XPATH, "//*[@class='dropdown-menu pull-right']/li[5]/a")
		resave_logs_button.click()
		sleep(10)

		resave_logs_panel_title = "Resave Logs"
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		resave_logs_dialog = self.soup.find('div', {'class':'modal-dialog'}).find('h3').get_text()

		assert resave_logs_panel_title == resave_logs_dialog 

class TestEditOptions(Setup):
	def test_delete_logs(self, capsys):
		''' test delete logs'''

		delete_icon = self.driver.find_element(By.XPATH,"//*[@ng-click='delete(record)']")
		delete_icon.click()
		sleep(3)

		confirmation_panel_title = "Are you sure you want to delete the Timesheet?"
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		confirmation_dialog_actual = self.soup.find('div', {'class':'sweet-alert show-input showSweetAlert visible'}).find('h2').get_text()
		assert confirmation_panel_title == confirmation_dialog_actual

		confirm_button = self.driver.find_element(By.XPATH,"//*[@class='confirm']")
		confirm_button.click()
		sleep(3)

		# success_dialog = "Selected logs successfully deleted."
		# success_dialog_actual = self.soup.find("div", {'class': 'sweet-alert hideSweetAlert'}).get_text()
		# assert success_dialog == success_dialog_actual

	def test_delete_timein(self, capsys):
		''' test deleting time in logs '''

		delete_icon = self.driver.find_element(By.XPATH,"//*[@title='Delete log']")
		delete_icon.click()
		sleep(3)

		confirmation_panel_title = "Are you sure you want to delete the Time In log?"
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		confirmation_dialog_actual = self.soup.find('div', {'class':'sweet-alert show-input showSweetAlert visible'}).find('h2').get_text()
		assert confirmation_panel_title == confirmation_dialog_actual

		confirm_button = self.driver.find_element(By.XPATH,"//*[@class='confirm']")
		confirm_button.click()
		sleep(3)

	def test_delete_timeout(self, capsys):
		''' test deleting time out logs '''

		delete_icon = self.driver.find_element(By.XPATH,"//*[@title='Delete log']")
		delete_icon.click()
		sleep(3)

		confirmation_panel_title = "Are you sure you want to delete the Time In log?"
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		confirmation_dialog_actual = self.soup.find('div', {'class':'sweet-alert show-input showSweetAlert visible'}).find('h2').get_text()
		assert confirmation_panel_title == confirmation_dialog_actual

		confirm_button = self.driver.find_element(By.XPATH,"//*[@class='confirm']")
		confirm_button.click()
		sleep(3)

	def test_edit_timein(self, capsys):
		''' test edit time in logs '''

		pencil_icon = self.driver.find_element(By.XPATH,"//*[@class='btn btn-link ng-scope']")
		pencil_icon.click()
		sleep(3)
		edit_time_in_dialog = self.driver.find_element(By.XPATH, "//*[@class='panel panel-primary ng-scope']").is_displayed()
		assert edit_time_in_dialog == True

		reason = "Test edit time in automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		time_in_hh = "10"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "30"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		save_button = self.driver.find_element(By.XPATH, "//*[@class='btn btn-sm btn-success']")
		save_button.click()
		expected_notif = "Timesheet successfully updated." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

	def test_edit_timeout(self, capsys):
		''' test edit time out logs '''

		pencil_icon = self.driver.find_element(By.XPATH,"//*[@class='btn btn-link ng-scope']")[3]
		pencil_icon.click()
		sleep(3)

		edit_time_in_dialog = self.driver.find_element(By.XPATH, "//*[@class='panel panel-primary ng-scope']").is_displayed()
		assert edit_time_in_dialog == True

		reason = "Test edit time out automation"
		reason_field_data = CreateLogs.input_reason(self, reason)
		assert reason == reason_field_data

		time_in_hh = "18"
		time_in_hour_data = CreateLogs.input_time_hour(self, time_in_hh)
		assert time_in_hh == time_in_hour_data
		
		time_in_mm = "45"
		time_in_minutes_data = CreateLogs.input_time_minutes(self, time_in_mm)
		assert time_in_mm == time_in_minutes_data

		save_button = self.driver.find_element(By.XPATH, "//*[@class='btn btn-sm btn-success']")
		save_button.click()
		expected_notif = "Timesheet successfully updated." 
		actual_success_notif = prompt.text(self)

		assert expected_notif == actual_success_notif

	def test_report_functionality(self, capsys):
		''' test report button functionality '''

		report_button = self.driver.find_element(By.XPATH, "//*[@ng-click='report(record)']").click()
		sleep(5)

		report_dialog = self.driver.find_element(By.XPATH, "//*[@class='sweet-alert show-input showSweetAlert visible']").is_displayed()
		assert report_dialog == True

		report_reason = self.driver.find_element(By.XPATH, "//*[@placeholder='Specify reason here...']")
		report_reason.send_keys("reason")
		sleep(3)

		confirm_button = self.driver.find_element(By.XPATH,"//*[@class='confirm']")
		confirm_button.click()
		sleep(3)

	# def test_view_schedule_details(self, capsys):
	# 	''' test the view_schedule_details functionality '''

	# def test date_filter(self, capsys):
	# 	''' test the date_filter functionality '''

	# def test_advance_filter(self, capsys):
	# 	''' test the advance_filter functionality '''

	# 	self.driver.implicitly_wait(50)
	# 	advance_filter_function(self)
		
	# 	advance_filter_popup = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[4]/tabletoolstrans/div/div/div/div").is_displayed()
	# 	assert advance_filter_popup == True
