import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть ленту заказов'):
            order_page.open()
            assert order_page.is_order_feed_loaded()
        
        with allure.step('Нажать на кнопку "Конструктор"'):
            main_page.click_constructor_button()
        
        with allure.step('Проверить переход на конструктор'):
            assert main_page.is_constructor_visible()
    
    @allure.title('Переход по клику на "Лента заказов"')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()
        
        with allure.step('Нажать на кнопку "Лента заказов"'):
            # Если есть открытые модальные окна - закроем их
            try:
                main_page.close_modal()
            except:
                pass
            import time
            time.sleep(1)  # дополнительная пауза
            main_page.click_order_feed_button()
        
        with allure.step('Проверить переход в ленту заказов'):
            assert order_page.is_order_feed_loaded()
