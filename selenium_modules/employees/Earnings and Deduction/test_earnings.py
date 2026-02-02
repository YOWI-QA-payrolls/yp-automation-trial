import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date as datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import searchbox, filter_effectivity, apply, right_click, pagination, prompt, auto_approval_review, record_per_page, record_field
from utils.advance_filter import reviewer_advance_filter_dropdown as advance_filter
from utils.approval_dialog import reviewer_approval_dialog as approval_dialog
from utils.attachment import reviewer_attachment as attachment
from utils.date import reviewer_date as date
from utils.set_site import reviewer_set_site as set_site


class test_earnings():
    def setup_method(self, method):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        # self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(width=1552, height=849)
        url = "https://yp.yahshuasupport.com/signin/?login=yes"
        self.driver.get(url)
        set_site.login(self)

        approval = self.driver.find_element(By.XPATH, '//*[@id="approval_list"]')
        approval_list = self.driver.find_element(By.XPATH, '//*[@id="undertime_overtime_approval"]/a')

        approval.click()
        approval_list.click()

        work_on_rest_day_approval = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div/div/''nav/ul/li[4]/a')
        work_on_rest_day_approval.click()
        sleep(10)

    def teardown_method(self, method):
        self.driver.quit()

    def check_clicking_recurring_menu(self, method):
        """ Check response clicking recurring under earnings in earnings and deductions menu. """

        expected_page = "Employee Recurring Earnings"

        click_employees = self.driver.find_element(By.XPATH,"//*[@id='employee_list']")
        click_employees.click()
        sleep(3)

        assert expected_page == "This page"

        self.driver.close()

        actual_data = search.box_function(self, input_data)
        is_search_icon_clicked = search.click_icon_button(self)
        displayed_relevant_result = search.check_all_search_results(self, input_data)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        actual_data = self.soup.find('table',{'id':'table'}).find('tbody').find('tr').find('td', class_="align_left ng-binding").text.strip().upper()

        # assert input_data in actual_data
        # assert is_search_icon_clicked == True