import allure
from Practikum_UI.page_objects.main_page import MainPage
from Practikum_UI.page_objects.order_page import OrderPage


@allure.title('Тесты на проверку страницы "Ленты заказов"')
class TestOrderPage:


    @allure.step('клик на заказ и открытие окна с деталями')
    def test_order_content_box(self, driver, order_page):
        order_page.click_order()
        assert 'modal_opened' in order_page.check_content_box_active()

    @allure.step('Проверка счетчика "Заказы за все время"')
    def test_check_all_orders(self, driver, login_page):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        login_page.login_step()
        order_page.click_order_feed_button()
        old_number = order_page.get_text_old_order_number_for_all_days()
        order_page.main_page_step()
        login_page.wait_layout()
        main_page.create_order()
        main_page.click_on_order_btn()
        main_page.wait_order_method()
        new_order_number = main_page.get_text_from_order_number()
        assert new_order_number > old_number, f'{new_order_number} и {old_number}'

    @allure.step('Проверка счетчика "Заказы за сегодня"')
    def test_check_today_orders(self, driver, login_page):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        login_page.login_step()
        order_page.click_order_feed_button()
        old = order_page.get_old_order_number_for_today()
        order_page.main_page_step()
        login_page.wait_layout()
        main_page.create_order()
        main_page.click_on_order_btn()
        main_page.wait_order_method()
        login_page.wait_layout()
        main_page.click_escape_button()
        order_page.click_order_feed_button()
        new = order_page.get_old_order_number_for_today()
        assert old < new

    @allure.step('Проверка наличие заказа в "ленте заказов"')
    def test_history_of_orders(self, driver, login_page):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        login_page.login_step()
        main_page.create_order()
        main_page.click_on_order_btn()
        main_page.wait_order_method()
        actual_order = main_page.get_text_from_order_number()
        login_page.wait_layout()
        main_page.click_escape_button()
        order_page.click_order_feed_button()
        all_orders = order_page.find_all_orders()
        assert actual_order in all_orders

    @allure.step('Проверка счетчика заказов "В работе"')
    def test_order_in_work_place(self, driver, login_page):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        login_page.wait_layout()
        login_page.login_step()
        main_page.create_order()
        main_page.click_on_order_btn()
        main_page.wait_order_method()
        actual_order = main_page.get_text_from_order_number()
        login_page.wait_layout()
        main_page.click_escape_button()
        order_page.click_order_feed_button()
        order_page.wait_method_for_order_in_work(actual_order)
        order = order_page.get_order_number_from_work_place()
        main_page.wait_order_method()
        work_order = order.replace('0', '', 1)
        assert work_order == actual_order
