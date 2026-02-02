from selenium import webdriver

def driversetup():   
    "Location of local chromedriver"
    driver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

    return driver

def main_url():
    "To be tested staging or live website url"

    url = "https://yp.yahshuasupport.com"

    return url

