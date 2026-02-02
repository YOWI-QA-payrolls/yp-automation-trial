from tkinter import dialog
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def click_leave_submit_button(self):

    submit_button = self.driver.find_element_by_id('leave_submit')
    self.driver.execute_script("arguments[0].click();", submit_button)
    sleep(3)