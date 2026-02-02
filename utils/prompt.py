from selenium.webdriver.common.by import By


def text(self):
    toast_container = self.driver.find_element(By.XPATH, "//*[@id='toast-container']/div/div/div/div[1]")
    actual_text = toast_container.text

    return actual_text
