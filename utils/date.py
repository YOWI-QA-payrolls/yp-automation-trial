from time import sleep
from datetime import date, datetime
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from utils.setup import driversetup
from selenium.webdriver.common.action_chains import ActionChains

class reviewer_date():

    def date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()


    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            click_search_calendar.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_search_icon_clicked


    def date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def date_total_record(self):
        """For assert, to show number of records being displayed after test"""
        total_record_result = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/span')
        actual_text = total_record_result.text
        return actual_text


    def leave_date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def leave_input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def leave_date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[1]/tabletoolsdaterange2/p/input[1]')
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def leave_date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def leave_input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def leave_date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def leave_date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def leave_date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[1]/tabletoolsdaterange2/p/input[2]')
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def leave_search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[4]')
            click_search_calendar.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

class recommender_date():

    def date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False
        return is_calendar_icon_clicked


    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()
        

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            click_search_calendar.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_search_icon_clicked


    def date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def date_total_record(self):
        """For assert, to show number of records being displayed after test"""
        total_record_result = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/span')
        actual_text = total_record_result.text
        return actual_text


    def leave_date_from(self):
        """Test date from functionality"""

        date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
        date_from_icon.click()


    def leave_date_to(self):
        """Test date functionality"""

        date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
        date_to_icon.click()


    def leave_search_icon(self):
        """Test calendar search icon functionality"""
        click_search_calendar = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[4]')
        click_search_calendar.click()


    def leave_date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def leave_date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


class approver_date():
    def check_system_date(self):
        """ System Date """

        system_date = datetime.now()
        current_date = system_date.strftime("%m/%d/%Y")
        return current_date

    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_from_calendar_icon(self):
        """ To click Date from calendar icon """

        try:
            date_from = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        input_date_from.click()

    def date_to_calendar_icon(self):
        """ To click Date to calendar icon """

        try:
            date_to = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        input_date_to.click()

    def date_field_search_icon(self):
        """ To click Search icon """

        try:
            search_icon = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            search_icon.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_search_icon_clicked = False
        sleep(3)

        return is_search_icon_clicked

    def date_to_field_input_box(self, date_to_input):
        """ To manually input specific date into date_to field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)
        sleep(3)

        actual_text = date_to_box.get_attribute('value')
        return actual_text

    def date_from_field_input_box(self, date_from_input):
        """ To manually input specific date into date_from field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)
        sleep(3)
        
        actual_text = date_from_box.get_attribute('value')
        return actual_text

    def check_format_date(date_input):
        format = "%m/%d/%Y"

        try:
            datetime.strptime(date_input, format)
            is_input_date_correct_format = True
        except ValueError:
            is_input_date_correct_format = False
        sleep(3)
        
        return is_input_date_correct_format

class Date():

    def check_system_date(self):
        """ System Date """

        system_date = datetime.now()
        current_date = system_date.strftime("%m/%d/%Y")
    
        return current_date

    def date_from_today(self):
        
        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    # def date_to_today(self):
    def to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_from_calendar_icon(self):
        """ To click Date from calendar icon """

        try:
            date_from = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        input_date_from.click()

    def date_to_calendar_icon(self):
        """ To click Date to calendar icon """

        try:
            date_to = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        input_date_to.click()

    def date_field_search_icon(self):
        """ To click Search icon """

        try:
            search_icon = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            search_icon.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_search_icon_clicked = False
        sleep(3)

        return is_search_icon_clicked

    def date_to_field_input_box(self, date_to_input):
        """ To manually input specific date into date_to field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)
        sleep(3)

        actual_text = date_to_box.get_attribute('value')
        return actual_text

    def date_from_field_input_box(self, date_from_input):
        """ To manually input specific date into date_from field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)
        sleep(3)
        
        actual_text = date_from_box.get_attribute('value')
        return actual_text

    def check_format_date(date_input):
        format = "%m/%d/%Y"

        try:
            datetime.strptime(date_input, format)
            is_input_date_correct_format = True
        except ValueError:
            is_input_date_correct_format = False
        sleep(3)
        
        return is_input_date_correct_format


    def from_input(self, input_data):
        """Date From Input Feature"""
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-model= 'filters.date_from']")
        date_from_inputbox.click()
        date_from_inputbox .send_keys(input_data)

    def to_input(self, input_data):
        """Date To Input Feature """
        date_from_inputbox = self.driver.find_element(By.XPATH,"//*[@ng-model = 'filters.date_to']")
        date_from_inputbox.click()
        date_from_inputbox .send_keys(input_data)


    def from_calendar(self):
        """Dropdown Date selection"""
        #not yet finish
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-click = main.open_date('date_from2')]")
        date_from_inputbox.click()

    def to_calendar(self):
        #not yet finish
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-click = 'main.open_date' and contains(., 'filter_date_to')")
        date_from_inputbox.click()

    #Date selection/input search button
    def selection_search_button(self):
        search_button = self.driver.find_element(By.XPATH, "//*[@ng-if = '!main.has_button']")
        search_button.click()

    #Pop Up
    def request_popup_date_from(self,input_data,request_type):    
        date_from = self.driver.find_element(By.XPATH, "//*[@datepicker-options = '{}.option_from']".format(request_type))
        date_from.clear()
        date_from.send_keys(input_data)
        date_from.send_keys(Keys.ENTER)

    def request_popup_date_to(self,input_data,request_type):    
        date_to = self.driver.find_element(By.XPATH, "//*[@datepicker-options = '{}.option_to']".format(request_type))
        date_to.clear()
        date_to.send_keys(input_data)
        date_to.send_keys(Keys.ENTER)

    def request_popup_date_from_using_model(self,input_data,request_type):    
        date_from = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_from']".format(request_type))
        date_from.clear()
        date_from.send_keys(input_data)
        date_from.send_keys(Keys.ENTER)

    def request_popup_date_to_using_model(self,input_data,request_type):    
        date_to = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_to']".format(request_type))
        date_to.clear()
        date_to.send_keys(input_data)
        date_to.send_keys(Keys.ENTER)

class reviewer_date():

    def date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()


    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            click_search_calendar.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_search_icon_clicked


    def date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def date_total_record(self):
        """For assert, to show number of records being displayed after test"""
        total_record_result = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/span')
        actual_text = total_record_result.text
        return actual_text


    def leave_date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def leave_input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def leave_date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[1]/tabletoolsdaterange2/p/input[1]')
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def leave_date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def leave_input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def leave_date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def leave_date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def leave_date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/'
                                                        'form/div[1]/tabletoolsdaterange2/p/input[2]')
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def leave_search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[4]')
            click_search_calendar.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

class recommender_date():

    def date_from(self):
        """Test date from functionality"""

        try:
            date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
            date_from_icon.click()
            sleep(3)
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False
        return is_calendar_icon_clicked


    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()
        

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        select_input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        select_input_date_from.click()
        sleep(3)


    def date_to(self):
        """Test date to functionality"""

        try:
            date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
            date_to_icon.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked


    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        select_input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        select_input_date_to.click()


    def search_icon(self):
        """Test calendar search icon functionality"""

        try:
            click_search_calendar = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            click_search_calendar.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_search_icon_clicked


    def date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


    def date_from_input_box(self, date_from_input):
        """ Input specific date into Date From field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)

        actual_text = date_from_box.get_attribute('value')
        return actual_text


    def date_to_input_box(self, date_to_input):
        """ Input specific date into Date To field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)

        actual_text = date_to_box.get_attribute('value')
        return actual_text


    def date_total_record(self):
        """For assert, to show number of records being displayed after test"""
        total_record_result = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/span')
        actual_text = total_record_result.text
        return actual_text


    def leave_date_from(self):
        """Test date from functionality"""

        date_from_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[1]/button')
        date_from_icon.click()


    def leave_date_to(self):
        """Test date functionality"""

        date_to_icon = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[3]/button')
        date_to_icon.click()


    def leave_search_icon(self):
        """Test calendar search icon functionality"""
        click_search_calendar = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[1]/form/div[1]/tabletoolsdaterange2/p/span[4]')
        click_search_calendar.click()


    def leave_date_from_field(self, date_from_input):
        """Test date from input"""
        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)


    def leave_date_to_field(self, date_to_input):
        """Test date to input"""
        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)


class approver_date():
    def check_system_date(self):
        """ System Date """

        system_date = datetime.now()
        current_date = system_date.strftime("%m/%d/%Y")
        return current_date

    def date_from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_from_calendar_icon(self):
        """ To click Date from calendar icon """

        try:
            date_from = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        input_date_from.click()

    def date_to_calendar_icon(self):
        """ To click Date to calendar icon """

        try:
            date_to = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        input_date_to.click()

    def date_field_search_icon(self):
        """ To click Search icon """

        try:
            search_icon = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            search_icon.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_search_icon_clicked = False
        sleep(3)

        return is_search_icon_clicked

    def date_to_field_input_box(self, date_to_input):
        """ To manually input specific date into date_to field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)
        sleep(3)

        actual_text = date_to_box.get_attribute('value')
        return actual_text

    def date_from_field_input_box(self, date_from_input):
        """ To manually input specific date into date_from field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)
        sleep(3)
        
        actual_text = date_from_box.get_attribute('value')
        return actual_text

    def check_format_date(date_input):
        format = "%m/%d/%Y"

        try:
            datetime.strptime(date_input, format)
            is_input_date_correct_format = True
        except ValueError:
            is_input_date_correct_format = False
        sleep(3)
        
        return is_input_date_correct_format

class Date():

    def check_system_date(self):
        """ System Date """

        system_date = datetime.now()
        current_date = system_date.strftime("%m/%d/%Y")
    
        return current_date

    def date_from_today(self):
        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def from_today(self):
        """ To click the today button in date_from calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    # def date_to_today(self):
    def to_today(self):
        """ To click the today button in date_to calendar """

        today_button = self.driver.find_element(By.XPATH, "//*[@ng-click=\"select('today', $event)\"]")
        today_button.click()

    def date_from_calendar_icon(self):
        """ To click Date from calendar icon """

        try:
            date_from = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_from')\"]")
            date_from.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_from(self, input_date_from_xpath):
        """ Select specific date_from from the calendar """

        input_date_from = self.driver.find_element(By.XPATH, input_date_from_xpath)
        input_date_from.click()

    def date_to_calendar_icon(self):
        """ To click Date to calendar icon """

        try:
            date_to = self.driver.find_element(By.XPATH, "//*[@ng-click=\"main.open_date('filter_date_to')\"]")
            date_to.click()
            is_calendar_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_calendar_icon_clicked = False

        return is_calendar_icon_clicked

    def input_date_to(self, input_date_to_xpath):
        """ Select specific date_to from the calendar """

        input_date_to = self.driver.find_element(By.XPATH, input_date_to_xpath)
        input_date_to.click()

    def date_field_search_icon(self):
        """ To click Search icon """

        try:
            search_icon = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.has_button']")
            search_icon.click()
            is_search_icon_clicked = True
        except Exception as error:
            print(error.__class__)
            is_search_icon_clicked = False
        sleep(3)

        return is_search_icon_clicked

    def date_to_field_input_box(self, date_to_input):
        """ To manually input specific date into date_to field """

        date_to_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_to']")
        date_to_box.send_keys(date_to_input)
        sleep(3)

        actual_text = date_to_box.get_attribute('value')
        return actual_text

    def date_from_field_input_box(self, date_from_input):
        """ To manually input specific date into date_from field """

        date_from_box = self.driver.find_element(By.XPATH, "//*[@ng-model='filters.date_from']")
        date_from_box.send_keys(date_from_input)
        sleep(3)
        
        actual_text = date_from_box.get_attribute('value')
        return actual_text

    def check_format_date(date_input):
        format = "%m/%d/%Y"

        try:
            datetime.strptime(date_input, format)
            is_input_date_correct_format = True
        except ValueError:
            is_input_date_correct_format = False
        sleep(3)
        
        return is_input_date_correct_format


    def from_input(self, input_data):
        """Date From Input Feature"""
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-model= 'filters.date_from']")
        date_from_inputbox.click()
        date_from_inputbox .send_keys(input_data)

    def to_input(self, input_data):
        """Date To Input Feature """
        date_from_inputbox = self.driver.find_element(By.XPATH,"//*[@ng-model = 'filters.date_to']")
        date_from_inputbox.click()
        date_from_inputbox .send_keys(input_data)


    def from_calendar(self):
        """Dropdown Date selection"""
        #not yet finish
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-click = main.open_date('date_from2')]")
        date_from_inputbox.click()

    def to_calendar(self):
        #not yet finish
        date_from_inputbox = self.driver.find_element(By.XPATH, "//*[@ng-click = 'main.open_date' and contains(., 'filter_date_to')")
        date_from_inputbox.click()

    #Date selection/input search button
    def selection_search_button(self):
        search_button = self.driver.find_element(By.XPATH, "//*[@ng-if = '!main.has_button']")
        search_button.click()

    #Pop Up
    def request_popup_date_from(self,input_data,request_type):    
        date_from = self.driver.find_element(By.XPATH, "//*[@datepicker-options = '{}.option_from']".format(request_type))
        date_from.clear()
        date_from.send_keys(input_data)
        date_from.send_keys(Keys.ENTER)
        date_from.send_keys(Keys.TAB)

    def request_popup_date_to(self,input_data,request_type):    
        date_to = self.driver.find_element(By.XPATH, "//*[@datepicker-options = '{}.option_to']".format(request_type))
        date_to.clear()
        date_to.send_keys(input_data)
        date_to.send_keys(Keys.ENTER)
        date_to.send_keys(Keys.TAB)

    def request_popup_date_from_using_model(self,input_data,request_type):    
        date_from = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_from']".format(request_type))
        date_from.clear()
        date_from.send_keys(input_data)
        date_from.send_keys(Keys.ENTER)

    def request_popup_date_to_using_model(self,input_data,request_type):    
        date_to = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_to']".format(request_type))
        date_to.clear()
        date_to.send_keys(input_data)
        date_to.send_keys(Keys.ENTER)
        
    #Pop Up using ng-model
    def create_request_popup_date_using_ngmodel(self,input_data,request_type):  
        """Using ng model attribute date"""
        date = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date']".format(request_type))
        date.send_keys(Keys.CONTROL + "a")
        date.send_keys(Keys.DELETE)
        date.send_keys(input_data)

    def create_request_popup_date_from_using_ngmodel(self,input_data,request_type):  
        """Using ng model attribute date from"""
        date_from = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_from']".format(request_type))
        date_from.send_keys(Keys.CONTROL + "a")
        date_from.send_keys(Keys.DELETE)
        date_from.send_keys(input_data)
        

    def create_request_popup_date_to_using_ngmodel(self,input_data,request_type):    
        """Using ng model attribute date to"""
        date_from = self.driver.find_element(By.XPATH, "//*[@ng-model = '{}.date_to']".format(request_type))
        date_from.send_keys(Keys.CONTROL + "a")
        date_from.send_keys(Keys.DELETE)
        date_from.send_keys(input_data)


# def date_create_request_popup_time_from_using_ngmodel(self,input_data,request_type):  
#     time_from = self.driver.find_element(By.XPATH, "//*[@ng-model = 'leave.{}']".format(request_type))
#     time_from.send_keys(Keys.CONTROL + "a")
#     time_from.send_keys(Keys.DELETE)
#     time_from.send_keys(input_data)


# def date_create_request_popup_time_to_using_ngmodel(self,input_data,request_type):  
#     time_to = self.driver.find_element(By.XPATH, "//*[@ng-model = 'leave.{}']".format(request_type))
#     time_to.send_keys(Keys.CONTROL + "a")
#     time_to.send_keys(Keys.DELETE)
#     time_to.send_keys(input_data)

