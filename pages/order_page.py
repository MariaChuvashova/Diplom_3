from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure
from urls import Url


class OrderPage(BasePage):
    @allure.step('Открыть ленту заказов')
    def open(self):
        self.driver.get(f"{Url.BASE_URL}/feed")
    
    @allure.step('Проверить загрузку ленты заказов')
    def is_order_feed_loaded(self):
        return self.is_element_visible(OrderPageLocators.FEED_TITLE)
    
    @allure.step('Получить счетчик за все время')
    def get_all_time_counter(self):
        counter = self.find_element(OrderPageLocators.ALL_TIME_COUNTER)
        return int(counter.text.replace(' ', '')) if counter.text else 0
    
    @allure.step('Получить счетчик за сегодня')
    def get_today_counter(self):
        counter = self.find_element(OrderPageLocators.TODAY_COUNTER)
        return int(counter.text.replace(' ', '')) if counter.text else 0
    
    @allure.step('Проверить наличие раздела "В работе"')
    def is_in_progress_section_visible(self):
        return self.is_element_visible(OrderPageLocators.IN_PROGRESS_SECTION)
    
    @allure.step('Получить заказы в работе')
    def get_orders_in_progress(self):
        orders = []
        if self.is_element_visible(OrderPageLocators.IN_PROGRESS_SECTION):
            section = self.find_element(OrderPageLocators.IN_PROGRESS_SECTION)
            order_elements = section.find_elements(By.TAG_NAME, "li")
            for order in order_elements:
                orders.append(order.text)
        return orders

    @allure.step('Дождаться загрузки счетчиков')
    def wait_counters_loaded(self, counter_type='all_time'):
        """Ждем загрузки счетчиков"""
        import time
        time.sleep(2)  # Простое ожидание, можно улучшить
    
    @allure.step('Получить значение счетчика')
    def get_counter(self, counter_type):
        """Получить значение счетчика по типу: 'all_time' или 'today'"""
        if counter_type == 'all_time':
            return self.get_all_time_counter()
        elif counter_type == 'today':
            return self.get_today_counter()
        else:
            raise ValueError(f"Неизвестный тип счетчика: {counter_type}")

    @allure.step('Ожидание загрузки счетчика')
    def wait_counters_loaded(self, counter_type):
        # Простое ожидание, можно улучшить
        import time
        time.sleep(2)
    
    @allure.step('Прочитать количество выполненных заказов')
    def get_counter(self, counter_type):
        if counter_type == 'all_time':
            return self.get_all_time_counter()
        elif counter_type == 'today':
            return self.get_today_counter()
        else:
            raise ValueError(f"Неизвестный тип счетчика: {counter_type}")

    @allure.step('Получить значение счетчика')
    def get_counter(self, counter_type):
        """
        Получить значение счетчика по типу.
        counter_type: 'all_time' или 'today'
        """
        if counter_type == 'all_time':
            return self.get_all_time_counter()
        elif counter_type == 'today':
            return self.get_today_counter()
        else:
            raise ValueError(f"Неизвестный тип счетчика: {counter_type}")
    
    @allure.step('Дождаться загрузки счетчиков')
    def wait_counters_loaded(self, counter_type=None):
        """Дождаться видимости счетчиков"""
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        if counter_type == 'all_time' or counter_type is None:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.ALL_TIME_COUNTER)
            )
        if counter_type == 'today' or counter_type is None:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.TODAY_COUNTER)
            )
