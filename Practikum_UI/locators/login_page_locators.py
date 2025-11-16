from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка войти в аккаунт на главной странице
    LOGIN_ACCOUNT_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"
    # Кнопка история заказов
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[contains(@class, 'Account_link') and text()='История заказов']"
    # Локатор номера заказа
    ORDER_HISTORY_NUMBER = By.XPATH, "//p[contains(@class, 'text_type_digits-default') and text()='#0282000']"
    # Кнопка на личный кабинет
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"
    ACCOUNT_TEXT = By.XPATH, "//p[contains(@class, 'Account_text') and text()='В этом разделе вы можете изменить свои персональные данные']"
    # Кнопка поля почта/логин при регистрации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    # Кнопка поля пароль при регистрации
    PASSWORD_FIELD = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']"
    PASSWORD_FIELD_2 = By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Пароль']"
    # Кнопка восстановления пароля
    PASSWORD_RECOVERY_BTN = By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']"
    # Кнопка поля с кодом
    RECOVERY_CODE_PLACE = By.XPATH, "//label[text()='Введите код из письма']/following-sibling::input[@name='name']"
    RECOVERY_CODE_PLACE_2 = By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Введите код из письма']"
    # Кнопка Сохранить
    SAVE_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Сохранить']"
    # Кнопка глаз
    PASS_EYE = By.XPATH, "//div[@class='input__icon input__icon-action']"
    # Кнопка Восстановить
    RECOVERY_BTN = By.XPATH, "//button[contains(@class, 'button_button_size_medium') and text()='Восстановить']"
    # Поле текст с новым паролем
    NEW_PASSWORD_BTN = By.XPATH, "//input[@class = 'text input__textfield' and @name='Введите новый пароль']"
    # Поле пароль
    DIV_CLASS = By.XPATH, '//label[text()="Пароль"]/parent::*'
    NEW_PASSWORD_BTN_2 = By.XPATH, "//input[@type='password']"
    # Локатор перекрывающего слоя FF
    OVERLAY_ELEM = By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']"
    # Кнопка выход на странице личного кабинета
    EXIT_BUTTON = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive') and text()='Выход']"
    # Текст Вход над страницей входа
    ENTER_TEXT = By.XPATH, "//h2[contains(text(), 'Вход')]"
    #LOCATOR_INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following::input'
    #LOCATOR_INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following::input'
