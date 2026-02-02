from selenium.webdriver.common.by import By
class Confirmation():

    def click_confirm_yes(self):
        yes = self.driver.find_element(By.CLASS_NAME,'confirm')
        yes.click()

    def click_confirm_cancel(self):
        cancel = self.driver.find_element(By.CLASS_NAME,'confirm')
        cancel.click()