import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Лента заказов - простые тесты')
class TestFeedSimple:
    @allure.title('Проверка загрузки ленты заказов')
    def test_feed_page_loads(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            time.sleep(2)
        
        with allure.step('Проверить заголовок'):
            assert order_page.is_order_feed_loaded()
            print("Лента заказов успешно загружена")
    
    @allure.title('Проверка наличия счетчиков')
    def test_counters_exist(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            time.sleep(2)
        
        with allure.step('Проверить счетчик за все время'):
            all_time = order_page.get_all_time_counter()
            print(f"Счетчик 'Выполнено за все время': {all_time}")
            assert isinstance(all_time, int)
            assert all_time >= 0
        
        with allure.step('Проверить счетчик за сегодня'):
            today = order_page.get_today_counter()
            print(f"Счетчик 'Выполнено за сегодня': {today}")
            assert isinstance(today, int)
            assert today >= 0
    
    @allure.title('Навигация конструктор ↔ лента заказов')
    def test_navigation_between(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Из конструктора в ленту заказов'):
            main_page.open()
            time.sleep(1)
            assert main_page.is_constructor_visible()
            main_page.click_order_feed_button()
            time.sleep(1)
            assert order_page.is_order_feed_loaded()
            print("Успешный переход: Конструктор → Лента заказов")
        
        with allure.step('Из ленты заказов в конструктор'):
            main_page.click_constructor_button()
            time.sleep(1)
            assert main_page.is_constructor_visible()
            print("Успешный переход: Лента заказов → Конструктор")
