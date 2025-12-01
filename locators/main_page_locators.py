from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[p[text()='Конструктор']]")
    BUTTON_ORDER_FEED = (By.XPATH, "//a[p[text()='Лента Заказов']]")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[p[text()='Личный Кабинет']]")
    
    # Ингредиенты
    INGREDIENT_FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_SPICY_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")
    
    # Модальные окна
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal_container__Wo2l_")
    
    # Конструктор
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__29Cd7")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Счетчик ингредиента (цифра сверху на ингредиенте)
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__ZNLkj")
    
    # Номер заказа (после оформления)
    MODAL_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal_title_shadow__')]")
