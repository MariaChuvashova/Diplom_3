from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_element_to_disappear(self, locator, timeout=5):
        self.wait.until(EC.invisibility_of_element_located(locator))
