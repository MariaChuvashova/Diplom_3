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
        self.click_element(AuthPageLocators.BUTTON_LOGIN)
    
    @allure.step('Выполнить авторизацию')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step('Проверить загрузку страницы авторизации')
    def is_login_page_loaded(self):
        return self.is_element_visible(AuthPageLocators.TITLE_LOGIN)
