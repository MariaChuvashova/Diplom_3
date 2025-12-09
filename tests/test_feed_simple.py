import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Лента заказов - простые тесты')
class TestFeedSimple:
    @allure.title('Проверка загрузки ленты заказов')
    def test_feed_page_loads(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
        
        with allure.step('Проверить заголовок'):
            assert order_page.is_order_feed_loaded()
    
    @allure.title('Проверка счетчика "Выполнено за все время"')
    def test_all_time_counter_exists(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
        
        with allure.step('Проверить счетчик за все время'):
            all_time = order_page.get_all_time_counter()
            assert isinstance(all_time, int)
            assert all_time >= 0
    
    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_today_counter_exists(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
        
        with allure.step('Проверить счетчик за сегодня'):
            today = order_page.get_today_counter()
            assert isinstance(today, int)
            assert today >= 0
    
    @allure.title('Навигация конструктор ↔ лента заказов')
    def test_navigation_between(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()
        
        with allure.step('Перейти в ленту заказов'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()
        
        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            assert main_page.is_constructor_visible()
