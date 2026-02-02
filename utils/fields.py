from tkinter import dialog
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def input_reason_field(self, input_data, module):
    input_reason = self.driver.find_element_by_xpath("//*[@ng-model = '{}.reason']".format(module))
    input_reason.send_keys(input_data)
    sleep(5)
