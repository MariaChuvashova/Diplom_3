import pytest
import allure
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
            main_page.click_ingredient()
            assert main_page.is_modal_visible()
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title
        
        with allure.step('Закрыть модальное окно крестиком'):
            main_page.close_modal()
        
        with allure.step('Проверить что окно закрыто'):
            assert not main_page.is_modal_visible()
