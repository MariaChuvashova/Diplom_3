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
