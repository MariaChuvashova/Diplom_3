import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Url
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(Url.BASE_URL)
    
    @allure.step('Нажать кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)
    
    @allure.step('Нажать кнопку "Лента заказов"')
    def click_order_feed_button(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(MainPageLocators.MODAL_CONTAINER)
            )
        except:
            pass
        self.wait_for_element_clickable(MainPageLocators.BUTTON_ORDER_FEED)
        self.click_element(MainPageLocators.BUTTON_ORDER_FEED)
    
    @allure.step('Нажать на ингредиент (булку)')
    def click_bun_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
    
    @allure.step('Нажать на ингредиент (соус)')
    def click_sauce_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_SPICY_SAUCE)
    
    @allure.step('Получить заголовок модального окна')
    def get_modal_title(self):
        return self.get_element_text(MainPageLocators.MODAL_TITLE)
    
    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_element_to_disappear(MainPageLocators.MODAL_CONTAINER, timeout=3)
    
    @allure.step('Проверить видимость модального окна')
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_TITLE, timeout=2)
    
    @allure.step('Проверить, что конструктор виден')
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step('Перетащить булку в конструктор')
    def drag_bun_to_constructor(self):
        self.drag_and_drop_element(
            MainPageLocators.INGREDIENT_FLUORESCENT_BUN,
            MainPageLocators.CONSTRUCTOR_AREA
        )
    
    @allure.step('Перетащить соус в конструктор')
    def drag_sauce_to_constructor(self):
        self.drag_and_drop_element(
            MainPageLocators.INGREDIENT_SPICY_SAUCE,
            MainPageLocators.CONSTRUCTOR_AREA
        )
    
    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter(self):
        try:
            return int(self.get_element_text(MainPageLocators.INGREDIENT_COUNTER))
        except:
            return 0
    
    @allure.step('Получить текст ингредиента в модальном окне')
    def get_modal_ingredient_name(self):
        return self.get_element_text(MainPageLocators.MODAL_INGREDIENT_NAME)
    
    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step('Получить номер заказа из модального окна')
    def get_order_number(self):
        order_text = self.get_element_text(MainPageLocators.MODAL_ORDER_NUMBER)
        # Извлекаем только цифры из текста
        import re
        numbers = re.findall(r'\d+', order_text)
        return int(numbers[0]) if numbers else None

    @allure.step('Проверить видимость модального окна (исправленный)')
    def is_modal_visible_fixed(self):
        """Проверяет, что модальное окно видимо на странице"""
        try:
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.wait import WebDriverWait
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_CONTAINER)
            )
            return True
        except:
            return False
