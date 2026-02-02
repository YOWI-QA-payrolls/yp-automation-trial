from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class TablePagination():

    def next_button(self):
        try:
            next_button = self.driver.find_element(By.XPATH, "//*[@ng-click='selectPage(page + 1, $event)']")
            next_button.click()
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False

    def record_per_page(self):
        record_per_page_button = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/div[7]/div/div/span/span[2]')
        record_per_page_button.click()
        self.driver.implicitly_wait(10)
        select_number = self.driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-1-"]/a/div')
        select_number.click()


    def page_one(self):
        try:
            page_one = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/div[3]/ul/li[2]/a")
            page_one.click()
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False

        return is_button_clicked

    def page_two(self):
        try:
            page_two = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/div[3]/ul/li[3]/a")
            page_two.click()
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False

        return is_button_clicked

    def page_three(self):
        try:
            page_three = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/div[3]/ul/li[4]/a")
            page_three.click()
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False

        return is_button_clicked

    def page_number(self, page_number):
        try:
            page_selection = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div/div/div/div/div/div/div/div[3]/pagination/div/div[3]/ul/li[{}]/a".format(page_number+1))
            page_selection.click()                         
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False
    def previous_button(self):
        try:
            previous_button = self.driver.find_element(By.XPATH, "//*[@ng-click='selectPage(page - 1, $event)']")
            previous_button.click()
            is_button_clicked = True
            sleep(3)
        except Exception as error:
            print(error.__class__)
            is_button_clicked = False

        return is_button_clicked

