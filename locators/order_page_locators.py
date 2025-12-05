from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок страницы
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счетчики
    ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # Раздел "В работе"
    IN_PROGRESS_TITLE = (By.XPATH, "//p[text()='В работе:']")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    
    # Список заказов в работе (номера)
    ORDER_NUMBERS_IN_PROGRESS = (By.CLASS_NAME, "OrderFeed_orderList__cBvyi")
