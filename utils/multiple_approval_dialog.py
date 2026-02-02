from selenium.webdriver.common.by import By

import time


def multiple_approval_dialog(self):
    multiple_approval_button = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/button[2]')
    multiple_approval_button.click()
    time.sleep(10)
