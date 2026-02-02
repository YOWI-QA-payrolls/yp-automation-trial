from datetime import datetime
import pytest
from pytest import skip
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.sample_data import DataSetup
from utils.setup import *
from request_cookies import add_cookies

class Setup():

   def setup_method(self): 
      
      self.driver = driversetup()
      self.driver.maximize_window()
      target_url = main_url()
      url = "%s//dashboard//" % (target_url)
      self.driver.get(url)

      self.driver.delete_all_cookies()
      add_cookies(self)
      self.driver.refresh()

   def teardown_method(self, method):
      self.driver.quit()

class TestSetupData(Setup):

      sample_location = ["Test Location 5","Test Location 6","Test Location 7"]
      sample_department = ["Test Department 5","Test Department 6","Test Department 7"]
      sample_section = ["Test Section 5","Test Section 6","Test Section 7"]
      sample_position = ["Test Position 5","Test Position 6","Test Position 7"]
      sample_division = ["Test Division 5","Test Division 6","Test Division 7"]
      sample_job_level = ["Hourlies","Monthlies","Supervisor"]
      target_url = main_url()


      #@pytest.mark.skip(reason="passed")
      def test_data_sample_location(self):
         """location"""

         self.driver.get("%s/leadmans/settings/mains/main_page/#location" % (self.target_url))
         DataSetup.add_location(self, self.sample_location)


      def test_data_sample_department(self):
         """department"""

         self.driver.get("%s/leadmans/settings/mains/main_page/#department" % (self.target_url))
         DataSetup.add_department(self,self.sample_department, self.sample_location)

      def test_data_sample_section(self):
         """section"""
         
         self.driver.get("%s/leadmans/settings/mains/main_page/#section" % (self.target_url))
         DataSetup.add_section(self,self.sample_section, self.sample_department)

      def test_data_sample_section(self):
         """position"""

         self.driver.get("%s/leadmans/settings/mains/main_page/#position" % (self.target_url))
         DataSetup.add_position(self,self.sample_position, self.sample_department)

      def test_data_sample_division(self):
         """division"""

         self.driver.get("%s/leadmans/settings/mains/main_page/#division" % (self.target_url))
         DataSetup.add_division(self, self.sample_division)

      def test_data_sample_schedule(self):
         """schedule"""

         self.driver.get("%s/leadmans/settings/mains/main_page/#schedule" % (self.target_url))
         DataSetup.add_schedule(self)

      def test_data_sample_holidays(self):
         """holidays"""

      def test_data_sample_users(self):
         """users"""

         self.driver.get("%s/users/users/main_page/" % (self.target_url))
         DataSetup.add_users(self)