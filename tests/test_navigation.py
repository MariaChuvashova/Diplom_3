import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestNavigation:
    @allure.title('Переход в ленту заказов из конструктора')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Дождаться загрузки конструктора'):
            assert main_page.is_constructor_visible()

        with allure.step('Закрыть возможные модальные окна'):
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        with allure.step('Нажать на кнопку "Лента заказов"'):
            main_page.click_order_feed_button()

        with allure.step('Проверить переход в ленту заказов'):
            assert order_page.is_order_feed_loaded()

    @allure.title('Переход из ленты заказов в конструктор')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_from_feed_to_constructor(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Дождаться загрузки конструктора'):
            assert main_page.is_constructor_visible()

        with allure.step('Перейти в ленту заказов'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()

        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            assert main_page.is_constructor_visible()

    @allure.title('Переход между конструктором и лентой заказов')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation_constructor_to_feed_and_back(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Дождаться загрузки конструктора'):
            assert main_page.is_constructor_visible()

        with allure.step('Перейти в ленту заказов'):
            main_page.click_order_feed_button()
            assert order_page.is_order_feed_loaded()

        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor_button()
            assert main_page.is_constructor_visible()
