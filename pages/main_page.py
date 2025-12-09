import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Url


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(Url.BASE_URL)

    @allure.step('Нажать кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Нажать кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)

    @allure.step('Получить текст заголовка модального окна')
    def get_modal_title(self):
        return self.get_element_text(MainPageLocators.MODAL_TITLE)

    @allure.step('Получить название ингредиента в модальном окне')
    def get_modal_ingredient_name(self):
        return self.get_element_text(MainPageLocators.MODAL_INGREDIENT_NAME)

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        # Находим крестик
        close_button = self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        # Используем ActionChains для клика, игнорируя перекрытие
        actions = ActionChains(self.driver)
        actions.move_to_element(close_button).click().perform()

    @allure.step('Проверить видимость конструктора')
    def is_constructor_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_AREA, timeout=5)
            return True
        except:
            return False

    @allure.step('Проверить видимость модального окна')
    def is_modal_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL_CONTAINER, timeout=5)
            return True
        except:
            return False

    @allure.step('Перетащить булку в конструктор')
    def drag_bun_to_constructor(self):
        source = MainPageLocators.INGREDIENT_FLUORESCENT_BUN
        target = MainPageLocators.CONSTRUCTOR_AREA
        self.drag_and_drop_element(source, target)

    @allure.step('Перетащить соус в конструктор')
    def drag_sauce_to_constructor(self):
        source = MainPageLocators.INGREDIENT_SPICY_SAUCE
        target = MainPageLocators.CONSTRUCTOR_AREA
        self.drag_and_drop_element(source, target)

    @allure.step('Получить счетчик ингредиента')
    def get_ingredient_counter(self):
        try:
            return int(self.get_element_text(MainPageLocators.INGREDIENT_COUNTER))
        except:
            return 0

    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL_ORDER_NUMBER, timeout=10)
            return self.get_element_text(MainPageLocators.MODAL_ORDER_NUMBER)
        except:
            return None

    @allure.step('Дождаться скрытия оверлея')
    def wait_overlay_hidden(self, overlay_type='loading'):
        if overlay_type == 'loading':
            locator = MainPageLocators.LOADING_OVERLAY
        else:
            locator = MainPageLocators.MODAL_OVERLAY
        self.wait_for_element_invisible(locator)

    @allure.step('Дождаться скрытия модального окна')
    def wait_modal_invisible(self, timeout=10):
        self.wait_for_element_invisible(MainPageLocators.MODAL_CONTAINER, timeout)

    @allure.step('Закрыть модальное окно заказа (специальная кнопка)')
    def click_close_order_button(self):
        from selenium.webdriver.common.action_chains import ActionChains
        # Ждём, пока кнопка станет кликабельной, и кликаем через ActionChains
        close_button = self.wait_for_element_clickable(MainPageLocators.ORDER_CLOSE_BUTTON, timeout=10)
        actions = ActionChains(self.driver)
        actions.move_to_element(close_button).click().perform()
