from selenium.webdriver.common.by import By


class MainPageLocators:
    # =================== НАВИГАЦИЯ ===================
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[p[text()='Конструктор']]")
    BUTTON_ORDER_FEED = (By.XPATH, "//a[p[text()='Лента Заказов']]")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[p[text()='Личный Кабинет']]")
    
    # =================== ИНГРЕДИЕНТЫ ===================
    INGREDIENT_FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_SPICY_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")
    
    # =================== МОДАЛЬНЫЕ ОКНА ===================
    MODAL_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and contains(text(), 'Флюоресцентная булка')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    MODAL_CONTAINER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    
    # =================== ОВЕРЛЕИ ===================
    LOADING_OVERLAY = (By.XPATH, '//img[contains(@class, "loading")]/parent::div')
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    # =================== КОНСТРУКТОР ===================
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # =================== СЧЕТЧИКИ ===================
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]")
    
    # =================== ЗАКАЗ ===================
    MODAL_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    # Кнопка закрытия модального окна заказа (специальная)
    ORDER_CLOSE_BUTTON = (By.XPATH, '//h2[contains(@class,"text_type_digits-large")]/parent::div/parent::div/button[contains(@class, "close")]')
