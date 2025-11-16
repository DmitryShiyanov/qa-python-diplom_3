import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from Practikum_UI.locators.main_page_locators import MainPageLocators
from Practikum_UI.page_objects.base_page import BasePage


@allure.title('Класс методов главной страницы')
class MainPage(BasePage):


    @allure.step('Метод клика по кнопке Конструктор')
    def click_constructor_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Метод клика по кнопке Лента Заказов')
    def click_order_feed_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Метод изьятия текста с локатора Соберите Бургер')
    def check_burger_text_success(self):
        return self.get_field_text(MainPageLocators.BURGER_TEXT)

    @allure.step('Метод изьятия текста с локатора Лента заказов')
    def check_order_text_success(self):
        return self.get_field_text(MainPageLocators.ORDER_FEED_TEXT)

    @allure.step('Клик на изображение булки')
    def click_bun_image(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(MainPageLocators.BUN_FLUR)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(MainPageLocators.BUN_FLUR)

    @allure.step('Проверка атрибута всплывающего окна')
    def check_window_attribute(self):
        element = self.find_element_with_wait(MainPageLocators.CONTENT_BOX)
        return element.get_attribute('class')

    @allure.step('Закрывает всплывающее окно')
    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(MainPageLocators.CONTENT_BOX_ESCAPE).perform()

    @allure.step('Метод клика по escape')
    def click_escape_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(MainPageLocators.CONTENT_BOX_ESCAPE)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(MainPageLocators.CONTENT_BOX_ESCAPE)

    @allure.step('Ожидание когда исчезнет всплывающее окно')
    def wait_until_element_closed(self):
        element = self.find_element_with_wait(MainPageLocators.CONTENT_BOX_2)
        return element.get_attribute('class')

    @allure.step('Ожидание')
    def wait_method(self):
        WebDriverWait(self.driver, 5)

    @allure.step('Метод перетаскивания ингредиентов')
    def drug_and_drop_method_chrome(self):
        elem_from = self.find_element_with_wait(MainPageLocators.BUN_FLUR)
        elem_to = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_FIELD)
        action = ActionChains(self.driver)
        action.drag_and_drop(elem_from, elem_to).perform()

    @allure.step('Забираем значение с каунтера')
    def get_text_from_counter(self):
        return self.get_field_text(MainPageLocators.BUN_COUNTER)

    @allure.step('Забираем значение с деталей заказа')
    def get_text_from_order_text(self):
        return self.get_field_text(MainPageLocators.ORDER_TEXT_BEGIN)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        try:
            number = self.wait_method_for_order(MainPageLocators.ORDER_NUMBER)
            return number
        except TimeoutException:
            pass

    @allure.step('Метод клика по кнопке заказа')
    def click_on_order_btn(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(MainPageLocators.ORDER_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(MainPageLocators.ORDER_BUTTON)

    @allure.step('Забираем значение текста с локатора заказа')
    def get_text_from_order_number(self):
        return self.get_field_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Метод ожидания заказа 9999')
    def wait_order_method(self):
        self.wait_method_for_order(MainPageLocators.ORDER_NUMBER)

    @allure.step('Шаг драг и дроп')
    def create_order(self):
        if Constants.browser_name == 'chrome':
            self.drug_and_drop_method_chrome()
        else:
            self.drag_and_drop_element_firefox(MainPageLocators.BUN_FLUR, MainPageLocators.CONSTRUCTOR_FIELD)
