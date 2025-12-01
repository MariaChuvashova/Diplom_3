from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver import ActionChains
import allure
from urls import Url
import time


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(Url.BASE_URL)
    
    @allure.step('Нажать кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)
    
    @allure.step('Нажать кнопку "Лента заказов"')
    def click_order_feed_button(self):
        # Даем время если было модальное окно
        time.sleep(1)
        self.click_element(MainPageLocators.BUTTON_ORDER_FEED)
    
    @allure.step('Нажать на ингредиент (булку)')
    def click_bun_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
    
    @allure.step('Нажать на ингредиент (соус)')
    def click_sauce_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_SPICY_SAUCE)
    
    @allure.step('Получить текст заголовка модального окна')
    def get_modal_title(self):
        return self.get_element_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step('Получить название ингредиента в модальном окне')
    def get_modal_ingredient_name(self):
        return self.get_element_text(MainPageLocators.MODAL_INGREDIENT_NAME)
    
    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        time.sleep(1)
        try:
            self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        except:
            element = self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
        # Ждем полного закрытия
        time.sleep(1)
    
    @allure.step('Проверить видимость модального окна')
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_TITLE)
    
    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter(self):
        try:
            # Ищем счетчик на ингредиенте
            sauce_element = self.find_element(MainPageLocators.INGREDIENT_SPICY_SAUCE)
            parent = sauce_element.find_element(By.XPATH, "..")
            counter = parent.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0
    
    @allure.step('Добавить ингредиент в конструктор')
    def add_ingredient_to_constructor(self):
        source = self.find_element(MainPageLocators.INGREDIENT_SPICY_SAUCE)
        target = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
    
    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step('Получить номер заказа')
    def get_order_number(self):
        element = self.find_element(MainPageLocators.MODAL_ORDER_NUMBER)
        return element.text
    
    @allure.step('Проверить видимость конструктора')
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_AREA)
