from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import os

class EmployeePerPage:

    def click_employee_per_page(self):
        ''' click employee per page drop-down '''
        
        employee_per_page = self.driver.find_element(By.XPATH, "//*[@class='ui-select-container select2 select2-container ng-not-empty ng-valid']")
        employee_per_page.click()
        sleep(2)

    def employee_per_page_options(self):
        ''' selects 1 employee per page '''

        option_1 = self.driver.find_element(By.XPATH,"//*[@id='ui-select-choices-row-1-']")
        option_1.click()
        sleep(2)

    def records_in_page(self):
        ''' Checks number of records displayed in the page '''

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        number_of_records = self.soup.find('table',{'id':'table'}).find('tbody').find_all('tr')

        return len(number_of_records)