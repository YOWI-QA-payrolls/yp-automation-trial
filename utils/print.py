from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import os
from utils.drop_down_arrow import Dropdown

class Print:

    def click_print_button(self):
        ''' click print button '''
        
        Dropdown.click_dropdown_arrow(self)

        sleep(2)
        print_button = self.driver.find_element(By.XPATH, "//*[@ng-if='main.has_print']")
        print_button.click()
        sleep(10)
