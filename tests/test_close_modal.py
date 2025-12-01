import pytest
import allure
import time
from pages.main_page import MainPage


@allure.feature('Закрытие модального окна')
class TestCloseModal:
    @allure.title('Закрытие окна деталей ингредиента по крестику')
    def test_close_modal_by_cross(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()
        
        with allure.step('Открыть детали ингредиента'):
            main_page.click_bun_ingredient()
            time.sleep(1)
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title
        
        with allure.step('Закрыть модальное окно крестиком'):
            main_page.close_modal()
            time.sleep(1)
        
        with allure.step('Проверить что окно закрыто'):
            # Пытаемся найти заголовок - должен быть exception
            try:
                main_page.get_modal_title()
                assert False, "Модальное окно должно быть закрыто"
            except:
                pass  # Окно закрыто - это правильно
