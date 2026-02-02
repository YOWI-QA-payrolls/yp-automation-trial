from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By

class RightClick():

    def user(self, employee_name):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[text()='{}']".format(employee_name))).perform();
        action.context_click().perform()

    def first_row(self, module):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='{}']/tbody/tr[1]".format(module))).perform();
        action.context_click().perform()
        
    def first_row_leave(self):

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='table']/tbody/tr[11]/td[3]")).perform();
        action.context_click().perform()
        
    def action(self, select_record):
        action = ActionChains(self.driver)
        action.context_click(select_record).perform()
        sleep(1)

        option_1 = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[3]/ul/li[1]/a").is_displayed()
        option_2 = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[3]/ul/li[2]/a").is_displayed()

        if option_1 and option_2 is True : is_option_displayed = True

        return is_option_displayed

    def view_logs_option(self):

        logs_option = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[3]/ul/li[1]/a")
        logs_option.click()
        sleep(5)

        self.driver.switch_to.window(self.driver.window_handles[1])
        window_title = self.driver.title

        return window_title

    def attach_option(self):

        attach_option = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[3]/ul/li[2]/a")
        attach_option.click()
        sleep(5)

        attachment_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_displayed = attachment_dialog.is_displayed()

        return is_displayed
