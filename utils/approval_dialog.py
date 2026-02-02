from math import ceil

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from utils import pagination

class reviewer_approval_dialog():
        
    def multiple_approval_dialog(self):
        multiple_approval_dialog_button = self.driver.find_element(By.XPATH, "//*[@ng-click='open_multiple_approval_dialog()']")
        multiple_approval_dialog_button.click()
        sleep(3)


    def checkbox(self):
        record_checkbox = self.driver.find_element(By.XPATH, '//*[@id="auto_approval_0"]')
        record_checkbox.click()
        sleep(5)
        is_selected = record_checkbox.is_selected()
        return is_selected


    def search_field(self, input_data):
        """Test search functionality"""

        search_box = self.driver.find_element(By.XPATH, "//*[@ng-model='main.filters.name']")
        search_box.send_keys(input_data)
        sleep(3)

        actual_input = search_box.get_attribute('value')
        return actual_input


    def enter_key(self, input_data):
        """Test ENTER key to search"""

        try:
            search_box = self.driver.find_element(By.XPATH, '//*[@ng-if = "!main.no_search"]')
            search_box.send_keys(input_data)
            search_box.send_keys(Keys.ENTER)
            sleep(5)
            is_search_enter_key_pressed = True
        except Exception as error:
            print(error.__class__)
            is_search_enter_key_pressed = False

        return is_search_enter_key_pressed


    def search_result(self, input_data):
        result = []
        for num in range(1, 10):
            try:
                xpath = "//*[@id='table']/tbody/tr[" + str(num) + "]/td[3]"
                record = self.driver.find_element(By.XPATH, xpath)
                name = record.text
                if name == "":
                    break
                elif input_data or input_data.lower() or input_data.capitalize() in name:
                    result.append(True)
                else:
                    result.append(False)
            except Exception as error:
                print(error.__class__)
                break

        if not result: successful_search = True

        for data in result:
            if data is True:
                successful_search = True
            else:
                successful_search = False
                break

        return successful_search


    def check_all_result(self, input_data): 
        panel_footer = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div[1]/label")
        text = panel_footer.text
        cut_text = text[len(text) - 2:]
        total_records = int(cut_text) / 10
        end_page = ceil(total_records)

        result = search_records_per_page(self, input_data)
        for page in range(1, end_page):
            pagination.next_button(self)
            result.extend(search_records_per_page(self, input_data))

        if not result: successful_search = True
        else:
            for data in result:
                if data is True: successful_search = True
                else:
                    successful_search = False
                    break

        return successful_search


    def search_records_per_page(self, input_data):
        result = []
        for row in range(1, 11):
            try:
                xpath = "//*[@id='table']/tbody/tr[" + str(row) + "]/td[4]"
                record = self.driver.find_element(By.XPATH, xpath)
                name = record.text
                if name == "":
                    break
                elif input_data or input_data.lower() or input_data.capitalize() in name:
                    result.append(True)
                else:
                    result.append(False)
            except Exception as error:
                print(error.__class__)
                break

        return result

class recommender_approval_dialog():

    def multiple_approval_dialog(self):
        multiple_approval_dialog_button = self.driver.find_element(By.XPATH, "//*[@ng-click='open_multiple_approval_dialog()']")
        multiple_approval_dialog_button.click()
        sleep(3)


    def checkbox(self):
        record_checkbox = self.driver.find_element(By.XPATH, '//*[@id="auto_approval_0"]')
        record_checkbox.click()
        sleep(5)
        is_selected = record_checkbox.is_selected()
        return is_selected