import pytest
import allure
import requests
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from helpers import generate_email, generate_password, generate_name
from urls import Url
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


@allure.feature('Лента заказов')
class TestOrders:
    @allure.title('Увеличение счетчика "Выполнено за всё время"')
    @pytest.mark.parametrize('counter_type', ['all_time', 'today'])
    def test_order_creation_counters(self, driver, registered_user_api, counter_type):
        """
        Проверяем, что счетчики увеличиваются при создании заказа.
        """
        email, password = registered_user_api
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Шаг 1: Авторизация
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
        
        # Шаг 2: Запомнить старые значения счетчиков
        with allure.step('Перейти в ленту заказов и запомнить счетчики'):
            main_page.click_order_feed_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(order_page.locators.FEED_TITLE)
            )
            counter_old = order_page.get_counter(counter_type)
        
        # Шаг 3: Вернуться в конструктор и создать заказ
        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
        
        with allure.step('Добавить ингредиенты в конструктор'):
            main_page.drag_bun_to_constructor()
            main_page.drag_sauce_to_constructor()
            # Ждем добавления ингредиентов
            WebDriverWait(driver, 5).until(
                lambda d: main_page.get_ingredient_counter() >= 2
            )
        
        with allure.step('Оформить заказ'):
            main_page.click_order_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_ORDER_NUMBER)
            )
            order_number = main_page.get_order_number()
            assert order_number is not None, "Номер заказа не появился"
        
        with allure.step('Закрыть модальное окно заказа'):
            main_page.close_modal()
            main_page.wait_element_to_disappear(MainPageLocators.MODAL_CONTAINER)
        
        # Шаг 4: Проверить новые значения счетчиков
        with allure.step('Проверить увеличение счетчика'):
            main_page.click_order_feed_button()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(order_page.locators.FEED_TITLE)
            )
            counter_new = order_page.get_counter(counter_type)
            
            assert counter_new == counter_old + 1, (
                f'Счетчик не увеличился. Тип: {counter_type}. '
                f'Было: {counter_old}, стало: {counter_new}'
            )
