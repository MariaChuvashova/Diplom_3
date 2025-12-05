import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


@allure.feature('Работа с ингредиентами')
class TestIngredient:
    @allure.title('Открытие деталей ингредиента')
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            assert main_page.is_constructor_visible()
        
        with allure.step('Нажать на ингредиент (булку)'):
            main_page.click_bun_ingredient()
        
        with allure.step('Проверить открытие модального окна'):
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_TITLE)
            )
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title
        
        with allure.step('Проверить детали ингредиента'):
            ingredient_name = main_page.get_modal_ingredient_name()
            assert 'Флюоресцентная булка R2-D3' in ingredient_name
    
    @allure.title('Закрытие всплывающего окна')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
        
        with allure.step('Открыть детали ингредиента'):
            main_page.click_bun_ingredient()
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_TITLE)
            )
            modal_title = main_page.get_modal_title()
            assert 'Детали ингредиента' in modal_title
        
        with allure.step('Закрыть модальное окно'):
            main_page.close_modal()
        
        with allure.step('Проверить закрытие окна'):
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located(MainPageLocators.MODAL_CONTAINER)
            )
            # Используем исправленный метод
            assert not main_page.is_modal_visible_fixed()
    
    @allure.title('Проверка счетчика ингредиента (drag-and-drop)')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main_page.open()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
            )
            assert main_page.is_constructor_visible()
        
        with allure.step('Получить начальное значение счетчика'):
            initial_counter = main_page.get_ingredient_counter()
        
        with allure.step('Перетащить булку в конструктор'):
            main_page.drag_bun_to_constructor()
            # Ждем изменения счетчика
            WebDriverWait(driver, 10).until(
                lambda d: main_page.get_ingredient_counter() > initial_counter
            )
        
        with allure.step('Получить новое значение счетчика'):
            new_counter = main_page.get_ingredient_counter()
        
        with allure.step('Проверить увеличение счетчика'):
            assert new_counter > initial_counter, f"Счетчик не увеличился. Было: {initial_counter}, стало: {new_counter}"
