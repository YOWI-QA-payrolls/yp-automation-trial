from math import ceil
from selenium.webdriver.common.by import By

class TableRecord():

    def get_page_count(self):
        """This get the overall page count in the table"""

        total_records = self.driver.find_element(By.XPATH, "//*[@ng-hide=\"main.current_module == 'dashboard'\"]")
        table_records = total_records.text
        cut_text_get_value = table_records.split(" : ")
        total_records = int(cut_text_get_value[1]) / 10
        page_count = ceil(total_records)

        return page_count