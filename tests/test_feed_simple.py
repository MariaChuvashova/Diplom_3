import pytest
from locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


@allure.feature('Лента заказов - простые тесты')
class TestFeedSimple:
    @allure.title('Проверка загрузки ленты заказов')
    def test_feed_page_loads(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.FEED_TITLE)
            )
        
        with allure.step('Проверить заголовок'):
            assert order_page.is_order_feed_loaded()
    
    @allure.title('Проверка наличия счетчиков')
    def test_counters_exist(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.FEED_TITLE)
            )
        
        with allure.step('Проверить счетчик за все время'):
            all_time = order_page.get_all_time_counter()
            assert isinstance(all_time, int)
            assert all_time >= 0
        
        with allure.step('Проверить счетчик за сегодня'):
            today = order_page.get_today_counter()
            assert isinstance(today, int)
            assert today >= 0
    
    @allure.title('Навигация конструктор ↔ лента заказов')
    def test_navigation_between(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Из конструктора в ленту заказов'):
            main_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
            main_page.click_order_feed_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.FEED_TITLE)
            )
            assert order_page.is_order_feed_loaded()
        
        with allure.step('Из ленты заказов в конструктор'):
            main_page.click_constructor_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
