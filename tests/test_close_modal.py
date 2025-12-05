import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature('Закрытие модального окна')
class TestCloseModal:
    @allure.title('Закрытие окна деталей ингредиента по крестику')
    def test_close_modal_by_cross(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
        
        with allure.step('Открыть детали ингредиента'):
            main_page.click_bun_ingredient()
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_TITLE)
            )
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title
        
        with allure.step('Закрыть модальное окно крестиком'):
            main_page.close_modal()
        
        with allure.step('Проверить что окно закрыто'):
            main_page.wait_element_to_disappear(MainPageLocators.MODAL_CONTAINER, timeout=5)
            assert not main_page.is_modal_visible()
