import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date as datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

from utils import searchbox, filter_effectivity, apply, right_click, pagination, prompt, auto_approval_review, record_per_page, record_field
from utils.advance_filter import reviewer_advance_filter_dropdown as advance_filter
from utils.approval_dialog import reviewer_approval_dialog as approval_dialog
from utils.attachment import reviewer_attachment as attachment
from utils.date import Date
from utils.set_site import admin_set_site as set_site
from utils.search import Search
from utils.filters import AdvanceFilter
from utils.confirmation import Confirmation


class Setup():
    def setup_method(self, method):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.set_window_size(width=1552, height=849)
        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)
        set_site.login(self)
        self.samplename = "EJP"

        employees = self.driver.find_element(By.ID,'employee_list')
        earnings_and_deduction = self.driver.find_element(By.ID,'employee_income_deduction')
        earnings = self.driver.find_element(By.ID,'employee_earnings')
        recurring_earnings = self.driver.find_element(By.ID,'employee_recurring_earnings_details')

        employees.click()
        sleep(1)
        earnings_and_deduction.click()
        sleep(1)
        earnings.click()
        recurring_earnings.click()
        sleep(3)

    def teardown_method(self, method):
        self.driver.quit()

class TestViewBy(Setup):
    def test_view_by_dropdown(self):
        """ Check "View By" dropdown options functionality  """

        view_by_dropdown = self.driver.find_element(By.XPATH, '//*[@class="select2-choice ui-select-match ng-scope"]')
        view_by_dropdown_list = self.driver.find_element(By.ID, 'ui-select-choices-0')

        view_by_dropdown.click()
        sleep(2)

        assert view_by_dropdown_list.is_displayed()

        self.driver.close()

    def test_view_by_dropdown_summary_option(self):
        """ Check response on clicking "Summary" options under "View By" dropdown button in the "Recurring Earnings" """

        view_by_dropdown = self.driver.find_element(By.XPATH, '//*[@class="select2-choice ui-select-match ng-scope"]')
        view_by_dropdown.click()
        sleep(1)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='Summary']")
        self.driver.execute_script("arguments[0].click();",select_option)
        sleep(1)

        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Summary"

        search = self.driver.find_element(By.XPATH, '//*[@ng-if="!main.no_search_button"]')
        search.click()
        sleep(1)

        assert check_selection == "Summary"

        sleep(2)

    def test_view_by_dropdown_detailed_option(self):
        """ Check response on clicking "Detailed" options under "View By" dropdown button in the "Recurring Earnings" """

        view_by_dropdown = self.driver.find_element(By.XPATH, '//*[@class="select2-choice ui-select-match ng-scope"]')
        view_by_dropdown.click()
        sleep(1)

        select_option = self.driver.find_element(By.XPATH, "//*[text()='Detailed']")
        self.driver.execute_script("arguments[0].click();",select_option)
        sleep(1)

        check_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[2]/div/a/span[2]/span").text
        assert check_selection == "Detailed"

        search = self.driver.find_element(By.XPATH, '//*[@ng-if="!main.no_search_button"]')
        search.click()
        sleep(1)

        assert check_selection == "Detailed"

        sleep(2)

class TestDate(Setup):
    def test_date_from(self):
        """ Check "Date From" functionality under " Recurring Earnings" tab. """

        Date.date_from_calendar_icon(self)
        sleep(4)

    def test_date_to(self):
        """ Check "Date To" functionality under " Recurring Earnings" tab."""

        Date.date_to_calendar_icon(self)
        sleep(4)

class TestRecurringEarningsType(Setup):

    def test_input_box(self):
        recurring_earnings_input_box = self.driver.find_element(By.XPATH,"//*[@class='select2-search-field']")
        recurring_earnings_input_box.click()
        sleep(4)

        recurring_earnings_drop_down = self.driver.find_element(By.XPATH,"//*[@class='ui-select-dropdown select2-drop select2-with-searchbox select2-drop-active']")

        assert recurring_earnings_drop_down.is_enabled() == True

    def test_select_all(self,capsys):

        select_all = self.driver.find_element(By.XPATH,"//*[@class='btn btn-xs btn-white']//i[contains(text(), ' Select all')]")
        select_all.click()
        sleep(1)

        recurring_earnings_type_field = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li").text

        assert recurring_earnings_type_field != ""

    def test_deselect_all(self,capsys):
        deselect_all = self.driver.find_element(By.XPATH,"//*[@class='btn btn-xs btn-white']//i[contains(text(), ' Deselect all')]")
        deselect_all.click() 

        try:
            recurring_earnings_type_field = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li")
        except Exception:
            recurring_earnings_type_field = ""
        
        assert recurring_earnings_type_field == ""

        recurring_earnings_type_field = ' '

        select_all = self.driver.find_element(By.XPATH,"//*[@class='btn btn-xs btn-white']//i[contains(text(), ' Select all')]")
        select_all.click()
        sleep(1)
        deselect_all = self.driver.find_element(By.XPATH,"//*[@class='btn btn-xs btn-white']//i[contains(text(), ' Deselect all')]")
        deselect_all.click() 

        try:
            recurring_earnings_type_field = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li")
        except Exception:
            recurring_earnings_type_field = ""
        
        assert recurring_earnings_type_field == ""


    def test_clicking_specific_recurring_earnings_type(self,capsys):
        ''' Check response on clicking specific Recurring Earnings Type '''

        recurring_earnings_input_box = self.driver.find_element(By.XPATH,"//*[@class='select2-search-field']")
        recurring_earnings_input_box.click()

        recurring_earnings_type = self.driver.find_element(By.XPATH,"//*[@class='select2-result-single']/li").click()
        sleep(1)

        recurring_earnings_type_field = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li")

        assert recurring_earnings_type_field.is_displayed()

        search_button = self.driver.find_element(By.XPATH,"//*[@class='btn btn-success col-sm']")
        search_button.click()
        sleep(3)

        assert recurring_earnings_type_field.is_displayed()

    def test_clicking_multiple_recurring_earnings_type(self,capsys):
        ''' Check response on clicking multiple Recurring Earnings Type '''

        recurring_earnings_input_box = self.driver.find_element(By.XPATH,"//*[@class='select2-search-field']")
        recurring_earnings_input_box.click()

        recurring_earnings_type = self.driver.find_element(By.XPATH,"//*[@class='ui-select-dropdown select2-drop select2-with-searchbox select2-drop-active']/ul/li/ul")

        recurring_earnings_type.click()
        recurring_earnings_input_box.click()
        recurring_earnings_type.click()
        sleep(1)

        search_button = self.driver.find_element(By.XPATH,"//*[@class='btn btn-success col-sm']")
        search_button.click()
        sleep(3)

        recurring_earnings_type_field_1 = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li")
        recurring_earnings_type_field_2 = self.driver.find_element(By.XPATH,"//*[@class='select2-choices']/span/li[1]")

        assert recurring_earnings_type_field_1.is_displayed()
        assert recurring_earnings_type_field_2.is_displayed()

class TestSearch(Setup):
    def test_searching_chapa_number(self,capsys):
        ''' Check response on searching Chapa number '''

        input_data = '123'

        actual_data = Search.box_function(self, input_data)
        Search.click_icon_button

        assert input_data == actual_data

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        table_data = self.soup.find('table',{'class':'table-bordered table-hover sticky-enabled'}).find('tbody').find('tr').find('th').text.strip()

        assert input_data == table_data

    def test_searching_employee_name(self,capsys):
        ''' Check response on searching employee name '''

        input_data = 'Sample1'

        actual_data = Search.box_function(self, input_data)
        Search.click_icon_button(self)
        sleep(3)

        assert input_data == actual_data

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        table_data = self.soup.find('table',{'class':'table-bordered table-hover sticky-enabled'}).find('tbody').find('tr').find_all('th')

        assert input_data in table_data[1].text.strip()


class TestAdvanceFilter(Setup):

    def test_clicking_advance_filter(self):
        """Check response when clicking "Advance Filter" button""" 

        AdvanceFilter.button_click(self)
        
        advance_filter_popup = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div")
        is_advance_filter_popup_displayed = advance_filter_popup.is_displayed()

        assert is_advance_filter_popup_displayed == True


        self.driver.close()

    def test_advance_filter_payroll_status_dropdown_button(self):
        """Check response "Payroll Status" dropdown button.""" 

        AdvanceFilter.button_click(self)

        advance_filter_popup = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div").is_displayed()
        assert advance_filter_popup == True

        AdvanceFilter.select_payroll_status(self,input_data="Normal",request_type = 'filter.payroll_status')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/abbr")
        x_icon.click()

        sleep(3)

        payroll_status_option = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[1]/div/a/span[1]").text
        
        assert payroll_status_option =="ALL"

        self.driver.close()

    def test_advance_filter_inputting_location(self):
        """Check response "Location" input box.""" 

        AdvanceFilter.button_click(self)

        AdvanceFilter.select_location(self,input_location="DAVAO",filter_no='ui-select-choices-4')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True

        x_icon.click()

        select_all_button =  self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[1]")
        select_all_button.click()
        sleep(10)
        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/button[2]")
        deselect_all_button.click()

        location_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[2]/div/ul/li/input")
        return_default_value = location_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_division(self):
        """Check response "Division" input box.""" 

        AdvanceFilter.button_click(self)

        AdvanceFilter.select_division(self,input_division="Division 1",filter_no='ui-select-choices-5')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True

        x_icon.click()

        select_all_button =  self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/button[1]")
        select_all_button.click()
        sleep(10)
        deselect_all_button = self.driver.find_element_by_xpath("//*//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/button[2]")
        deselect_all_button.click()

        division_inputbox = self.driver.find_element_by_xpath("//*//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[3]/div/ul/li/input")
        return_default_value = division_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_department(self):
        """Check response "Department" input box.""" 

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_department(self,input_department="Operations",filter_no='ui-select-choices-6')

        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True

        x_icon.click()


        select_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/button[1]")
        deselect_all_button.click()

        sleep(3)

        department_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[4]/div/ul/li/input")
        return_default_value = department_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_section(self):
        """Check response "Section" input box.""" 

        AdvanceFilter.button_click(self)
        AdvanceFilter.select_section(self,input_section="Section 1",filter_no='ui-select-choices-7')
        
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/div/ul/span/li/a")
        x_icon_displayed = x_icon.is_displayed()

        assert x_icon_displayed == True

        x_icon.click()

        select_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/button[1]")
        select_all_button.click()

        deselect_all_button = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/button[2]")
        deselect_all_button.click()

        location_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[5]/div/ul/li/input")
        return_default_value = location_inputbox.get_attribute("placeholder")

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_job_level(self):
        """Check response "Job level" input box.""" 

        AdvanceFilter.button_click(self)
        sleep(5)
        AdvanceFilter.select_job_level(self,input_data="Monthlies",request_type= 'filter.job_level')
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/abbr")
        x_icon.click()

        job_level_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_employee(self):
        """Check response "Employee" input box.""" 

        AdvanceFilter.button_click(self)
        sleep(5)
        input_employee = "Sample, Sample1"
        AdvanceFilter.select_employee(self,input_employee)

        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/abbr")
        x_icon.click()

        employee_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[7]/div/div[2]/a/span[1]")
        return_default_value = employee_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_search_button(self):

        AdvanceFilter.button_click(self)
        sleep(5)

        self.driver.close()

    def test_advance_filter_reset_button(self):
        """Check response "Reset" button.""" 

        AdvanceFilter.button_click(self)
        sleep(5)
        AdvanceFilter.select_job_level(self,input_data="Monthlies",request_type= 'filter.job_level')
        AdvanceFilter.click_reset_button(self)
        sleep(5)

        job_level_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_inputting_job_level(self):
        """Check response "Job Level" input box.""" 

        AdvanceFilter.button_click(self)
        sleep(5)

        input_job_level="Monthlies"
        AdvanceFilter.select_job_level(self,input_job_level,request_type= 'filter.job_level')
        x_icon = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/abbr")
        x_icon.click()

        job_level_inputbox = self.driver.find_element_by_xpath("//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div[3]/tabletoolstrans/div/div/div/div/div[2]/div/div/div/span[1]/div[6]/div/a/span[1]")
        return_default_value = job_level_inputbox.text

        assert return_default_value == "ALL"

        self.driver.close()

    def test_advance_filter_reset_button(self):
        """Check response "Reset" button.""" 

        AdvanceFilter.button_click(self)
        sleep(5)

        input_job_level="Monthlies"
        input_employee = "Sample, Sample1"
        AdvanceFilter.select_job_level(self,input_job_level,request_type= 'filter.job_level')
        AdvanceFilter.select_employee(self,input_employee)
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

    def test_recurring_earnings_caret_dropdown_button(self): 
        """Check response "Caret" dropdown button.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@class='col-sm-6 row pull-right']/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()

        caret_dropdown = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']")

        assert caret_dropdown.is_displayed()

    def test_recurring_earnings_export_button(self, capsys): 
        """Check response "Export" dropdown option.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@class='col-sm-6 row pull-right']/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()
        caret_dropdown = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']")
        assert caret_dropdown.is_displayed()


        export_button = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']/li")
        export_button.click()
        sleep(1)

        new_tab = requests.get("https://yp.yahshuasupport.com/export/common_tables/employee_additional_pay?fields={%22employeeid%22:{%22display%22:%22Employee%20ID%22,%22sort%22:1,%22selected%22:true,%22default%22:true,%22uneditable%22:true,%22value%22:%22employeeid%22},%22lastname%22:{%22display%22:%22Last%20Name%22,%22sort%22:2,%22selected%22:true,%22value%22:%22lastname%22},%22firstname%22:{%22display%22:%22First%20Name%22,%22sort%22:3,%22selected%22:true,%22value%22:%22firstname%22},%22middlename%22:{%22display%22:%22Middle%20Name%22,%22sort%22:4,%22selected%22:true,%22value%22:%22middlename%22},%22total_employee_additional_pay%22:{%22display%22:%22Total%22,%22sort%22:5,%22selected%22:true,%22default%22:true,%22value%22:%22total_employee_additional_pay%22}}&filters=%7B%22records_per_page%22%3A10%2C%22view_by%22%3A%22Summary%22%2C%22typee%22%3A%22Additional%20Pay%22%2C%22type_ids%22%3A%5B%5D%2C%22pagination%22%3A%7B%22limit%22%3A10%2C%22current_page%22%3A1%2C%22total_records%22%3A1%2C%22total_pages%22%3A1%2C%22limit_options_orig%22%3A%5B20%2C50%2C100%2C150%5D%2C%22limit_options%22%3A%5B20%2C50%2C100%2C150%2C1%5D%7D%2C%22show_hide_column%22%3Atrue%2C%22show_inactive%22%3Afalse%2C%22name%22%3A%22Sample1%22%7D&email=false&view_by=%22Summary%22")

        assert 200 == new_tab.status_code

    def test_recurring_earnings_import_button(self): 
        """Click "Import" dropdown option.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@class='col-sm-6 row pull-right']/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()
        caret_dropdown = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']")
        assert caret_dropdown.is_displayed()


        import_button = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']/li[2]")
        import_button.click()
        sleep(5)

        new_tab = requests.get("https://yp.yahshuasupport.com/settings/imports/#import_employee_additional_pay")

        assert 200 == new_tab.status_code

    def test_recurring_earnings_print_button(self): 
        """Check response clicking "Print" button.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@class='col-sm-6 row pull-right']/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()
        caret_dropdown = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']")
        assert caret_dropdown.is_displayed()


        print_button = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']/li[4]")
        print_button.click()
        sleep(5)


        new_tab = requests.get("https://yp.yahshuasupport.com/employees/additional_pay_and_deductions/additional_pays/prints/?filters=%7B%22records_per_page%22:10,%22view_by%22:%22Summary%22,%22typee%22:%22Additional%20Pay%22,%22type_ids%22:[],%22pagination%22:%7B%22limit%22:10,%22current_page%22:1,%22total_records%22:1,%22total_pages%22:1,%22limit_options_orig%22:[20,50,100,150],%22limit_options%22:[20,50,100,150,1]%7D,%22show_hide_column%22:true,%22show_inactive%22:false,%22name%22:%22Sample1%22%7D&columns=%7B%22employeeid%22:%7B%22display%22:%22Employee%20ID%22,%22sort%22:1,%22selected%22:true,%22default%22:true,%22uneditable%22:true,%22value%22:%22employeeid%22%7D,%22lastname%22:%7B%22display%22:%22Last%20Name%22,%22sort%22:2,%22selected%22:true,%22value%22:%22lastname%22%7D,%22firstname%22:%7B%22display%22:%22First%20Name%22,%22sort%22:3,%22selected%22:true,%22value%22:%22firstname%22%7D,%22middlename%22:%7B%22display%22:%22Middle%20Name%22,%22sort%22:4,%22selected%22:true,%22value%22:%22middlename%22%7D,%22total_employee_additional_pay%22:%7B%22display%22:%22Total%22,%22sort%22:5,%22selected%22:true,%22default%22:true,%22value%22:%22total_employee_additional_pay%22%7D%7D&additional_pay_view_by=Summary&name=Sample1&inactive=false&print=yes")

        assert 200 == new_tab.status_code

    def test_recurring_earnings_delete_button(self): 
        """Check response clicking "Delete" button.""" 

        caret_button = self.driver.find_element(By.XPATH, "//*[@class='col-sm-6 row pull-right']/tabletoolstrans/div/div/div/button[3]")
        caret_button.click()
        caret_dropdown = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']")
        assert caret_dropdown.is_displayed()

        delete_button = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']/li[6]")
        delete_button.click()

        Confirmation.click_confirm_yes(self)
        sleep(2)

        expected_notif = 'Employee Additional Pay successfully removed.'

        actual_notif = self.driver.find_element(By.XPATH,"//*[@aria-label = 'Employee Additional Pay successfully removed']").text

        assert expected_notif == actual_notif






