import os

from selenium.webdriver.common.by import By
from time import sleep


class reviewer_attachment():

    def attach_file(self, file_path):
        try:
            drop_files = self.driver.find_element(By.XPATH, "//*[@id='page-top']/input")
            drop_files.send_keys(file_path)
            sleep(3)
            file_attached = True
        except Exception as error:
            print(error.__class__)
            file_attached = False

        try:
            error_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]").is_displayed()
            if error_dialog is True: file_attached = False
            error_dialog_displayed = True
        except Exception as error:
            print(error.__class__)
            error_dialog_displayed = False

        return [file_attached, error_dialog_displayed]


    def upload_button(self):
        click_upload_button = self.driver.find_element(By.ID, 'upload_now')
        click_upload_button.click()
        sleep(1)

        file_uploaded = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/div[6]/div/div/div/div/div[3]")
        file_name = file_uploaded.text
        print(file_name)

        return file_name


    def download_all(self):
        download_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/div[6]/a")
        download_all_button.click()
        sleep(5)

        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.zip'):
                    is_downloaded = True

            seconds += 1

        return is_downloaded


    def close_button(self):
        close = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[1]")
        close.click()
        sleep(5)

        attachment_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_displayed = attachment_dialog.is_displayed()

        return is_displayed


    def error_notif_ok_button(self):
        ok_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/div[7]/button[2]")
        ok_button.click()
        sleep(3)

class recommender_attachment():

    def attach_file(self, file_path):
        try:
            drop_files = self.driver.find_element(By.XPATH, "//*[@id='page-top']/input")
            drop_files.send_keys(file_path)
            sleep(3)
            file_attached = True
        except Exception as error:
            print(error.__class__)
            file_attached = False

        try:
            error_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]").is_displayed()
            if error_dialog is True: file_attached = False
            error_dialog_displayed = True
        except Exception as error:
            print(error.__class__)
            error_dialog_displayed = False

            return [file_attached, error_dialog_displayed]


    def upload_button(self):
        click_upload_button = self.driver.find_element(By.ID, 'upload_now')
        click_upload_button.click()
        sleep(1)

        file_uploaded = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/div[6]/div/div/div/div/div[3]")
        file_name = file_uploaded.text
        print(file_name)

        return file_name


    def download_all(self):
        download_all_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[2]/div/div[2]/div[6]/a")
        download_all_button.click()
        sleep(5)

        timeout = 5
        seconds = 0
        is_downloaded = True
        while is_downloaded and seconds < timeout:
            sleep(1)
            is_downloaded = False
            files = os.listdir("C://Users/HP/Downloads")

            for fname in files:
                if fname.endswith('.zip'):
                    is_downloaded = True

            seconds += 1

        return is_downloaded


    def close_button(self):
        close = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div/div/div[3]/div/button[1]")
        close.click()
        sleep(5)

        attachment_dialog = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/div")
        is_displayed = not attachment_dialog.is_displayed()

        return is_displayed


    def error_notif_ok_button(self):
        ok_button = self.driver.find_element(By.XPATH, "//*[@id='page-top']/div[6]/div[7]/button[2]")
        ok_button.click()
        sleep(3)
