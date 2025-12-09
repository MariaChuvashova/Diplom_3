from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
import allure
from urls import Url


class AuthPage(BasePage):
    @allure.step('Открыть страницу авторизации')
    def open(self):
        self.driver.get(f"{Url.BASE_URL}/login")

    @allure.step('Ввести email')
    def enter_email(self, email):
        email_input = self.find_element(AuthPageLocators.INPUT_EMAIL)
        email_input.clear()
        email_input.send_keys(email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        password_input = self.find_element(AuthPageLocators.INPUT_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        # Используем ActionChains для клика, игнорируя перекрытие
        login_button = self.find_element(AuthPageLocators.BUTTON_LOGIN)
        actions = ActionChains(self.driver)
        actions.move_to_element(login_button).click().perform()

    @allure.step('Выполнить авторизацию')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step('Проверить загрузку страницы авторизации')
    def is_login_page_loaded(self):
        try:
            self.wait_for_element_visible(AuthPageLocators.TITLE_LOGIN, timeout=5)
            return True
        except:
            return False
