from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import os

class Dropdown:

    def click_dropdown_arrow(self):
        ''' click dropdown button beside advance filter '''
        
        drop_down = self.driver.find_element(By.XPATH, "//*[@class='btn btn-default dropdown-toggle ng-scope']")
        drop_down.click()
        sleep(2)
