import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from helpers import generate_email, generate_password, generate_name
from urls import Url


@pytest.fixture
def driver():
    """Фикстура драйвера только для Firefox для отладки"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    # После теста пытаемся закрыть все модальные окна
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ESCAPE).perform()
    except:
        pass
    driver.quit()


@pytest.fixture
def create_user():
    """Фикстура генерации данных пользователя"""
    email = generate_email()
    password = generate_password()
    name = generate_name()
    return {
        "email": email,
        "password": password,
        "name": name
    }


@pytest.fixture
def registered_user():
    """Фикстура создания зарегистрированного пользователя"""
    email = generate_email()
    password = generate_password()
    name = generate_name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(f"{Url.BASE_URL}/api/auth/register", json=payload)
    response.raise_for_status()
    return payload

@pytest.fixture
def registered_user_api():
    """Создание пользователя через API с последующим удаление"""
    email = generate_email()
    password = generate_password()
    name = generate_name()
    
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    
    response = requests.post(f"{Url.BASE_URL}/api/auth/register", json=payload)
    assert response.status_code == 200
    
    yield email, password
    
    # Удаление пользователя после теста
    access_token = response.json().get("accessToken")
    if access_token:
        headers = {"Authorization": f"Bearer {access_token}"}
        requests.delete(f"{Url.BASE_URL}/api/auth/user", headers=headers)
