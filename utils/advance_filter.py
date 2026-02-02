import os

from selenium.webdriver.common.by import By

import time

class reviewer_advance_filter_dropdown():

    def advance_filter_dropdown(self):
        """Test advance filter dropdown functionality"""

        dropdown_icon = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[2]/tabletoolstrans/div/div/div/button[3]')
        dropdown_icon.click()
        time.sleep(5)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_2 = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_2 and option_3 is True: options_displayed = True
        return options_displayed


    def export_option(self):
        """Test export option functionality"""

        click_export_option = self.driver.find_element(By.LINK_TEXT, 'Export')
        click_export_option.click()

        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            time.sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1

        return is_downloaded


    def summary_report_export_option(self):
        """Test summary report export functionality"""
        summary_report_export = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export')
        summary_report_export.click()
        time.sleep(5)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        dialog_displayed = summary_report_export_dialog.is_displayed()

        return dialog_displayed


    def summary_report_export_close_button(self):
        close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
        close_button.click()
        time.sleep(3)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_dialog_closed = not summary_report_export_dialog.is_displayed()

        return is_dialog_closed


    def summary_report_export_period_from_calendar(self):
        # self.driver.implicitly_wait(10)
        period_from_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_from\')\"]")
        period_from_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_period_to_calendar(self):
        # self.driver.implicitly_wait(10)
        period_to_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_to\')\"]")
        period_to_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[3]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_cut_off_calendar(self):
        # self.driver.implicitly_wait(10)
        cut_off_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'cut_off\')\"]")
        cut_off_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[4]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_calendar_input_period_from(self, period_from_input):
        # self.driver.implicitly_wait(10)
        period_from_input = self.driver.find_element(By.XPATH, period_from_input)
        period_from_input.click()
        time.sleep(3)

        period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
        actual_text = period_from_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_calendar_input_period_to(self, period_to_input):
        # self.driver.implicitly_wait(10)
        period_to_input = self.driver.find_element(By.XPATH, period_to_input)
        period_to_input.click()
        time.sleep(3)

        period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
        actual_text = period_to_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_calendar_input_cut_off(self, cut_off_input):
        # self.driver.implicitly_wait(10)
        cut_off_input = self.driver.find_element(By.XPATH, cut_off_input)
        cut_off_input.click()
        time.sleep(3)

        cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
        actual_text = cut_off_input_box.get_attribute('value')

        return actual_text


    def check_if_file_downloaded():
        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            time.sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1
        time.sleep(3)

        return is_downloaded


    def summary_report_export_button(self):
        export_button = self.driver.find_element(By.XPATH, "//*[@ng-click='export_summary_report()']")
        export_button.click()
        time.sleep(5)


    def summary_report_export_period_from_input_box(self, period_from_input):
        period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
        period_from_input_box.send_keys(period_from_input)

        actual_text = period_from_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_period_to_input_box(self, period_to_input):
        period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
        period_to_input_box.send_keys(period_to_input)

        actual_text = period_to_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_cut_off_input_box(self, cut_off_input):
        cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
        cut_off_input_box.send_keys(cut_off_input)

        actual_text = cut_off_input_box.get_attribute('value')

        return actual_text


    def print_option(self):
        dropdown_print_option = self.driver.find_element(By.LINK_TEXT, "Print")
        dropdown_print_option.click()
        # time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        window_title = self.driver.title

        return window_title


    def leave_advance_filter(self):
        """Test advance filter dropdown functionality"""

        dropdown_icon = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[2]/'
                                                        'tabletoolstrans/div/div/div/button[3]')
        dropdown_icon.click()
        time.sleep(5)

class recommender_advance_filter_dropdown():

    def advance_filter_dropdown(self):
        """Test advance filter dropdown functionality"""

        dropdown_icon = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[2]/tabletoolstrans/div/div/div/button[3]')
        dropdown_icon.click()
        time.sleep(5)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_2 = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_2 and option_3 is True: options_displayed = True
        return options_displayed


    def export_option(self):
        """Test export option functionality"""

        click_export_option = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/'
                                                                'div/form/div[2]/tabletoolstrans/div/div/div/ul/li[1]/a')
        click_export_option.click()

        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            time.sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1

        return is_downloaded


    def summary_report_export_option(self):
        """Test summary report export functionality"""
        summary_report_export = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/'
                                                                'div/div/form/div[2]/tabletoolstrans/div/div/div/'
                                                                'ul/li[3]/a[1]')
        summary_report_export.click()
        time.sleep(5)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        dialog_displayed = summary_report_export_dialog.is_displayed()

        return dialog_displayed


    def summary_report_export_close_button(self):
        close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
        close_button.click()
        time.sleep(3)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_dialog_closed = not summary_report_export_dialog.is_displayed()

        return is_dialog_closed


    def summary_report_export_period_from_calendar(self):
        # self.driver.implicitly_wait(10)
        period_from_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_from\')\"]")
        period_from_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_period_to_calendar(self):
        # self.driver.implicitly_wait(10)
        period_to_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_to\')\"]")
        period_to_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[3]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_cut_off_calendar(self):
        # self.driver.implicitly_wait(10)
        cut_off_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'cut_off\')\"]")
        cut_off_calendar_icon.click()
        time.sleep(3)

        calendar = self.driver.find_element(By.XPATH,
                                            "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[4]/"
                                            "p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed


    def summary_report_export_calendar_input_period_from(self, period_from_input):
        # self.driver.implicitly_wait(10)
        period_from_input = self.driver.find_element(By.XPATH, period_from_input)
        period_from_input.click()
        time.sleep(3)

        period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
        actual_text = period_from_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_calendar_input_period_to(self, period_to_input):
        # self.driver.implicitly_wait(10)
        period_to_input = self.driver.find_element(By.XPATH, period_to_input)
        period_to_input.click()
        time.sleep(3)

        period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
        actual_text = period_to_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_calendar_input_cut_off(self, cut_off_input):
        # self.driver.implicitly_wait(10)
        cut_off_input = self.driver.find_element(By.XPATH, cut_off_input)
        cut_off_input.click()
        time.sleep(3)

        cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
        actual_text = cut_off_input_box.get_attribute('value')

        return actual_text


    def check_if_file_downloaded():
        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            time.sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1
        time.sleep(3)

        return is_downloaded


    def summary_report_export_button(self):
        export_button = self.driver.find_element(By.XPATH, "//*[@ng-click='export_summary_report()']")
        export_button.click()
        time.sleep(5)


    def summary_report_export_period_from_input_box(self, period_from_input):
        period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
        period_from_input_box.send_keys(period_from_input)

        actual_text = period_from_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_period_to_input_box(self, period_to_input):
        period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
        period_to_input_box.send_keys(period_to_input)

        actual_text = period_to_input_box.get_attribute('value')

        return actual_text


    def summary_report_export_cut_off_input_box(self, cut_off_input):
        cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
        cut_off_input_box.send_keys(cut_off_input)

        actual_text = cut_off_input_box.get_attribute('value')

        return actual_text


    def print_option(self):
        dropdown_print_option = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/'
                                                                'div/form/div[2]/tabletoolstrans/div/div/div/ul/'
                                                                'li[3]/a[2]')
        dropdown_print_option.click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        window_title = self.driver.title

        return window_title


    def leave_advance_filter(self):
        """Test advance filter dropdown functionality"""

        dropdown_icon = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[2]/'
                                                        'tabletoolstrans/div/div/div/button[3]')
        dropdown_icon.click()
        time.sleep(5)
