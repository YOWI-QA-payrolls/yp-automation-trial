from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from math import ceil
from utils.get_data import get_table_record_page_count
from utils.pagination import TablePagination
from utils.table import TableRecord

class Search():
    def box_function(self,input_data):
        """Searchbox input field"""
        
        try:
            search_box = self.driver.find_element(By.XPATH, "//*[@placeholder = 'Search...']")
        except NoSuchElementException:
            raise ValueError("Search box was not found")

        search_box.send_keys(input_data)
        actual_text = search_box.get_attribute('value')

        if actual_text!= input_data:
            raise Exception("Input data is not the same with the actual")
        else:
            return actual_text
    
    def click_icon_button(self):
        """Search icon button beside searchbox"""

        try:
            sleep(3)
            search_button = self.driver.find_element(By.XPATH, "//*[@ng-if = '!main.no_search_button']") 
            search_button.click()
            is_search_icon_clicked = True

        except NoSuchElementException:
            is_search_icon_clicked = False
            raise ValueError("Search icon button was not found")

        return is_search_icon_clicked


    def click_enter_function(self, input_data):
        """Send ENTER key to search"""

        search_box = self.driver.find_element(By.XPATH, "//*[@ng-if='!main.no_search']")
        search_box.send_keys(input_data)
        search_box.send_keys(Keys.ENTER)
        sleep(3)

        actual_text = search_box.get_attribute('value')
        return actual_text

        
    def check_search_results(self, input_data, table_name, column_number):
        """This check all the record row within a page if it's search input is within the record"""
        result = []
        for num in range(1,11):
            try:
                xpath = "//*[@id='"+ str(table_name) +"']/tbody/tr[" + str(num) + "]/td[" + str(column_number) + "]"
                record = self.driver.find_element(By.XPATH, xpath)
                name = record.text
                if name == "" : break
                elif input_data or input_data.lower() or input_data.capitalize() in name:
                    result.append(True)
                else: result.append(False)
            except Exception as error:
                print(error.__class__)
                break

        if not result : successful_search = True
        else:
            for data in result:
                if data is True : successful_search = True
                else: 
                    successful_search = False
                    break

        return successful_search


    def records_per_page(self,input_data, table_name, column_number):
        """This check all the record row within a page if it's search input is within the record"""
        result = []
        for row in range(1,11):
            try:
                xpath = "//*[@id='"+ str(table_name) +"']/tbody/tr[" + str(row) + "]/td["+ str(column_number) +"]" or  "//*[@id='"+ str(table_name) +"']/tbody/tr[" + str(row) + "]/td[7]"
                data_record = self.driver.find_element(By.XPATH, xpath)
                extracted_data = data_record.text
                if extracted_data == "" : break
                elif input_data or input_data.lower() or input_data.capitalize() or input_data.upper() in extracted_data:
                    result.append(True)
                else: 
                    result.append(False)
            except Exception as error:
                print(error.__class__)
                break

        return result


    def check_all_search_results(self, input_data,capsys, table_name, column_number):
        """This check the table record in all the pages for the search input data to assert with the records"""
        
        sleep(5)
        page_count = TableRecord.get_page_count(self)
        with capsys.disabled():
            print(page_count)
            
        result = Search.records_per_page(self, input_data, table_name, column_number)
        for page in range(1, page_count):
            TablePagination.next_button(self)
            result.extend(Search.records_per_page(self, input_data, table_name, column_number))

        with capsys.disabled():
            print(result)

        if not result : successful_search = True
        else:
            for data in result:
                if data is True: successful_search = True
                else: 
                    successful_search = False
                    break

        return successful_search
