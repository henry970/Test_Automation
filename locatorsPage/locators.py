import time

from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "email-id")
    PASSWORD_INPUT = (By.ID, "password")
    REMEMBER_BUTTON = (By.ID, "remember")
    LOGIN_BUTTON = (By.ID, "submit-id")


class AddCustomerPageLocators:
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "#new-customer")


class NewCustomerPageLocators:
    EMAIL_ADDRESS_INPUT = (By.ID, "EmailAddress")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    CITY_INPUT = (By.ID, "City")
    SELECT_GENDER = (By.CSS_SELECTOR, "#loginform > div > div > div > div > form > div:nth-child(6) > input[type=radio]:nth-child(2)")
    ADD_TO_PROMOTER_lIST = (By.CSS_SELECTOR, "#loginform > div > div > div > div > form > div:nth-child(7) > input[type=checkbox]")
    time.sleep(23)
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#loginform > div > div > div > div > form > button')

class LogOutPageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'body > nav > ul > li > a')
