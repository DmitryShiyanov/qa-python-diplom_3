import allure
from Practikum_UI.page_objects.main_page import MainPage


@allure.title('Тесты на проверку главное страницы')
class TestMainPage:


    @allure.step('Проверяем редирект по ссылке на Конструктор')
    def test_click_btn_constructor_success(self, driver, login_page):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert 'Соберите бургер' == main_page.check_burger_text_success()

    @allure.step('Проверяем редирект по ссылке на Ленту заказов')
    def test_click_btn_order_feed_success(self, driver, main_page):
        main_page.click_order_feed_button()
        assert 'Лента заказов' == main_page.check_order_text_success()

    @allure.step('Проверяем всплывающее окно Box')
    def test_click_on_ingredient_success(self, driver, main_page):
        main_page.click_bun_image()
        assert 'contentBox' in main_page.check_window_attribute()

    @allure.step('Проверяем закрытие всплывающего окна')
    def test_click_on_ingredient_and_escape_success(self, driver, main_page):
        main_page.click_bun_image()
        main_page.click_escape_button()
        main_page.wait_method()
        assert 'modal_opened' not in main_page.wait_until_element_closed() , f'тот самый  attr {main_page.wait_method_until_elem_closed()}'

    @allure.step('Проверяем изменение каунтера ингредиентов')
    def test_drug_and_drop_success(self, driver, main_page):
        main_page.create_order()
        assert len(main_page.get_text_from_counter()) > 0

    @allure.step('Проверяем возможность сделать заказ залогиненному пользователю')
    def test_login_and_get_order_success(self, driver, login_page):
        main_page = MainPage(driver)
        login_page.login_step()
        login_page.wait_layout()
        main_page.create_order()
        login_page.wait_layout()
        main_page.click_on_order_btn()
        assert 'Ваш заказ начали готовить' == main_page.get_text_from_order_text()
