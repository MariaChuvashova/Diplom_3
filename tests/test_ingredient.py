import pytest
import allure
from pages.main_page import MainPage


class TestIngredient:
    @allure.title('Открытие всплывающего окна с деталями ингредиента')
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()

        with allure.step('Закрыть возможные модальные окна'):
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        with allure.step('Открыть детали ингредиента'):
            main_page.click_ingredient()

        with allure.step('Проверить заголовок модального окна'):
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title

    @allure.title('Закрытие всплывающего окна')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()

        with allure.step('Закрыть возможные модальные окна'):
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        with allure.step('Открыть детали ингредиента'):
            main_page.click_ingredient()

        with allure.step('Закрыть модальное окно'):
            main_page.close_modal()

        with allure.step('Проверить закрытие окна'):
            # Ждем, пока модальное окно скроется
            main_page.wait_modal_invisible()

    @allure.title('Увеличение счетчика ингредиента')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()

        with allure.step('Закрыть возможные модальные окна'):
            # Ждем исчезновения оверлея
            main_page.wait_overlay_hidden(overlay_type='modal')

        with allure.step('Получить начальное значение счетчика'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Перетащить булку в конструктор'):
            main_page.drag_bun_to_constructor()

        with allure.step('Проверить увеличение счетчика'):
            # Ждем, пока счетчик увеличится
            import time
            timeout = 10
            start_time = time.time()
            while time.time() - start_time < timeout:
                current_counter = main_page.get_ingredient_counter()
                if current_counter > initial_counter:
                    break
                time.sleep(0.5)
            else:
                assert False, f"Счетчик не увеличился за {timeout} секунд. Был: {initial_counter}, сейчас: {current_counter}"
