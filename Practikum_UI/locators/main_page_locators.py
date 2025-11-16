from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка поля с кодом
    RECOVERY_CODE_PLACE = By.XPATH, "//label[text()='Введите код из письма']/following-sibling::input[@name='name']"
    # Кнопка сохранить
    SAVE_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Сохранить']"
    # Кнопка регистрация
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Зарегистрироваться']"
    # Кнопка Войти на странице входа
    LOGIN_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Войти']"
    # Кнопка-ссылка на регистрацию
    REGISTRATION_HREF = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Зарегистрироваться']"
    # Кнопка войти через ссылку регистрации
    REGISTRATION_LOGIN_BUTTON = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Войти']"
    # Кнопка войти в аккаунт на главной странице
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"
    # Текст Вход над страницей входа
    ENTER_TEXT = By.XPATH, "//h2[contains(text(), 'Вход')]"
    # Текст ошибки при вводе некорректного пароля
    ERROR_TEXT = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
    # Кнопка Оформить заказ
    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"
    # Кнопка на личный кабинет
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"
    # Кнопка "профиль" в личном кабинете
    PROFILE_BUTTON = By.XPATH, "//a[contains(@class, 'Account_link') and text()='Профиль']"
    # Кнопка восстановления пароля
    PASSWORD_RECOVERY_BTN = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']"
    # Кнопка выход на странице личного кабинета
    EXIT_BUTTON = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive') and text()='Выход']"
    # Заголовок на главной странице "Соберите бургер"
    BURGER_TEXT = By.XPATH, "//h1[text()='Соберите бургер']"
    # Кнопка линк на Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    # Логотип Stellar Burgers
    STELLAR_BURGERS_BTN = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"
    # Кнопка булки
    BUN_BUTTON = By.XPATH, "//span[text()='Булки']/parent::div"
    # Кнопка соусы
    SAUCES_BUTTON = By.XPATH, "//span[text()='Соусы']/parent::div"
    # Кнопка начинки
    FILLINGS_BUTTON = By.XPATH, "//span[text()='Начинки']/parent::div"
    # Начинка мясо молюска
    MEAT_MOLUSKIN = By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']"
    # Соус SpicyX
    SAUCE_SPICYX = By.XPATH, "//p[text()='Соус Spicy-X']"
    # Булка краторная
    BUN_CRATOR = By.XPATH, "//p[text()='Краторная булка N-200i']"
    # Булка Флюоресцентная
    BUN_FLUR = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    # Текст локатор Лента заказов
    ORDER_FEED_TEXT = By.XPATH, "//h1[contains(@class, 'text text_type_main-large mt-10 mb-5') and text()='Лента заказов']"
    # Локатор о заказе
    ORDER_TEXT_BEGIN = By.XPATH, "//p[contains(@class, 'text_type_main-small') and text()='Ваш заказ начали готовить']"
    # Контент BOX
    CONTENT_BOX = By.XPATH, "//h2[starts-with(text(),'Детали') or contains(text(), 'ингредиента')]/parent::*"
    CONTENT_BOX_2 = By.XPATH, "//section[@class='Modal_modal__P3_V5']/ancestor::*"
    # Локатор крестика
    CONTENT_BOX_ESCAPE = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    # Поле для конструктора
    CONSTRUCTOR_FIELD = By.CSS_SELECTOR, ".constructor-element_pos_top"
    # Каунтер булки
    BUN_COUNTER = By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']"
    # Локатор номера заказа
    ORDER_NUMBER = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
