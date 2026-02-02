from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def select_all(self):
    """Selecting all in the table"""
    select_all_checkbox = self.driver.find_element(By.ID, 'auto_approval')
    select_all_checkbox.click()
    sleep(3)
    is_checkbox_selected = select_all_checkbox.is_selected()

    return is_checkbox_selected

def check_search_record_displays(self,input_data, column_record):
    """Check result of search exists in the table"""

    record_per_page = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[6]/div/div/span/span[2]")
    record_count = record_per_page.text
    record_count = int(record_count)

    for record_row_number in range(11,10+record_count):
        try:
            table_record_row = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[{}]/td[{}]".format(record_row_number, column_record))
            column_name = table_record_row.text
            assert input_data == column_name
            print(column_name)

        except NoSuchElementException:
            raise ValueError(column_name ,"not found")

 
def check_search_record_status(self,input_data, column_record):
    """Check result of search exists in the table"""

    record_per_page = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div[1]/form/div[6]/div/div/span/span[2]")
    record_count = record_per_page.text
    record_count = int(record_count)

    for record_row_number in range(11,10+record_count):
        try:
            table_record_row = self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[{}]/td[{}]/span[2]/b/span".format(record_row_number, column_record))
            column_name = table_record_row.text
            assert "Reviewed" in column_name

        except NoSuchElementException:
            raise ValueError(column_name ,"not found")

    assert input_data == column_name


def advance_filter_status_option_reviewed(self):
    reviewed_by = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr[4]/td[10]/span[2]/b/span")
    reviewed_by.text

def advance_filter_status_option_recommended(self):
    recommended_by = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr[4]/td[11]/span[2]/b")
    recommended_by.text

def advance_filter_status_option_approved(self):
    approved_by = self.driver.find_element(By.XPATH,"//*[@id='table']/tbody/tr[12]/td[12]/span[2]/b")
    approved_by.text

    