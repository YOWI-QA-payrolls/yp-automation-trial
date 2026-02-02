import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import date as datetime

from utils import search, dropdown, filter_effectivity, right_click, pagination, auto_approval, toast_container, filters, records, filter_by_effectivity
from utils.attachment import recommender_attachment as attachment
from utils.date import approver_date as date
from utils.set_site import approver_set_site as set_site

class Setup():
    def setup_method(self):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()

        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)
        set_site.login(self)

        approval = self.driver.find_element(By. XPATH, '//*[@id="approval_list"]')
        officialBusiness_approval = self.driver.find_element(By.XPATH, '//*[@id="undertime_overtime_approval"]/a')
        approval.click()
        officialBusiness_approval.click()

        officialBusiness_section = self.driver.find_element(By.XPATH, "//*[@ui-sref='officialbusiness_approval']")
        officialBusiness_section.click()
        sleep(7)

    def teardown_method(self):
        self.driver.quit()

class TestDateField(Setup):
    ## Test Date Field functionality
    # @pytest.mark.skip(reason="passed")
    def test_date_field_select_date_in_calendar(self):
        """Check response when choosing specific date in the calendar icon"""

        expected_text_1 = "05/03/2022"
        input_date_from_xpath = "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/div[1]/ul/li[1]/div/div/div/table/tbody/tr[1]/td[3]/button/span"
        
        date_from_calendar_clicked = date.date_from_calendar_icon(self)
        date.input_date_from(self, input_date_from_xpath)
        actual_text_1 = date.date_from_field_input_box(self, date_from_input="")

        expected_text_2 = "05/19/2022"
        input_date_to_xpath = "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/div[2]/ul/li[1]/div/div/div/table/tbody/tr[3]/td[5]/button/span"
        
        date_to_calendar_clicked = date.date_to_calendar_icon(self)
        date.input_date_to(self, input_date_to_xpath)
        actual_text_2 = date.date_to_field_input_box(self, date_to_input="")

        assert date_from_calendar_clicked == True
        assert expected_text_1 == actual_text_1
        assert date_to_calendar_clicked == True
        assert expected_text_2 == actual_text_2

        self.driver.close()
    
    # @pytest.mark.skip(reason="passed")
    def test_date_field_calendar_icon(self):
        """Check response when clicking calendar icon on both date from and to"""

        expected_text = datetime.today().strftime("%m/%d/%Y")
        date_from_calendar_clicked = date.date_from_calendar_icon(self)
        date.date_from_today(self)
        actual_text_1 = date.date_from_field_input_box(self, date_from_input="")

        date_to_calendar_icon_clicked = date.date_to_calendar_icon(self)
        date.date_to_today(self)
        actual_text_2 = date.date_to_field_input_box(self, date_to_input="")

        assert date_from_calendar_clicked == True
        assert expected_text == actual_text_1
        assert date_to_calendar_icon_clicked == True
        assert expected_text == actual_text_2

        self.driver.close()
    
    @pytest.mark.skip(reason="passed")
    def test_date_field_when_no_entry(self):
        """Check response when there's no entry"""

        input_data = ["Sample1", "Sample2", "Sample3", "Sample4"]

        is_search_icon_clicked = date.date_field_search_icon(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)
        
        assert is_search_icon_clicked == True
        assert displayed_relevant_result == True

        self.driver.close()

    # @pytest.mark.skip(reason="not as expected")
    @pytest.mark.xfail(reason="not as expected")
    def test_date_field_string_input(self):
        """Check response when entering string type in the 'date from' and 'to' box"""

        date_from_input = "Mar 15, 2022"
        date.date_from_field_input_box(self, date_from_input)
        is_date_from_correct_format = date.check_format_date(date_from_input)

        date_to_input = "Mar 29, 2022"
        date.date_to_field_input_box(self, date_to_input)
        is_date_to_correct_format = date.check_format_date(date_to_input)

        assert is_date_from_correct_format == True  # False
        assert is_date_to_correct_format == True    # False

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_date_field_invalid_date_input(self):
        """Check response when entering invalid date"""

        expected_text = "Please indicate Date From."
        date_from_input = "02/30/2022"
        actual_date_from_input = date.date_from_field_input_box(self, date_from_input)

        date_to_input = "03/17/2022"
        actual_date_to_input = date.date_to_field_input_box(self, date_to_input)
        is_search_icon_clicked = date.date_field_search_icon(self)
        actual_text = toast_container.text(self)

        assert date_from_input == actual_date_from_input
        assert date_to_input == actual_date_to_input
        assert is_search_icon_clicked == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_date_field_invalid_date_range(self):
        """Check response when entering invalid date range"""

        expected_text = "Please indicate correct date range."
        date_from_input = "03/15/2022"
        actual_date_from_input = date.date_from_field_input_box(self, date_from_input)

        date_to_input = "12/31/2021"
        actual_date_to_input = date.date_to_field_input_box(self, date_to_input)
        is_search_icon_clicked = date.date_field_search_icon(self)
        actual_text = toast_container.text(self)

        assert date_from_input == actual_date_from_input
        assert date_to_input == actual_date_to_input
        assert is_search_icon_clicked == True
        assert expected_text == actual_text

        self.driver.close()

class TestSearch(Setup):
    ## Test Search Functionality
    @pytest.mark.skip(reason="passed")
    def test_search_entering_valid_entry(self):
        """Check response when searching a valid entry"""

        input_data = "Sample2"

        actual_data = search.box_function(self, input_data)
        is_search_icon_clicked = search.click_icon_button(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)
        
        assert input_data == actual_data
        assert is_search_icon_clicked == True
        assert displayed_relevant_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_entering_invalid_entry(self):
        """Check response when searching an invalid entry"""

        input_data = "Yason"

        actual_data = search.box_function(self, input_data)
        is_search_icon_clicked = search.click_icon_button(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)

        assert input_data == actual_data
        assert is_search_icon_clicked == True
        assert displayed_relevant_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_entering_special_char_entry(self):
        """Check response when entering special characters and numbers"""

        input_data = "!@#123"

        actual_data = search.box_function(self, input_data)
        is_search_icon_clicked = search.click_icon_button(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)

        assert input_data == actual_data
        assert is_search_icon_clicked == True
        assert displayed_relevant_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_icon_function(self):
        """Check response when clicking search icon"""

        input_data = ["Sample1", "Sample2", "Sample3", "Sample4"]
        
        is_search_icon_clicked = search.click_icon_button(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)

        assert is_search_icon_clicked == True
        assert displayed_relevant_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_clicking_enter_key(self):
        """Check response if "Enter key" (keyboard) can be used to enter search data"""

        input_data = "Sample2"

        actual_data = search.click_enter_function(self, input_data)
        displayed_relevant_result = search.check_all_search_results(self, input_data)

        assert input_data == actual_data
        assert displayed_relevant_result == True

        self.driver.close()

class TestDropdown(Setup):
    ## Test Dropdown Functionality
    @pytest.mark.skip(reason="passed")
    def test_dropdown_arrow_icon_function(self):
        """ Check response when clicking the dropdown arrow icon """

        dropdown_icon_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/button[3]")
        dropdown_icon_button.click()
        sleep(3)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_3 is True : are_options_displayed = True

        assert are_options_displayed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_dropdown_export_function(self):
        """ Check response when clicking 'Export' """

        dropdown_icon_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/button[3]")
        dropdown_icon_button.click()
        sleep(3)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_3 is True : are_options_displayed = True
        file_downloaded = dropdown.export_option(self)

        assert are_options_displayed == True
        assert file_downloaded == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_dropdown_print_function(self):
        """ Check response when clicking 'Print' """

        expected_text = "Official Business Approval"

        dropdown_icon_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/button[3]")
        dropdown_icon_button.click()
        sleep(3)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_3 is True : are_options_displayed = True
        actual_text = dropdown.print_option(self)
        sleep(7)

        assert are_options_displayed == True
        assert expected_text == actual_text

        self.driver.close()

class TestfilterEffectivityDate(Setup):
    ## Test Filter by effectivity date Functionality
    @pytest.mark.skip(reason="passed")
    def test_filter_by_effectivity_function(self):
        """ Check response when clicking 'Filter by Effectivity date' checkbox """

        is_selected = filter_by_effectivity.checkbox(self)

        assert is_selected == False

        self.driver.close()

class TestApply(Setup):
    ## Test Apply Functionality
    @pytest.mark.skip(reason="passed")
    def test_apply_specific_employee_selected(self):
        """ Check response when applying auto approval when no employee is selected """

        expected_text = "Request successfully approved."
        expected_approval = "Approve"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        option_displayed = auto_approval.dropdown(self)
        actual_approval = auto_approval.approve_option(self)
        select_record_1 = self.driver.find_element(By.ID, 'auto_approval_0')
        select_record_1.click()
        record_1_selected = select_record_1.is_selected()
        sleep(3)
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert option_displayed == True
        assert expected_approval == actual_approval
        assert record_1_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_apply_multiple_employee_selected(self):
        """ Check response when applying auto approval when no employee is selected """

        expected_text = "Request successfully approved."
        expected_approval = "Approve"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        option_displayed = auto_approval.dropdown(self)
        actual_approval = auto_approval.approve_option(self)
        select_all_record = self.driver.find_element(By.ID, 'auto_approval_0')
        select_all_record.click()
        select_record_1 = self.driver.find_element(By.ID, 'auto_approval_1')
        select_record_1.click()
        all_record_selected = select_all_record.is_selected() and select_record_1.is_selected()
        sleep(3)
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert option_displayed == True
        assert expected_approval == actual_approval
        assert all_record_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text

        self.driver.close()
    
    @pytest.mark.skip(reason="passed")
    def test_apply_no_employee_selected(self):
        """ Check response when applying auto approval when no employee is selected """

        expected_text = "No selected request to auto approve."
        expected_option = "Approve"

        option_displayed = auto_approval.dropdown(self)
        actual_option = auto_approval.approve_option(self)
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        actual_text = toast_container.text(self)

        assert option_displayed == True
        assert expected_option == actual_option
        assert confirmation_popped_up == True
        assert expected_text == actual_text

        self.driver.close()

class TestAutoApproval(Setup): 
    ## Test Auto Approval - Approve Functionality
    @pytest.mark.skip(reason="passed")
    def test_auto_approval_function(self):
        """ Check response when clicking "Approve" dropdown """

        expected_text = "Approve"
        option_displayed = auto_approval.dropdown(self)
        actual_text = auto_approval.approve_option(self)

        assert option_displayed == True
        assert expected_text == actual_text

        self.driver.close()

class TestRecordsPerPage(Setup):
    ## Test Records per Page Functionality
    @pytest.mark.skip(reason="passed")
    def test_records_per_page_function(self):
        """ Check response when clicking 'Records per page' button """
        
        expected_text = "5"
        are_options_displayed = records.per_page_dropdown(self)
        actual_text = records.per_page_option_5(self)
        is_option_clicked = actual_text[0]

        assert are_options_displayed == True
        assert is_option_clicked == True
        assert expected_text == actual_text[1]
        
        self.driver.close()

class TestRecordsField(Setup):
    ## Test Records Field Functionality
    @pytest.mark.skip(reason="passed")
    def test_records_checkbox(self):
        """ Check response when clicking Record checkbox """

        is_checkbox_selected = records.select_all(self)

        assert is_checkbox_selected == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_clicking_record_row(self):
        """ Check response when clicking a record row """

        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        dialog_displayed = records.click_record_row(self, record_row_xpath)

        assert dialog_displayed == True
        
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_official_business_approval_request_approve_recommended_record(self):
        """ Check response when approving a reviewed and recommended record row """

        expected_text = "Request successfully approved."
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        confirmation_popped_up = records.confirm_yes_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert dialog_displayed == True
        assert approve_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text
        
        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_records_official_business_approval_request_record_in_hours_edit_date(self):
        """ Check response when clicking "Overtime Approval Request" dialog """

        expected_text = "Request successfully approved."
        expected_data = "03/31/2022"
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        input_date_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[3]/div[1]/p[1]/div/ul/li[1]/div/div/div/table/tbody/tr[5]/td[5]/button"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        calendar_clicked = records.click_calendar_icon(self)
        actual_data = records.edit_date(self, input_date_xpath)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        confirmation_popped_up = records.confirm_yes_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert dialog_displayed == True
        assert calendar_clicked == True
        assert expected_data == actual_data
        assert approve_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text
        
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_official_business_approval_request_record_in_day_edit_date(self):
        """ Check response when clicking "Overtime Approval Request" dialog """

        expected_text = "Request successfully approved."
        expected_data = "04/27/2022"
        no_of_ob_days = "1"
        record_row_xpath = "//*[@id='table']/tbody/tr[2]/td[4]"
        input_date_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/span/span/div/div[2]/p/div/ul/li[1]/div/div/div/table/tbody/tr[5]/td[4]/button"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        actual_number_of_days = records.ob_change_number_of_day(self, no_of_ob_days)
        calendar_clicked = records.ob_click_calendar_icon(self)
        actual_data = records.ob_edit_date(self, input_date_xpath)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        confirmation_popped_up = records.confirm_yes_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert dialog_displayed == True
        assert actual_number_of_days == no_of_ob_days
        assert calendar_clicked == True
        assert expected_data == actual_data
        assert approve_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text
        
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_official_business_approval_request_recommended_record_edit_time(self):
        """ Check response when changing the number of hours """

        expected_text = "Request successfully approved."
        input_time_from = ["01","30"]
        input_time_to = ["05","00"]
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        actual_time_from = records.ob_edit_time_from(self, input_time_from)
        actual_time_to = records.ob_edit_time_to(self, input_time_to)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        confirmation_popped_up = records.confirm_yes_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert dialog_displayed == True
        assert input_time_from == actual_time_from
        assert input_time_to == actual_time_to
        assert approve_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text
        
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_official_business_approval_request_not_recommended_record(self):
        """ Check response when approving a record row without reviewed and/or recommended """

        expected_text_1 = "This requests has not yet reviewed and recommended."
        expected_text_2 = "This requests has not yet recommended."
        record_row_xpath = "//*[@id='table']/tbody/tr[6]/td[4]"

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        actual_text = toast_container.text(self)

        assert dialog_displayed == True
        assert approve_selected == True
        assert actual_text == expected_text_1 or expected_text_2

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_close_button(self):
        """ Check response when clicking the 'Close' button from Overtime Approval Request """

        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        dialog_displayed = records.click_record_row(self, record_row_xpath)
        dialog_closed = records.close_button(self)

        assert dialog_displayed == True
        assert dialog_closed == True
        
        self.driver.close()
    
    @pytest.mark.skip(reason="passed")
    def test_records_pagination(self):
        """ Check response when clicking Previous/Page/Next button """
        
        expected_text = "5"
        are_options_displayed = records.per_page_dropdown(self)
        actual_text = records.per_page_option_5(self)
        next_button_clicked = pagination.next_button(self)
        previous_button_clicked = pagination.previous_button(self)

        assert are_options_displayed == True
        assert expected_text == actual_text[1]
        assert next_button_clicked == True
        assert previous_button_clicked == True
        
        self.driver.close()