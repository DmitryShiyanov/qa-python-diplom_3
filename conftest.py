import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data
from data import Constants
from Practikum_UI.page_objects.login_page import LoginPage
from Practikum_UI.page_objects.main_page import MainPage
from Practikum_UI.page_objects.order_page import OrderPage


@pytest.fixture(params=['chrome','firefox'])
def driver(request):
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--window-size=1920,1080')
    data.browser_name = request.param
    if request.param == 'chrome':
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Constants.MAIN_PAGE_URL)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(f'{Constants.MAIN_PAGE_URL}{Constants.LOGIN_PAGE_URL}')
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(f'{Constants.MAIN_PAGE_URL}{Constants.ORDER_PAGE_URL}')
    return page
