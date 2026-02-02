from selenium.webdriver.common.by import By


def checkbox(self):
    filter_checkbox = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div/div/div/div/form/div[4]/label/div/ins')
    filter_checkbox.click()

    is_selected = filter_checkbox.is_selected()
    return is_selected
