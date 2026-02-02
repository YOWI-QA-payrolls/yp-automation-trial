from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class RecordsPerPage():

    def by_selecting(self, selection_option):

        records = dict({'5': '0' ,'10': '1','15': '2'})
        corresponding_array = records.values[selection_option]

        pagination_inputbox = self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-select-match')]")
        pagination_inputbox.click()

        record_page_option = self.driver.find_elements(By.XPATH, "//*[@id='ui-select-choices-row-{}-']/a/div)".format(corresponding_array))
        record_page_option.click()

    def by_inputting(self, input_data):
        
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-select-match')]").click()
        # records_per_page_input = self.driver.find_element(By.XPATH, "//input[@type='{}'])[4]").format(input_data)
        records_per_page_input = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[7]/div/input[1]")
        records_per_page_input.send_keys(input_data)

        record_per_page_display_selection = records_per_page_input.get_attribute('value')

        return record_per_page_display_selection

    def per_page_dropdown(self):
        records_per_page_dropdown = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/div[7]/div/div/span/span[2]')
        records_per_page_dropdown.click()
        sleep(3)

        option_1 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[3]").is_displayed()
        option_2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[4]").is_displayed()
        option_3 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[5]").is_displayed()

        if option_1 and option_2 and option_3 is True : is_option_displayed = True

        return is_option_displayed


    def per_page_option_5(self):
        try:
            option_five = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div/div/form/div[7]/div/ul/li/div[3]/a")
            option_five.click()
            option_clicked = True
            sleep(3)
        except Exception:
            print(Exception)
            option_clicked = False

        records_per_page_dropdown = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/form/div[7]/div/div/span/span[2]")
        actual_text = records_per_page_dropdown.get_attribute('textContent')

        return [option_clicked, actual_text]