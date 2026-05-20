from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_INPUT_EMAIL = (By.ID, "id_login-username")
    LOGIN_INPUT_PASSWORD = (By.ID, "id_login-password")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_INPUT_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_INPUT_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_INPUT_PASSWORD2 = (By.ID, "id_registration-password2")
