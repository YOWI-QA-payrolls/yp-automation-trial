from time import sleep, time
from selenium import webdriver

class WaitElement():

    def to_appear(self, element_variable_name):
        """wait the element to appear then it will be targetted through selenium"""

        element = element_variable_name.is_displayed()
        if element == True:
            pass
        else:
            sleep(0.3)
            self.to_appear(self, element_variable_name)
