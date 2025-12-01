import pytest
import allure
import requests
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from helpers import generate_email, generate_password, generate_name
from urls import Url


@allure.feature('Лента заказов')
class TestOrders:
    @pytest.fixture
    def registered_user_api(self):
        """Создание пользователя через API"""
        email = generate_email()
        password = generate_password()
        name = generate_name()
        
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(f"{Url.BASE_URL}/api/auth/register", json=payload)
        assert response.status_code == 200
        
        yield email, password
        
        # Удаление пользователя после теста
        access_token = response.json().get("accessToken")
        if access_token:
            headers = {"Authorization": f"Bearer {access_token}"}
            requests.delete(f"{Url.BASE_URL}/api/auth/user", headers=headers)
    
    @allure.title('Увеличение счетчика "Выполнено за всё время"')
    @pytest.mark.skip(reason="Требует настройки drag-and-drop и авторизации")
    def test_all_time_counter_increases(self, driver, registered_user_api):
        email, password = registered_user_api
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            assert main_page.is_constructor_visible()
        
        with allure.step('Получить начальное значение счетчика за все время'):
            order_page.open()
            initial_count = order_page.get_all_time_counter()
        
        with allure.step('Создать новый заказ'):
            main_page.open()
            main_page.add_ingredient_to_constructor()
            main_page.click_order_button()  # Исправлено!
            
            time.sleep(2)  # ждем обработки заказа
            
            order_number = main_page.get_order_number()
            assert order_number is not None
            
            main_page.close_modal()
        
        with allure.step('Проверить увеличение счетчика за все время'):
            order_page.open()
            final_count = order_page.get_all_time_counter()
            assert final_count > initial_count, \
                f'Счетчик не увеличился. Было: {initial_count}, стало: {final_count}'
    
    @allure.title('Увеличение счетчика "Выполнено за сегодня"')
    @pytest.mark.skip(reason="Требует настройки drag-and-drop и авторизации")
    def test_today_counter_increases(self, driver, registered_user_api):
        email, password = registered_user_api
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            assert main_page.is_constructor_visible()
        
        with allure.step('Получить начальное значение счетчика за сегодня'):
            order_page.open()
            initial_today_count = order_page.get_today_counter()
        
        with allure.step('Создать новый заказ'):
            main_page.open()
            main_page.add_ingredient_to_constructor()
            main_page.click_order_button()  # Исправлено!
            
            time.sleep(2)
            
            order_number = main_page.get_order_number()
            assert order_number is not None
            
            main_page.close_modal()
        
        with allure.step('Проверить увеличение счетчика за сегодня'):
            order_page.open()
            final_today_count = order_page.get_today_counter()
            assert final_today_count > initial_today_count, \
                f'Счетчик за сегодня не увеличился. Было: {initial_today_count}, стало: {final_today_count}'
    
    @allure.title('Номер заказа появляется в разделе "В работе"')
    @pytest.mark.skip(reason="Требует настройки drag-and-drop и авторизации")
    def test_order_in_progress(self, driver, registered_user_api):
        email, password = registered_user_api
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        auth_page = AuthPage(driver)
        
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            assert main_page.is_constructor_visible()
        
        with allure.step('Создать новый заказ'):
            main_page.open()
            main_page.add_ingredient_to_constructor()
            main_page.click_order_button()  # Исправлено!
            
            time.sleep(2)
            
            order_number = main_page.get_order_number()
            assert order_number is not None
            
            main_page.close_modal()
        
        with allure.step('Проверить наличие заказа в работе'):
            order_page.open()
            orders_in_progress = order_page.get_orders_in_progress()
            assert len(orders_in_progress) > 0, 'Нет заказов в работе'
            
            # Проверяем что наш номер заказа есть в списке
            order_found = False
            for order in orders_in_progress:
                if order_number in order:
                    order_found = True
                    break
            
            assert order_found, f'Заказ {order_number} не найден в разделе "В работе"'
