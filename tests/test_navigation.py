import pytest
from locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.FEED_TITLE)
            )
            assert order_page.is_order_feed_loaded()
        
        with allure.step('Нажать на кнопку "Конструктор"'):
            main_page.click_constructor_button()
        
        with allure.step('Проверить переход на конструктор'):
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
    
    @allure.title('Переход по клику на "Лента заказов"')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
        
        with allure.step('Нажать на кнопку "Лента заказов"'):
            if main_page.is_modal_visible():
                main_page.close_modal()
            main_page.wait_for_element_clickable(MainPageLocators.BUTTON_ORDER_FEED)
            main_page.click_order_feed_button()
        
        with allure.step('Проверить переход в ленту заказов'):
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.FEED_TITLE)
            )
            assert order_page.is_order_feed_loaded()
