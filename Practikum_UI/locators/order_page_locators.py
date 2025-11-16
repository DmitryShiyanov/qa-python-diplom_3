from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Булка краторная
    BUN_CRATOR = By.XPATH, "//p[text()='Краторная булка N-200i']"
    # Булка Флюоресцентная
    BUN_FLUR = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    # Текст локатор Лента заказов
    ORDER_FEED_TEXT = By.XPATH, "//h1[contains(@class, 'text text_type_main-large mt-10 mb-5') and text()='Лента заказов']"
    # Локатор о заказе
    ORDER_TEXT_BEGIN = By.CSS_SELECTOR, ".text_type_main-small mb-2"
    # Локатор номера заказа
    ORDER_NUMBER = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    # Локатор всплывающего окна заказа
    ORDER_BOX_LOCATOR = By.XPATH, "//section[2]"
    # Локатор списка UL
    LIST_ORDER_LOCATOR = By.XPATH,   "//li[contains(@class, 'OrderHistory_listItem__2x95r')]/parent::*"
    # Локатор первого заказа
    FIRST_ORDER_LINK = By.XPATH, "//ul/li[3]/a"
    # Локатор Выполнено за все время
    ALL_TIME_ORDERS = By.XPATH, '//p[text()="Выполнено за все время:"]/following::p'
    # Локатор Выполнено за сегодня
    TODAY_ORDERS = By.XPATH, "//p[contains(@class, 'text text_type_main-medium') and text()='Выполнено за сегодня:']/following::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    # Локатор список заказов
    LIST_ORDERS = By.XPATH, "//p[@class='text text_type_digits-default']"
    # Локатор заказа из поля "в работе"
    ORDERS_IN_WORK = By.XPATH, "//ul[@class ='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/child::*"
