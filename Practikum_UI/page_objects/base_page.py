import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@allure.title('Базовый класс')
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов с ожиданием')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Клик по элементу с ожиданием')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Метод заполнения поля')
    def add_text_in_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Метод изьятия текста с элемента')
    def get_field_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Метод скролл')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Метод распаковки локатора и форматирования')
    def format_locators(self, locator_1, number):
        method, locator = locator_1
        locator = locator.format(number)
        return (method, locator)

    @allure.step('Метод открытия URL')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Метод клика по элементу для FF')
    def click_to_element_for_firefox(self, locator):
        ActionChains(self.driver).move_by_offset(0, 0 ).click().perform()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Вэйт для Лэйаута')
    def wait_method_until_elem_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until_not(
                expected_conditions.visibility_of_element_located(
                    locator))
        except TimeoutException:
            pass

    @allure.step('Метод перетаскивания ингредиентов')
    def drag_and_drop_method_for_browser(self, locator_from, locator_to):
        elem_from=self.find_element_with_wait(locator_from)
        elem_to=self.find_element_with_wait(locator_to)
        self.driver.drag_and_drop(elem_from,elem_to)

    @allure.step('Вэйт метод для ожидания bcисчезновения номера заказа 9999')
    def wait_method_for_order(self, locator):
        try:
            WebDriverWait(self.driver, 5).until_not(
                expected_conditions.text_to_be_present_in_element(
                    locator, '9999'))
        except TimeoutException:
            pass

    @allure.step('Дроп элемента для FF')
    def drag_and_drop_element_firefox(self, element_locator, destination_locator):
        from_element = self.find_element_with_wait(element_locator)
        to_element = self.find_element_with_wait(destination_locator)
        self.driver.execute_script("""
                                    const [from_element, to_element] = arguments;
                                    const dataTransfer = new DataTransfer();
                                    // Эмуляция событий drag-and-drop
                                    ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {                
                                    const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });     
                                    (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                                    });  
                                    """, from_element, to_element)
