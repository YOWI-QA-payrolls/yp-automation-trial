import pytest
from datetime import date as datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import searchbox, filter_effectivity, apply, right_click, pagination, prompt, auto_approval_review, record_per_page, record_field
from utils.advance_filter import reviewer_advance_filter_dropdown as advance_filter
from utils.approval_dialog import reviewer_approval_dialog as approval_dialog
from utils.attachment import reviewer_attachment as attachment
from utils.date import reviewer_date as date
from utils.set_site import reviewer_set_site as set_site


class Setup():

    def setup_method(self, method):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        # self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(width=1552, height=849)
        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)
        set_site.login(self)

        approval = self.driver.find_element(By.XPATH, '//*[@id="approval_list"]')
        approval_list = self.driver.find_element(By.XPATH, '//*[@id="undertime_overtime_approval"]/a')

        approval.click()
        approval_list.click()

        undertime_approval = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/nav/ul/li[2]/a')
        undertime_approval.click()
        sleep(10)

    sleep(15)

    def teardown_method(self, method):
        self.driver.quit()

class TestDate(Setup):
    # Check Date Field Functionality
    # @pytest.mark.skip(reason="passed")
    def test_specific_date_in_the_calendar(self):
        """Check response when choosing specific date in the calendar"""

        expected_text_1 = "05/06/2022"
        input_date_from_xpath = "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/" \
                                "tabletoolsdaterange2/p/div[1]/ul/li[1]/div/div/div/table/tbody/tr[1]/td[6]/button"
        date_from_icon = date.date_from(self)
        date.input_date_from(self, input_date_from_xpath)
        actual_text_1 = date.date_from_input_box(self, date_from_input="")
        sleep(3)

        expected_text_2 = "05/06/2022"
        input_date_to_xpath = "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/" \
                              "tabletoolsdaterange2/p/div[2]/ul/li[1]/div/div/div/table/tbody/tr[1]/td[6]/button"
        date_to_icon = date.date_to(self)
        date.input_date_to(self, input_date_to_xpath)
        actual_text_2 = date.date_to_input_box(self, date_to_input="")
        sleep(3)

        assert True == date_from_icon
        assert expected_text_1 == actual_text_1
        assert True == date_to_icon
        assert expected_text_2 == actual_text_2
        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_calendar_icon_on_date_from_and_date_to(self):
        """Check response when clicking calendar icon"""

        expected_text = datetime.today().strftime("%m/%d/%Y")
        date_from_icon = date.date_from(self)
        date.date_from_today(self)
        actual_text_1 = date.date_from_input_box(self, date_from_input="")
        sleep(3)
        date_to_icon = date.date_to(self)
        date.date_to_today(self)
        actual_text_2 = date.date_to_input_box(self, date_to_input="")
        sleep(3)
        assert date_from_icon == True
        assert expected_text == actual_text_1
        assert date_to_icon == True
        assert expected_text == actual_text_2
        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_response_when_no_entry_to_both_date_from_and_to(self):
        """Check response when there's no entry to both date from and to"""

        input_data = ["Sample1", "Sample2", "Sample3", "Sample4"]
        date_search_icon = date.search_icon(self)
        sleep(3)
        displayed_relevant_result = searchbox.check_all_result(self, input_data)
        assert date_search_icon == True
        assert displayed_relevant_result == True
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_of_string_type_input(self):
        """Check response when entering string type in the date from and to box"""

        expected_text_1 = "October 19, 2021"
        date_from_input = "October 19, 2021"
        date.date_from_field(self, date_from_input)
        actual_text_1 = date.date_from_input_box(self, date_from_input="")
        time.sleep(5)
        expected_text_2 = "October 19, 2021"
        date_to_input = "October 19, 2021"
        date.date_to_field(self, date_to_input)
        actual_text_2 = date.date_from_input_box(self, date_from_input="")

        date.search_icon(self)
        time.sleep(5)
        assert expected_text_1 == actual_text_1
        assert expected_text_2 == actual_text_2
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_when_entering_invalid_date(self):
        """Check response when entering invalid date"""

        expected_text = "Please indicate Date From."
        expected_text_1 = "04/32/2022"
        date_from_input = "04/32/2022"
        date.date_from_field(self, date_from_input)
        actual_text_1 = date.date_from_input_box(self, date_from_input="")
        time.sleep(5)

        expected_text_2 = "04/01/2022"
        date_to_input = "04/01/2022"
        date.date_to_field(self, date_to_input)
        actual_text_2 = date.date_to_input_box(self, date_to_input="")

        date.search_icon(self)
        time.sleep(5)

        assert expected_text_1 == actual_text_1
        assert expected_text_2 == actual_text_2
        actual_text = prompt.text(self)
        assert expected_text == actual_text
        sleep(3)
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_of_invalid_date_range(self):
        """Check response when entering invalid date range"""

        expected_text = "Please indicate correct date range."

        expected_text_1 = "10/19/2021"
        date_from_input = "10/19/2021"
        date.date_from_field(self, date_from_input)
        actual_text_1 = date.date_from_input_box(self, date_from_input="")
        time.sleep(5)

        expected_text_2 = "10/01/2021"
        date_to_input = "10/01/2021"
        date.date_to_field(self, date_to_input)
        actual_text_2 = date.date_to_input_box(self, date_to_input="")

        date.search_icon(self)
        time.sleep(5)

        assert expected_text_1 == actual_text_1
        assert expected_text_2 == actual_text_2
        actual_text = prompt.text(self)
        assert expected_text == actual_text
        sleep(3)
        self.driver.close()

class TestSearch(Setup):
    # Check Search Functionality
    @pytest.mark.skip(reason="passed")
    def test_search_entering_valid_entry(self):
        """Check response when searching a valid entry"""

        input_data = "Sample1"

        actual_input = searchbox.search_box_function(self, input_data)
        search_icon_clicked = searchbox.search_icon(self)
        data_search_result = searchbox.check_all_result(self, input_data)

        assert input_data == actual_input
        assert search_icon_clicked == True
        assert data_search_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_entering_invalid_entry(self):
        """Check response when searching an invalid entry"""

        input_data = "not found in database"

        actual_input = searchbox.search_box_function(self, input_data)
        search_icon_clicked = searchbox.search_icon(self)
        data_search_result = searchbox.search_result(self, input_data)

        assert input_data == actual_input
        assert search_icon_clicked == True
        assert data_search_result == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_entering_special_char_and_numbers(self):
        """Check response when entering string type in the date from and to box"""

        input_data = "@!&123"

        actual_input = searchbox.search_box_function(self, input_data)
        search_icon_clicked = searchbox.search_icon(self)
        data_search_result = searchbox.search_result(self, input_data)

        assert input_data == actual_input
        assert search_icon_clicked == True
        assert data_search_result == True

        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_search_icon(self):
        """Check response when clicking search icon"""

        input_data = ["Sample1", "Sample2", "Sample3", "Sample4"]

        search_icon_clicked = searchbox.search_icon(self)
        displayed_relevant_result = searchbox.check_all_result(self, input_data)
        assert search_icon_clicked == True
        assert displayed_relevant_result == True
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_search_enter_key(self):
        """Check response if "Enter key" can be used to enter search data"""

        input_data = "Sample1"
        search_enter_key = searchbox.enter_key(self, input_data)
        data_search_result = searchbox.check_all_result(self, input_data)

        assert search_enter_key == True
        assert data_search_result == True

        self.driver.close()

    # Check Advance Filter Dropdown Functionality
    @pytest.mark.skip(reason="passed")
    def test_dropdown_arrow_icon(self):
        """Check response when clicking the dropdown arrow icon"""

        options_displayed = advance_filter.advance_filter_dropdown(self)
        sleep(3)
        assert options_displayed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_export_button(self):
        """Check response when clicking 'Export' button"""

        options_displayed = advance_filter.advance_filter_dropdown(self)
        file_downloaded = advance_filter.export_option(self)
        sleep(7)
        assert options_displayed == True
        assert file_downloaded == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export(self):
        """Check response when clicking 'Summary Report Export' button"""

        options_displayed = advance_filter.advance_filter_dropdown(self)
        dialog_displayed = advance_filter.summary_report_export_option(self)

        assert options_displayed == True
        assert dialog_displayed == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_close_button(self):
        """Check response when clicking 'Close' button - Summary report export"""

        options_displayed = advance_filter.advance_filter_dropdown(self)
        dialog_displayed = advance_filter.summary_report_export_option(self)
        dialog_closed = advance_filter.summary_report_export_close_button(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert dialog_closed == True
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_valid_input(self):
        """Check response when entering valid input in 'Period from', 'Period to', 'Cut-off'"""
        expected_period_from = "05/06/2022"
        expected_period_to = "05/07/2022"
        expected_cut_off = "05/31/2022"
        period_from_input = "/html/body/div[1]/div/div/div/div[2]/div/div[2]/p[1]/div/ul/li[1]/div/div/div/table/" \
                            "tbody/tr[1]/td[6]/button"
        period_to_input = "/html/body/div[1]/div/div/div/div[2]/div/div[3]/p[1]/div/ul/li[1]/div/div/div/table/" \
                          "tbody/tr[1]/td[7]/button"
        cut_off_input = "/html/body/div[1]/div/div/div/div[2]/div/div[4]/p[1]/div/ul/li[1]/div/div/div/table/" \
                        "tbody/tr[5]/td[3]/button"

        options_displayed = advance_filter.advance_filter_dropdown(self)
        dialog_displayed = advance_filter.summary_report_export_option(self)

        period_from_calendar = advance_filter.summary_report_export_period_from_calendar(self)
        actual_period_from = advance_filter.summary_report_export_calendar_input_period_from(self, period_from_input)
        period_to_calendar = advance_filter.summary_report_export_period_to_calendar(self)
        actual_period_to = advance_filter.summary_report_export_calendar_input_period_to(self, period_to_input)
        cut_off_calendar = advance_filter.summary_report_export_cut_off_calendar(self)
        actual_cut_off = advance_filter.summary_report_export_calendar_input_cut_off(self, cut_off_input)
        advance_filter.summary_report_export_button(self)
        file_downloaded = advance_filter.check_if_file_downloaded()

        assert options_displayed == True
        assert dialog_displayed == True
        assert period_from_calendar == True
        assert expected_period_from == actual_period_from
        assert period_to_calendar == True
        assert expected_period_to == actual_period_to
        assert cut_off_calendar == True
        assert expected_cut_off == actual_cut_off
        assert file_downloaded == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_invalid_input(self):
        """Check response when entering invalid input in 'Period from', 'Period to', 'Cut-off'"""
        expected_text = "Please input Period From."
        period_from_input = "invalid"
        period_to_input = "invalid"
        cut_off_input = "invalid"

        options_displayed = advance_filter.advance_filter_dropdown(self)
        dialog_displayed = advance_filter.summary_report_export_option(self)

        actual_period_from = advance_filter.summary_report_export_period_from_input_box(self, period_from_input)
        actual_period_to = advance_filter.summary_report_export_period_to_input_box(self, period_to_input)
        actual_cut_off = advance_filter.summary_report_export_cut_off_input_box(self, cut_off_input)
        advance_filter.summary_report_export_button(self)
        actual_text = prompt.text(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert period_from_input == actual_period_from
        assert period_to_input == actual_period_to
        assert cut_off_input == actual_cut_off
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_summary_report_export_special_character_input(self):
        """Check response when entering special character input in 'Period from', 'Period to', 'Cut-off'"""
        expected_text = "Please input Period From."
        period_from_input = "#$%123"
        period_to_input = "#$%123"
        cut_off_input = "#$%123"

        options_displayed = advance_filter.advance_filter_dropdown(self)
        dialog_displayed = advance_filter.summary_report_export_option(self)

        actual_period_from = advance_filter.summary_report_export_period_from_input_box(self, period_from_input)
        actual_period_to = advance_filter.summary_report_export_period_to_input_box(self, period_to_input)
        actual_cut_off = advance_filter.summary_report_export_cut_off_input_box(self, cut_off_input)
        advance_filter.summary_report_export_button(self)
        actual_text = prompt.text(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert period_from_input == actual_period_from
        assert period_to_input == actual_period_to
        assert cut_off_input == actual_cut_off
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_print_functionality(self):
        """Check response when clicking 'Print' button"""
        expected_text = "Undertime Approval"
        options_displayed = advance_filter.advance_filter_dropdown(self)
        actual_text = advance_filter.print_option(self)
        sleep(7)

        assert options_displayed == True
        assert expected_text == actual_text

        self.driver.close()

class TestEffectivityDate(Setup):
    # Check "Filter by effectivity date" functionality
    @pytest.mark.skip(reason="passed")
    def test_filter_by_effectivity_date_functionality(self):
        """Check response when clicking "Filter by Effectivity date" checkbox"""

        is_selected = filter_effectivity.checkbox(self)
        sleep(3)
        assert is_selected == False

        self.driver.close()

class TestApply(Setup):
    # Check "Apply" functionality
    @pytest.mark.skip(reason="passed")
    def test_auto_approval_review_specific_employee(self):
        """Check response when applying auto approval to the specific employee"""

        expected_text = "Request successfully reviewed."

        record_checkbox = self.driver.find_element(By.XPATH, '//*[@id="auto_approval_4"]')
        record_checkbox.click()
        record_selected = record_checkbox.is_selected()
        sleep(3)
        confirmation = apply.apply_button(self)
        apply.confirm_button(self)
        actual_text = prompt.text(self)
        sleep(3)

        assert record_selected == True
        assert confirmation == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="not needed")
    def test_auto_approval_review_multiple_employees(self):
        """Check response when applying auto approval to the multiple employee"""

        expected_text = "Request successfully reviewed."

        record_checkbox = self.driver.find_element(By.XPATH, '//*[@id="auto_approval"]')
        record_checkbox.click()
        record_selected = record_checkbox.is_selected()
        sleep(3)
        confirmation = apply.apply_button(self)
        apply.confirm_button(self)
        actual_text = prompt.text(self)
        sleep(3)

        assert record_selected == True
        assert confirmation == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_auto_approval_review_no_record_selected(self):
        """Check response when applying auto approval when no record is selected"""

        expected_text = "No selected request to auto review."

        confirmation = apply.apply_button(self)
        apply.confirm_button(self)
        actual_text = prompt.text(self)
        sleep(3)

        assert confirmation == True
        assert expected_text == actual_text

        self.driver.close()

class TestAutoApproval(Setup):
    # Check Auto approval - Review Functionality
    @pytest.mark.skip(reason="passed")
    def test_auto_approval_review_dropdown_functionality(self):
        """Check response when clicking "Review" dropdown"""

        expected_text = "Review"
        option_displayed = auto_approval_review.dropdown(self)
        actual_text = auto_approval_review.review_option(self)

        assert option_displayed == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_auto_approval_review_button_option(self):
        """Check response when clicking "Review" button"""

        option_displayed = auto_approval_review.dropdown(self)
        sleep(5)
        click_review_button = auto_approval_review.review_button(self)
        sleep(5)
        assert option_displayed == True
        assert click_review_button == True
        self.driver.close()

class TestRecordsPerPage(Setup):
    # Check Records per page Functionality
    @pytest.mark.skip(reason="passed")
    def test_record_per_page_dropdown(self):
        """Check response when clicking "Record per page" dropdown."""

        options_displayed = record_per_page.per_page_dropdown(self)
        actual_text = record_per_page.per_page_option_5(self)
        is_option_clicked = actual_text[0]

        assert options_displayed == True
        assert is_option_clicked == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_select_number_in_record_per_page_dropdown(self):
        """Check response when selecting a number in "Record per page" dropdown."""

        expected_text = "5"
        options_displayed = record_per_page.per_page_dropdown(self)
        actual_text = record_per_page.per_page_option_5(self)
        is_option_clicked = actual_text[0]

        assert options_displayed == True
        assert is_option_clicked == True
        assert expected_text == actual_text[1]

        self.driver.close()

class TestRecordsField(Setup):
    # Check Records Field
    @pytest.mark.skip(reason="passed")
    def test_response_when_clicking_record_checkbox(self):
        """Check response when clicking Record checkbox"""

        advance_filter_option = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/'
                                                                   'div/div/form/div[2]/tabletoolstrans/div/div/div/button[2]')
        advance_filter_option.click()
        sleep(3)
        deselect_all = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                          'form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/'
                                                          'div/span[1]/div[1]/button[2]')
        deselect_all.click()
        sleep(2)
        input_filter = "Pending"
        input_pending =  self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/'
                                                            'div/form/div[2]/tabletoolstrans/div/div/div/div/div[2]/'
                                                            'div/div/div/span[1]/div[1]/div/ul/li/input')
        input_pending.send_keys(input_filter)
        input_pending.send_keys(Keys.ENTER)
        sleep(2)
        apply_search = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                          'form/div[2]/tabletoolstrans/div/div/div/div/div[2]/div/div/'
                                                          'div/span[1]/div[11]/button[1]')
        apply_search.click()
        sleep(5)

        select_checkbox = record_field.checkbox(self)

        assert select_checkbox == True

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_when_clicking_record_row(self):
        """Check response when clicking a record row"""

        record_row_xpath = '//*[@id="table"]/tbody/tr[2]'
        dialog_displayed = record_field.record_row(self, record_row_xpath)
        dialog_closed = record_field.close_button(self)
        assert dialog_displayed == True
        assert dialog_closed == True

        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_response_when_clicking_overtime_approval_dialog_reviewed(self):
        """ Check response when clicking "Overtime Approval dialog" button """

        expected_text = "Request successfully reviewed"
        record_row_xpath = '//*[@id="table"]/tbody/tr[1]'
        edit_date = "05/27/2022"

        dialog_displayed = record_field.record_row(self, record_row_xpath)
        actual_date = record_field.edit_date(self, edit_date)
        record_field.submit_button(self)
        confirmation_displayed = record_field.confirm_button(self)
        actual_text = prompt.text(self)
        sleep(3)

        assert dialog_displayed == True
        assert edit_date == actual_date
        assert confirmation_displayed == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_when_clicking_overtime_approval_dialog_not_yet_reviewed(self):
        """ Check response when clicking "Overtime Approval dialog" button """

        expected_text = "Request successfully reviewed"
        record_row_xpath = '//*[@id="table"]/tbody/tr[3]'

        dialog_displayed = record_field.record_row(self, record_row_xpath)
        approve_selected = record_field.reviewed_record(self)
        record_field.submit_button(self)
        confirmation_displayed = record_field.confirm_button(self)
        actual_text = prompt.text(self)

        assert dialog_displayed == True
        assert approve_selected == True
        assert confirmation_displayed == True
        assert expected_text == actual_text

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_response_when_clicking_pages(self):
        """ Check response when clicking Previous/Next button """
        expected_text = "5"
        are_options_displayed = record_per_page.per_page_dropdown(self)
        actual_text = record_per_page.per_page_option_5(self)
        next_button_clicked = pagination.next_button(self)
        previous_button_clicked = pagination.previous_button(self)

        assert are_options_displayed == True
        assert expected_text == actual_text[1]
        assert next_button_clicked == True
        assert previous_button_clicked == True

        self.driver.close()

class TestRightClick(Setup):
    # Check Right Click Option
    @pytest.mark.skip(reason="passed")
    def test_view_logs_button(self):
        """ Check response when clicking 'View Logs' button """
        expected_text = "Dashboard"
        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]')
        options_displayed = right_click.action(self, select_record)
        actual_text = right_click.view_logs_option(self)

        assert options_displayed == True
        assert expected_text == actual_text
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_right_click_attach_option(self):
        """ Check response when clicking "Attach" button """

        select_record = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[4]")
        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)

        assert options_displayed == True
        assert dialog_displayed == True

        self.driver.close()

class TestAttachment(Setup):
    # Check Attachment Functionality
    @pytest.mark.skip(reason="passed")
    def test_attachment_click_drop_files(self):
        """ Check response when clicking "drop files here to upload" """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[2]')
        file_path = "E://fileattach.docx"
        expected_file_name = "fileattach.docx"

        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        file_attached = attachment.attach_file(self, file_path)
        uploaded_file = attachment.upload_button(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert file_attached[0] == True
        assert expected_file_name == uploaded_file

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_more_than_11_mb(self):
        """ Check response when uploading file more than 11MB """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]')
        file_path = "E://INTERNSHIP//quality handbook.pdf"

        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_attached = attachment.attach_file(self, file_path)
        error_dialog_displayed = is_file_attached[1]
        attachment.error_notif_ok_button(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert is_file_attached[0] == False
        assert error_dialog_displayed == True
        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_less_than_10_mb(self):
        """ Check response when uploading file less than 10MB """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[2]')
        file_path = "E://fileattach.docx"
        expected_file_name = "fileattach.docx"

        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        file_attached = attachment.attach_file(self, file_path)
        uploaded_file = attachment.upload_button(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert file_attached[0] == True
        assert expected_file_name == uploaded_file

        self.driver.close()

    @pytest.mark.skip(reason="passed")
    def test_attachment_upload_button(self):
        """ Check response when clicking 'Upload' button """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[2]')
        file_path = "E://fileattach.docx"
        expected_file_name = "fileattach.docx"

        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        file_attached = attachment.attach_file(self, file_path)
        uploaded_file = attachment.upload_button(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert file_attached[0] == True
        assert expected_file_name == uploaded_file

        self.driver.close()

    @pytest.mark.skip(reason="Overtime attribute...")
    def test_attachment_download_all_button(self):
        """ Check response when clicking "Download all" button """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]')
        options_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        is_file_downloaded = attachment.download_all(self)

        assert options_displayed == True
        assert dialog_displayed == True
        assert is_file_downloaded == True
        self.driver.close()

    # @pytest.mark.skip(reason="passed")
    def test_attachment_close_button(self):
        """ Check response when clicking 'Close' button """

        select_record = self.driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]')
        option_displayed = right_click.action(self, select_record)
        dialog_displayed = right_click.attach_option(self)
        dialog_closed = attachment.close_button(self)

        assert option_displayed == True
        assert dialog_displayed == True
        assert dialog_closed == False

        self.driver.close()
