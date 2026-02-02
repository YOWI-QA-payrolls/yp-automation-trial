from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import os

class GearIcon:

    def click_gear_icon(self):
        ''' click gear icon '''
        
        gear_icon = self.driver.find_element(By.XPATH, "//*[@popover-title='Columns']")
        gear_icon.click()
        sleep(2)

    def click_select_all_check_box(self):
        ''' click select all '''

        select_all = self.driver.find_element(By.XPATH,"//*[@id='select_all']")
        select_all.click()
        sleep(2)

