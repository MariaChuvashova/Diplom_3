from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    
    @allure.step('Найти элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )
    
    @allure.step('Найти все элементы')
    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы {locator} не найдены"
        )
    
    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
        element.click()
    
    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
        return element.text
    
    @allure.step('Проверить видимость элемента')
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step('Ждать исчезновения элемента')
    def wait_element_to_disappear(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_locator, target_locator):
        from seletools.actions import drag_and_drop
        source_element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(source_locator)
        )
        target_element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(target_locator)
        )
        drag_and_drop(self.driver, source_element, target_element)
    
    @allure.step('Ждать кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step('Заполнить поле')
    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
