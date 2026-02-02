from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import os
from utils.drop_down_arrow import Dropdown

class Export:

    def click_export_button(self):
        ''' click export button '''
        
        Dropdown.click_dropdown_arrow(self)

        sleep(2)
        export_button = self.driver.find_element(By.XPATH, "//*[@class='dropdown-menu pull-right']/li/a")
        export_button.click()
        sleep(10)
