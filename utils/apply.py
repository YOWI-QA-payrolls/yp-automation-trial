from time import sleep

from selenium.webdriver.common.by import By

class reviewer_apply():
        
    def apply_button(self):
        click_apply_button = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/button[1]')
        click_apply_button.click()
        sleep(3)

        confirmation_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
        is_displayed = confirmation_dialog.is_displayed()

        return is_displayed


    def confirm_button(self):
        click_confirm_button = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[4]/div[7]/button[2]')
        click_confirm_button.click()
        sleep(1)

class recommender_apply():
    def apply_button(self):
        click_apply_button = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/button[1]')
        click_apply_button.click()
        sleep(3)

        confirmation_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[4]")
        is_displayed = confirmation_dialog.is_displayed()

        return is_displayed


    def confirm_button(self):
        click_confirm_button = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[4]/div[7]/button[2]')
        click_confirm_button.click()
    