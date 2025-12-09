import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from urls import Url

from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Открыть ленту заказов')
    def open(self):
        self.driver.get(Url.BASE_URL + '/feed')

    @allure.step('Дождаться загрузки ленты заказов')
    def is_order_feed_loaded(self):
        try:
            self.wait_for_element_visible(OrderPageLocators.FEED_TITLE, timeout=10)
            return True
        except:
            return False

    @allure.step('Получить счетчик "Выполнено за все время"')
    def get_all_time_counter(self):
        try:
            self.wait_for_element_visible(OrderPageLocators.ALL_TIME_COUNTER, timeout=10)
            text = self.get_element_text(OrderPageLocators.ALL_TIME_COUNTER)
            return int(text) if text.isdigit() else 0
        except:
            return 0

    @allure.step('Получить счетчик "Выполнено за сегодня"')
    def get_today_counter(self):
        try:
            self.wait_for_element_visible(OrderPageLocators.TODAY_COUNTER, timeout=10)
            text = self.get_element_text(OrderPageLocators.TODAY_COUNTER)
            return int(text) if text.isdigit() else 0
        except:
            return 0

    @allure.step('Получить номер последнего заказа в работе')
    def get_in_progress_order_number(self):
        try:
            self.wait_for_element_visible(OrderPageLocators.IN_PROGRESS_SECTION, timeout=10)
            elements = self.find_elements(OrderPageLocators.ORDER_NUMBERS_IN_PROGRESS)
            return elements[0].text if elements else None
        except:
            return None

    @allure.step('Дождаться обновления счетчиков')
    def wait_counters_loaded(self, counter_type='all_time'):
        # Ожидаем появления счетчика
        if counter_type == 'all_time':
            self.wait_for_element_visible(OrderPageLocators.ALL_TIME_COUNTER, timeout=10)
        elif counter_type == 'today':
            self.wait_for_element_visible(OrderPageLocators.TODAY_COUNTER, timeout=10)
        else:
            self.wait_for_element_visible(OrderPageLocators.ALL_TIME_COUNTER, timeout=10)
            self.wait_for_element_visible(OrderPageLocators.TODAY_COUNTER, timeout=10)

    @allure.step('Проверить наличие раздела "В работе"')
    def is_in_progress_section_visible(self):
        try:
            self.wait_for_element_visible(OrderPageLocators.IN_PROGRESS_SECTION, timeout=5)
            return True
        except:
            return False

    @allure.step('Дождаться увеличения счетчика')
    def wait_counter_increased(self, counter_type, initial_value, timeout=10):
        """
        Ждем, пока счетчик увеличится относительно initial_value.
        counter_type: 'all_time' или 'today'
        """
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            if counter_type == 'all_time':
                current = self.get_all_time_counter()
            else:
                current = self.get_today_counter()
            if current > initial_value:
                return True
            time.sleep(0.5)
        # Если не увеличился за timeout
        return False
