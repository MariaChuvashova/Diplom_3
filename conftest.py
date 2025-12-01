import pytest
from selenium import webdriver
import requests
from helpers import generate_email, generate_password, generate_name
from urls import Url


@pytest.fixture
def driver():
    """Фикстура драйвера только для Firefox для отладки"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
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
