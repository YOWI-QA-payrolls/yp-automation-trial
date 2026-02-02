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
        holiday_approval = self.driver.find_element(By.XPATH, '//*[@id="undertime_overtime_approval"]/a')
        approval.click()
        holiday_approval.click()

        holiday_section = self.driver.find_element(By.XPATH, "//*[@ui-sref='workonholiday_approval']")
        holiday_section.click()
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
    def test_calendar_icon(self):
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
        """Check response when searching an invalid entry"""

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

class TestDropDown(Setup):
    ## Test Dropdown Functionality
    @pytest.mark.skip(reason="passed")
    def test_dropdown_arrow_icon_function(self):
        """ Check response when clicking the dropdown arrow icon """

        are_options_displayed = dropdown.icon_button(self)

        assert are_options_displayed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_export_function(self):
        """ Check response when clicking 'Export' """

        are_options_displayed = dropdown.icon_button(self)
        file_downloaded = dropdown.export_option(self)

        assert are_options_displayed == True
        assert file_downloaded == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_option(self):
        """ Check response when clicking 'Summary Report Export' button """

        are_options_displayed = dropdown.icon_button(self)
        dialog_displayed = dropdown.summary_report_export_option(self)

        assert are_options_displayed == True
        assert dialog_displayed == True

        self.driver.close()
    
    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_close_button(self):
        """ Check response when clicking 'Close' button of the Summary Report Export dialog """

        are_options_displayed = dropdown.icon_button(self)
        dialog_displayed = dropdown.summary_report_export_option(self)
        is_dialog_closed = dropdown.summary_report_export_close_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_dialog_closed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_valid_date_input(self):
        """ Check response when entering valid input in 'Period from', 'Period to', 'Cut-off' """
        
        expected_period_from = "05/01/2022"
        expected_period_to = "05/15/2022"
        expected_cut_off = "05/31/2022"
        period_from_input = "/html/body/div[1]/div/div/div/div[2]/div/div[2]/p[1]/div/ul/li[1]/div/div/div/table/tbody/tr[1]/td[1]/button"
        period_to_input =  "/html/body/div[1]/div/div/div/div[2]/div/div[3]/p[1]/div/ul/li[1]/div/div/div/table/tbody/tr[3]/td[1]/button"
        cut_off_input =  "/html/body/div[1]/div/div/div/div[2]/div/div[4]/p[1]/div/ul/li[1]/div/div/div/table/tbody/tr[5]/td[3]/button"
        
        are_options_displayed = dropdown.icon_button(self)
        dialog_displayed = dropdown.summary_report_export_option(self)
        period_from_calendar_displayed = dropdown.summary_report_export_period_from_calendar(self)
        actual_period_from = dropdown.summary_report_export_calendar_input_period_from(self, period_from_input)
        period_to_calendar_displayed = dropdown.summary_report_export_period_to_calendar(self)
        actual_period_to = dropdown.summary_report_export_calendar_input_period_to(self, period_to_input)
        cut_off_calendar_displayed = dropdown.summary_report_export_cut_off_calendar(self)
        actual_cut_off = dropdown.summary_report_export_calendar_input_cut_off(self, cut_off_input)
        dropdown.summary_report_export_button(self)
        file_downloaded = dropdown.check_if_file_downloaded()

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert period_from_calendar_displayed == True
        assert expected_period_from == actual_period_from
        assert period_to_calendar_displayed == True
        assert expected_period_to == actual_period_to
        assert cut_off_calendar_displayed == True
        assert expected_cut_off == actual_cut_off
        assert file_downloaded == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_invalid_date_input(self):
        """ Check response when entering valid input in 'Period from', 'Period to', 'Cut-off' """
        
        expected_text = "Please input Period From."
        period_from_input = "yason"
        period_to_input =  "yason"
        cut_off_input =  "yason"
        
        are_options_displayed = dropdown.icon_button(self)
        dialog_displayed = dropdown.summary_report_export_option(self)
        actual_period_from = dropdown.summary_report_export_period_from_input_box(self, period_from_input)
        actual_period_to = dropdown.summary_report_export_period_to_input_box(self, period_to_input)
        actual_cut_off = dropdown.summary_report_export_cut_off_input_box(self, cut_off_input)
        dropdown.summary_report_export_button(self)
        actual_text = toast_container.text(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert period_from_input == actual_period_from
        assert period_to_input == actual_period_to
        assert cut_off_input == actual_cut_off
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_special_char_date_input(self):
        """ Check response when entering valid input in 'Period from', 'Period to', 'Cut-off' """
        
        expected_text = "Please input Period From."
        period_from_input = "!@#123"
        period_to_input =  "!@#123"
        cut_off_input =  "!@#123"
        
        are_options_displayed = dropdown.icon_button(self)
        dialog_displayed = dropdown.summary_report_export_option(self)
        actual_period_from = dropdown.summary_report_export_period_from_input_box(self, period_from_input)
        actual_period_to = dropdown.summary_report_export_period_to_input_box(self, period_to_input)
        actual_cut_off = dropdown.summary_report_export_cut_off_input_box(self, cut_off_input)
        dropdown.summary_report_export_button(self)
        actual_text = toast_container.text(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert period_from_input == actual_period_from
        assert period_to_input == actual_period_to
        assert cut_off_input == actual_cut_off
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_print_function(self):
        """ Check response when clicking 'Print' """

        expected_text = "Work on holiday Approval"

        are_options_displayed = dropdown.icon_button(self)
        actual_text = dropdown.print_option(self)
        sleep(7)

        assert are_options_displayed == True
        assert expected_text == actual_text

        self.driver.close()

class TestEffectivityDate(Setup):
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
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        select_record_1 = self.driver.find_element(By.ID, 'auto_approval_0')
        select_record_1.click()
        record_1_selected = select_record_1.is_selected()
        sleep(3)
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        sleep(1)
        actual_text = toast_container.text(self)
        sleep(3)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert record_1_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_apply_multiple_employee_selected(self):
        """ Check response when applying auto approval when no employee is selected """

        expected_text = "Request successfully approved."
        expected_status = "Recommended"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        select_all_record = self.driver.find_element(By.ID, 'auto_approval_0')
        select_all_record.click()
        select_record_1 = self.driver.find_element(By.ID, 'auto_approval_1')
        select_record_1.click()
        all_record_selected = select_all_record.is_selected() and select_record_1.is_selected()
        sleep(3)
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        sleep(1)
        actual_text = toast_container.text(self)
        sleep(3)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert all_record_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text

        self.driver.close()
    
    @pytest.mark.skip(reason="passed")
    def test_apply_no_employee_selected(self):
        """ Check response when applying auto approval when no employee is selected """

        expected_text = "No selected request to auto approve."
        confirmation_popped_up = auto_approval.apply_button(self)
        auto_approval.confirm_button(self)
        sleep(3)
        actual_text = toast_container.text(self)

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
    def test_records_holiday_approval_request_approve_recommended_record(self):
        """ Check response when approving a reviewed and recommended record row """

        expected_text = "Request successfully approved."
        expected_status = "Recommended"
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"

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

    @pytest.mark.skip(reason="passed")
    def test_records_holiday_approval_request_recommended_record_edit_date(self):
        """ Check response when clicking "Overtime Approval Request" dialog """

        expected_text = "Request successfully approved."
        expected_data = "12/25/2022"
        expected_status = "Recommended"
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"
        input_date_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[1]/p[1]/div/ul/li[1]/div/div/div/table/tbody/tr[4]/td[2]/button"

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
    def test_records_holiday_approval_request_recommended_record_edit_hours(self):
        """ Check response when changing the number of hours """

        expected_text = "Request successfully approved."
        expected_status = "Recommended"
        input_data = "6"
        record_row_xpath = "//*[@id='table']/tbody/tr[1]/td[4]"

        # Set the advance filter to only show the recommended records
        advance_filter_button_clicked = filters.advance_filter_function(self)
        actual_status = filters.recommended_status_only(self)
        search_button_clicked = filters.advance_filter_function_search(self)

        dialog_displayed = records.click_record_row(self, record_row_xpath)
        actual_data = records.change_number_of_hours(self, input_data)
        approve_selected = records.approve_record(self)
        records.submit_button(self)
        confirmation_popped_up = records.confirm_yes_button(self)
        actual_text = toast_container.text(self)

        assert advance_filter_button_clicked == True
        assert expected_status == actual_status
        assert search_button_clicked == True
        assert dialog_displayed == True
        assert input_data == actual_data
        assert approve_selected == True
        assert confirmation_popped_up == True
        assert expected_text == actual_text
        
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_records_holiday_approval_request_not_recommended_record(self):
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

class TestRightClick(Setup):
    ## Test Right Click Option
    @pytest.mark.skip(reason="passed")
    def test_right_click_view_logs_option(self):
        """ Check response when clicking 'View Logs' button """
        
        expected_text = "Dashboard"
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[4]")
        are_options_displayed = right_click.action(self, select_record)
        actual_text = right_click.view_logs_option(self)

        assert are_options_displayed == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_right_click_attach_option(self):
        """ Check response when clicking "Attach" button """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[4]")
        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)

        assert are_options_displayed == True
        assert dialog_displayed == True

        self.driver.close()

class TestAttachment(Setup):
    ## Test Attachment Functionality
    @pytest.mark.skip(reason="passed")
    def test_attachment_click_drop_files(self):
        """ Check response when clicking "drop files here to upload" """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")
        file_path = "C://Users/heyysson/Documents/OJT Files/sample.docx"
        expected_file_name = "sample.docx"

        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_attached = attachment.attach_file(self, file_path)
        actual_file_name = attachment.upload_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_file_attached[0] == True
        assert expected_file_name == actual_file_name

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_more_than_11_mb(self):
        """ Check response when uploading file more than 11MB """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")
        file_path = "C://Users/heyysson/Downloads/Telegram Desktop/quality handbook.pdf"

        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_attached = attachment.attach_file(self, file_path)
        error_dialog_displayed = is_file_attached[1]
        attachment.error_notif_ok_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_file_attached[0] == False
        assert error_dialog_displayed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_less_than_10_mb(self):
        """ Check response when uploading file less than 10MB """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")
        file_path = "C://Users/heyysson/Documents/OJT Files/sample.docx"
        expected_file_name = "sample.docx"

        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_attached = attachment.attach_file(self, file_path)
        actual_file_name = attachment.upload_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_file_attached[0] == True
        assert expected_file_name == actual_file_name

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_button(self):
        """ Check response when clicking 'Upload' button """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")
        file_path = "C://Users/heyysson/Documents/OJT Files/sample.docx"
        expected_file_name = "sample.docx"

        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_attached = attachment.attach_file(self, file_path)
        actual_file_name = attachment.upload_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_file_attached[0] == True
        assert expected_file_name == actual_file_name

        self.driver.close()

    # @pytest.mark.skip(reason="not as expected")
    @pytest.mark.xfail(reason="not as expected")
    def test_attachment_download_all_button(self):
        """ Check response when clicking "Download all" button """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")

        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_downloaded = attachment.download_all(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_file_downloaded == True   # file not downloaded

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_close_button(self):
        """ Check response when clicking 'Close' button """
        
        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[3]/td[4]")
        
        are_options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_dialog_closed = attachment.close_button(self)

        assert are_options_displayed == True
        assert dialog_displayed == True
        assert is_dialog_closed == True

        self.driver.close()