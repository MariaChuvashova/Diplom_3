from selenium.webdriver.common.by import By


class AuthPageLocators:
    # Форма авторизации
    INPUT_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    INPUT_PASSWORD = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    
    # Заголовок
    TITLE_LOGIN = (By.XPATH, "//h2[text()='Вход']")
