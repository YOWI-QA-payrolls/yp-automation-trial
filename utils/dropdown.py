from tkinter import dialog
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class Dropdown():

    def click_employee_dropdown(self):
        employee_selection = self.driver.find_element(By.XPATH,"//*[@ng-model = 'leave.employee']")
        sleep(3)
        employee_selection.click()

    def click_type_of_leave_dropdown(self):
        leave_type_dropdown = self.driver.find_element(By.XPATH,"//*[@placeholder='Type of Leave']")
        leave_type_dropdown.click()
        sleep(3)

    def select_dropdown_option(self, input_data):
        select_option = self.driver.find_element(By.XPATH,"//div[text()='{}']".format(input_data))
        self.driver.execute_script("arguments[0].click();",select_option)
        sleep(3)

    def icon_button(self):
        dropdown_icon_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/button[3]")
        dropdown_icon_button.click()
        sleep(3)

        option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
        option_2 = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export').is_displayed()
        option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

        if option_1 and option_2 and option_3 is True : is_option_displayed = True
        return is_option_displayed

    def export_option(self):
        export_option = self.driver.find_element(By.LINK_TEXT, 'Export')
        export_option.click()
        sleep(3)

        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/heyysson/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1

        return is_downloaded

    def summary_report_export_option(self):
        summary_report_export_option = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export')
        summary_report_export_option.click()
        sleep(5)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        dialog_displayed = summary_report_export_dialog.is_displayed()

        return dialog_displayed

    def summary_report_export_close_button(self):
        close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
        close_button.click()
        sleep(3)

        summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_dialog_closed = not summary_report_export_dialog.is_displayed()

        return is_dialog_closed

    def summary_report_export_button(self):
        export_button = self.driver.find_element(By.XPATH, "//*[@ng-click='export_summary_report()']")
        export_button.click()
        sleep(5)

    def check_if_file_downloaded():
        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/heyysson/Downloads")

            for fname in files:
                if fname.endswith('.xlsx'):
                    is_downloaded = True

            seconds += 1
        sleep(3)

        return is_downloaded

    def summary_report_export_period_from_calendar(self):
        self.driver.implicitly_wait(10)
        period_from_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_from\')\"]")
        period_from_calendar_icon.click()
        sleep(1)

        calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed

    def summary_report_export_period_to_calendar(self):
        self.driver.implicitly_wait(10)
        period_to_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_to\')\"]")
        period_to_calendar_icon.click()
        sleep(1)

        calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[3]/p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed

    def summary_report_export_cut_off_calendar(self):
        self.driver.implicitly_wait(10)
        cut_off_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'cut_off\')\"]")
        cut_off_calendar_icon.click()
        sleep(1)

        calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[4]/p[1]/div/ul/li[1]/div")
        is_calendar_displayed = calendar.is_displayed()

        return is_calendar_displayed

    def summary_report_export_calendar_input_period_from(self, period_from_input):
        self.driver.implicitly_wait(10)
        period_from_input = self.driver.find_element(By.XPATH, period_from_input)
        period_from_input.click()
        sleep(1)
        
        period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
        actual_text = period_from_input_box.get_attribute('value')

        return actual_text

    def summary_report_export_calendar_input_period_to(self, period_to_input):
        self.driver.implicitly_wait(10)
        period_to_input = self.driver.find_element(By.XPATH, period_to_input)
        period_to_input.click()
        sleep(1)

        period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
        actual_text = period_to_input_box.get_attribute('value')

        return actual_text

    def summary_report_export_calendar_input_cut_off(self, cut_off_input):
        self.driver.implicitly_wait(10)
        cut_off_input = self.driver.find_element(By.XPATH, cut_off_input)
        cut_off_input.click()
        sleep(1)
        
        cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
        actual_text = cut_off_input_box.get_attribute('value')

        return actual_text

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
        print_option = self.driver.find_element(By.LINK_TEXT, "Print")
        print_option.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        window_title = self.driver.title

        return window_title


def click_employee_dropdown(self):
    employee_selection = self.driver.find_element(By.XPATH,"//*[@ng-model = 'leave.employee']")
    sleep(3)
    employee_selection.click()

def click_type_of_leave_dropdown(self):
    leave_type_dropdown = self.driver.find_element(By.XPATH,"//*[@placeholder='Type of Leave']")
    leave_type_dropdown.click()
    sleep(3)

def select_dropdown_option(self, input_data):
    select_option = self.driver.find_element(By.XPATH,"//div[text()='{}']".format(input_data))
    self.driver.execute_script("arguments[0].click();",select_option)
    sleep(3)


def icon_button(self):
    dropdown_icon_button = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[2]/tabletoolstrans/div/div/div/button[3]")
    dropdown_icon_button.click()
    sleep(3)

    option_1 = self.driver.find_element(By.LINK_TEXT, 'Export').is_displayed()
    option_2 = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export').is_displayed()
    option_3 = self.driver.find_element(By.LINK_TEXT, 'Print').is_displayed()

    if option_1 and option_2 and option_3 is True : is_option_displayed = True
    return is_option_displayed

def export_option(self):
    export_option = self.driver.find_element(By.LINK_TEXT, 'Export')
    export_option.click()
    sleep(3)

    timeout = 5
    seconds = 0
    is_downloaded = True
    while is_downloaded and seconds < timeout:
        sleep(1)
        is_downloaded = False
        files = os.listdir("C://Users/heyysson/Downloads")

        for fname in files:
            if fname.endswith('.xlsx'):
                is_downloaded = True

        seconds += 1

    return is_downloaded

def summary_report_export_option(self):
    summary_report_export_option = self.driver.find_element(By.LINK_TEXT, 'Summary Report Export')
    summary_report_export_option.click()
    sleep(5)

    summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    dialog_displayed = summary_report_export_dialog.is_displayed()

    return dialog_displayed

def summary_report_export_close_button(self):
    close_button = self.driver.find_element(By.XPATH, "//*[@ng-click='main.close_dialog()']")
    close_button.click()
    sleep(3)

    summary_report_export_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    is_dialog_closed = not summary_report_export_dialog.is_displayed()

    return is_dialog_closed

def summary_report_export_button(self):
    export_button = self.driver.find_element(By.XPATH, "//*[@ng-click='export_summary_report()']")
    export_button.click()
    sleep(5)

def check_if_file_downloaded():
    timeout = 5
    seconds = 0
    is_downloaded = True
    while is_downloaded and seconds < timeout:
        sleep(1)
        is_downloaded = False
        files = os.listdir("C://Users/heyysson/Downloads")

        for fname in files:
            if fname.endswith('.xlsx'):
                is_downloaded = True

        seconds += 1
    sleep(3)

    return is_downloaded

def summary_report_export_period_from_calendar(self):
    self.driver.implicitly_wait(10)
    period_from_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_from\')\"]")
    period_from_calendar_icon.click()
    sleep(1)

    calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/p[1]/div/ul/li[1]/div")
    is_calendar_displayed = calendar.is_displayed()

    return is_calendar_displayed

def summary_report_export_period_to_calendar(self):
    self.driver.implicitly_wait(10)
    period_to_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'period_to\')\"]")
    period_to_calendar_icon.click()
    sleep(1)

    calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[3]/p[1]/div/ul/li[1]/div")
    is_calendar_displayed = calendar.is_displayed()

    return is_calendar_displayed

def summary_report_export_cut_off_calendar(self):
    self.driver.implicitly_wait(10)
    cut_off_calendar_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date(\'cut_off\')\"]")
    cut_off_calendar_icon.click()
    sleep(1)

    calendar = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[4]/p[1]/div/ul/li[1]/div")
    is_calendar_displayed = calendar.is_displayed()

    return is_calendar_displayed

def summary_report_export_calendar_input_period_from(self, period_from_input):
    self.driver.implicitly_wait(10)
    period_from_input = self.driver.find_element(By.XPATH, period_from_input)
    period_from_input.click()
    sleep(1)
    
    period_from_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_from']")
    actual_text = period_from_input_box.get_attribute('value')

    return actual_text

def summary_report_export_calendar_input_period_to(self, period_to_input):
    self.driver.implicitly_wait(10)
    period_to_input = self.driver.find_element(By.XPATH, period_to_input)
    period_to_input.click()
    sleep(1)

    period_to_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.period_to']")
    actual_text = period_to_input_box.get_attribute('value')

    return actual_text

def summary_report_export_calendar_input_cut_off(self, cut_off_input):
    self.driver.implicitly_wait(10)
    cut_off_input = self.driver.find_element(By.XPATH, cut_off_input)
    cut_off_input.click()
    sleep(1)
    
    cut_off_input_box = self.driver.find_element(By.XPATH, "//*[@ng-model='summary_export.cut_off']")
    actual_text = cut_off_input_box.get_attribute('value')

    return actual_text

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
    print_option = self.driver.find_element(By.LINK_TEXT, "Print")
    print_option.click()

    self.driver.switch_to.window(self.driver.window_handles[1])
    window_title = self.driver.title

    return window_title