import allure


@allure.title('Тесты на проверку формы логина и личного кабинета')
class TestLoginPage:


    @allure.step('Проверяем переход на страницу восстановления пароля')
    def test_press_recovery_btn_true(self, driver, login_page):
        login_page.press_password_recovery()
        assert 'Восстановить' in login_page.check_recovery_text_field()

    @allure.step('Проверяем работу кнопки Восстановить')
    def test_enter_mail_field(self, driver, login_page):
        login_page.press_password_recovery()
        login_page.wait_layout()
        login_page.enter_mail_method()
        assert 'Введите код из письма' in login_page.check_password_relay_status()

    @allure.step('клик по кнопке показать/скрыть пароль делает поле активным')
    def test_for_check_light_field(self, driver, login_page):
        login_page.press_password_recovery()
        login_page.wait_layout()
        login_page.enter_mail_method()
        login_page.wait_layout()
        login_page.wait_layout()
        login_page.click_()
        assert 'input_status_active' in login_page.check_password_field_on_lighting()

    @allure.step('Проверяем переход в личный кабинет')
    def test_login_method_success(self, driver, login_page):
        login_page.login_step()
        login_page.wait_layout()
        login_page.click_lk_button()
        assert 'В этом разделе вы можете изменить свои персональные данные' in login_page.check_login_success()

    @allure.step('Проверяем переход в раздел истории заказов')
    def test_order_history_view(self, driver, login_page):
        login_page.login_step()
        login_page.wait_layout()
        login_page.click_lk_button()
        login_page.click_order_button()
        assert '#0282000' == login_page.check_order_number()

    @allure.step('Проверяем выход из аккаунта')
    def test_exit_from_lk_success(self, driver, login_page):
        login_page.login_step()
        login_page.wait_layout()
        login_page.click_lk_button()
        login_page.click_exit_btn()
        assert 'Вход' == login_page.check_exit_success()
