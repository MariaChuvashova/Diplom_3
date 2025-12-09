import pytest
import allure
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrders:
    @allure.title('Увеличение счетчика "Выполнено за всё время"')
    def test_order_increases_all_time_counter(self, driver, registered_user_api):
        """
        Проверяем, что счетчик "Выполнено за всё время" увеличивается при создании заказа.
        """
        email, password = registered_user_api
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Шаг 1: Авторизация
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            assert main_page.is_constructor_visible()

        # Шаг 2: Запомнить старое значение счетчика
        with allure.step('Перейти в ленту заказов и запомнить счетчик'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()
            counter_old = order_page.get_all_time_counter()

        # Шаг 3: Вернуться в конструктор и создать заказ
        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            assert main_page.is_constructor_visible()

        with allure.step('Добавить ингредиенты в конструктор'):
            main_page.drag_bun_to_constructor()
            main_page.drag_sauce_to_constructor()

        with allure.step('Оформить заказ'):
            main_page.click_order_button()
            order_number = main_page.get_order_number()
            assert order_number is not None, "Номер заказа не появился"

        with allure.step('Закрыть модальное окно заказа'):
            # Ждём исчезновения спиннера загрузки
            main_page.wait_overlay_hidden(overlay_type='loading')
            # Закрываем модальное окно
            main_page.click_close_order_button()
            # Ждём, пока модальное окно полностью скроется
            main_page.wait_modal_invisible()
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        # Шаг 4: Проверить новое значение счетчика
        with allure.step('Перейти в ленту заказов и проверить счетчик'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()
            counter_new = order_page.get_all_time_counter()

        with allure.step('Убедиться, что счетчик увеличился'):
            assert counter_new > counter_old, f"Счетчик не увеличился: было {counter_old}, стало {counter_new}"

    @allure.title('Увеличение счетчика "Выполнено за сегодня"')
    def test_order_increases_today_counter(self, driver, registered_user_api):
        """
        Проверяем, что счетчик "Выполнено за сегодня" увеличивается при создании заказа.
        """
        email, password = registered_user_api
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Шаг 1: Авторизация
        with allure.step('Авторизоваться'):
            auth_page.open()
            auth_page.login(email, password)
            assert main_page.is_constructor_visible()

        # Шаг 2: Запомнить старое значение счетчика
        with allure.step('Перейти в ленту заказов и запомнить счетчик'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()
            counter_old = order_page.get_today_counter()

        # Шаг 3: Вернуться в конструктор и создать заказ
        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            assert main_page.is_constructor_visible()

        with allure.step('Добавить ингредиенты в конструктор'):
            main_page.drag_bun_to_constructor()
            main_page.drag_sauce_to_constructor()

        with allure.step('Оформить заказ'):
            main_page.click_order_button()
            order_number = main_page.get_order_number()
            assert order_number is not None, "Номер заказа не появился"

        with allure.step('Закрыть модальное окно заказа'):
            # Ждём исчезновения спиннера загрузки
            main_page.wait_overlay_hidden(overlay_type='loading')
            # Закрываем модальное окно
            main_page.click_close_order_button()
            # Ждём, пока модальное окно полностью скроется
            main_page.wait_modal_invisible()
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        # Шаг 4: Проверить новое значение счетчика
        with allure.step('Перейти в ленту заказов и проверить счетчик'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()
            counter_new = order_page.get_today_counter()

        with allure.step('Убедиться, что счетчик увеличился'):
            assert counter_new > counter_old, f"Счетчик не увеличился: было {counter_old}, стало {counter_new}"
