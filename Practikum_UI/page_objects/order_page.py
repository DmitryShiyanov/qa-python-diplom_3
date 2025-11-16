import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from Practikum_UI.locators.order_page_locators import OrderPageLocators
from Practikum_UI.page_objects.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Метод клика по кнопке Лента Заказов')
    def click_order_feed_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(OrderPageLocators.ORDER_FEED_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(OrderPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Метод клика по заказу')
    def click_order(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(OrderPageLocators.FIRST_ORDER_LINK)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(OrderPageLocators.FIRST_ORDER_LINK)

    @allure.step('Метод проверки всклывающего окна')
    def check_content_box_active(self):
        element = self.find_element_with_wait(OrderPageLocators.ORDER_BOX_LOCATOR)
        return element.get_attribute('class')

    @allure.step('Забираем значение текста с локатора заказа "за все время"')
    def get_text_old_order_number_for_all_days(self):
        return self.get_field_text(OrderPageLocators.ALL_TIME_ORDERS)

    @allure.step('Забираем значение текста с локатора заказа "за сегодня"')
    def get_old_order_number_for_today(self):
        return self.get_field_text(OrderPageLocators.TODAY_ORDERS)

    @allure.step('Забираем номер заказа из "в работе"')
    def get_order_number_from_work_place(self):
        WebDriverWait(self.driver, 3)
        return self.get_field_text(OrderPageLocators.ORDERS_IN_WORK)

    @allure.step('Переход на главную страницу')
    def main_page_step(self):
        self.go_to_url(Constants.MAIN_PAGE_URL)

    @allure.step('Создаем список всех заказов')
    def find_all_orders(self):
        orders = self.find_elements_with_wait(OrderPageLocators.LIST_ORDERS)
        list_orders = []
        for order in orders:
            new_order = order.text.replace('#0', '')
            list_orders.append(new_order)
        return list_orders

    @allure.step('Ожидание появления заказа в списке "в работе"')
    def wait_method_for_order_in_work(self, number):
        try:
            WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(OrderPageLocators.ORDERS_IN_WORK, number))
        except TimeoutException:
            pass
