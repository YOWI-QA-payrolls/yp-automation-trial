from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from utils.setup import driversetup
from selenium.webdriver.common.action_chains import ActionChains 


def input_time_from_hour(self, input_data):
    hour = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[1]/input")
    hour.clear()
    hour.send_keys(input_data)

def input_time_from_minute(self, input_data):
    minute = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[2]/div/table/tbody/tr[2]/td[3]/input")
    minute.clear() 
    minute.send_keys(input_data)

def input_time_to_hour(self, input_data):
    hour = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[1]/input")
    hour.clear()
    hour.send_keys(input_data)

def input_time_to_minute(self, input_data):
    minute = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/form/span/div[5]/div[3]/div/table/tbody/tr[2]/td[3]/input")
    minute.clear()
    minute.send_keys(input_data)