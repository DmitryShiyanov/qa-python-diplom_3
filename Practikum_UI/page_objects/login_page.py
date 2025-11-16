import allure
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from Practikum_UI.locators.login_page_locators import LoginPageLocators
from Practikum_UI.locators.main_page_locators import MainPageLocators
from Practikum_UI.page_objects.base_page import BasePage


@allure.title('Класс страницы логина и личного кабинета')
class LoginPage(BasePage):

    @allure.step('метод логина')
    def login_step(self):
        self.find_element_with_wait(LoginPageLocators.EMAIL_FIELD).send_keys(Constants.DEF_MAIL)
        self.find_element_with_wait(LoginPageLocators.PASSWORD_FIELD).send_keys(Constants.DEF_PASSWORD)
        self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON).click()

    @allure.step('метод клика на кнопку восстановить')
    def press_password_recovery(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BTN)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.PASSWORD_RECOVERY_BTN)

    @allure.step('Заполняем поле почты')
    def enter_mail_method(self):
        self.add_text_in_field(LoginPageLocators.EMAIL_FIELD, Constants.DEF_MAIL)
        self.click_to_element(LoginPageLocators.RECOVERY_BTN)

    @allure.step('Метод изьятия текста с кнопки Сохранить')
    def check_recovery_success(self):
        return self.get_field_text(LoginPageLocators.SAVE_BUTTON)

    @allure.step('Метод проверки поля на подсветку')
    def check_password_field_on_lighting(self):
        return self.find_element_with_wait(LoginPageLocators.DIV_CLASS).get_attribute('class')

    @allure.step('Метод изьятия текста с кнопки Сохранить')
    def check_recovery_text_field(self):
        return self.get_field_text(LoginPageLocators.RECOVERY_BTN)

    @allure.step('')
    def check_password_relay_status(self):
        return self.get_field_text(LoginPageLocators.RECOVERY_CODE_PLACE_2)

    @allure.step('Метод клика по кнопки скрытия пароля')
    def eye_click(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(LoginPageLocators.PASS_EYE)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.PASS_EYE)

    @allure.step('Метод ожидания исчезновения перекрывающего слоя')
    def wait_layout(self):
        try:
            self.wait_method_until_elem_visible(LoginPageLocators.OVERLAY_ELEM)
        except Exception:
            pass
    @allure.step('Метод клика по кнопке Личный кабинет')
    def click_lk_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Метод изьятия текста с локатора в ЛК')
    def check_login_success(self):
        return self.get_field_text(LoginPageLocators.ACCOUNT_TEXT)

    @allure.step('Клик по кнопке История заказов')
    def click_order_button(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(LoginPageLocators.ORDER_HISTORY_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка номера заказа')
    def check_order_number(self):
        return self.get_field_text(LoginPageLocators.ORDER_HISTORY_NUMBER)

    @allure.step('Клик по кнопке Выход')
    def click_exit_btn(self):
        if Constants.browser_name == 'chrome':
            self.click_to_element(LoginPageLocators.EXIT_BUTTON)
            WebDriverWait(self.driver, 3)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.EXIT_BUTTON)

    @allure.step('Метод проверки успешности выхода из ЛК')
    def check_exit_success(self):
        return self.get_field_text(LoginPageLocators.ENTER_TEXT)

    @allure.step('Клик на глаз поля пароль')
    def click_(self):
        self.click_to_element(LoginPageLocators.PASS_EYE)
