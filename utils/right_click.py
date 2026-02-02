from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


def action(self, select_record):
    action_select = ActionChains(self.driver)
    action_select.context_click(select_record).perform()
    sleep(2)

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
    attach = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[3]/ul/li[2]/a")
    attach.click()
    sleep(5)

    attachment_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
    dialog_displayed = attachment_dialog.is_displayed()

    return dialog_displayed
