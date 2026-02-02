 
from time import sleep


def click_whole_day_radio_button(self):
    whole_day = self.driver.find_element_by_xpath("//*[@id = 'whole_day']")
    whole_day.click()
    sleep(3)

def click_half_day_radio_button(self):
    half_day = self.driver.find_element_by_xpath("//*[@id = 'half_day']")
    half_day.click()
    sleep(3)