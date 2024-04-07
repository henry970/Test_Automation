from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Automation.locatorsPage.locators import (LoginPageLocators, AddCustomerPageLocators, NewCustomerPageLocators,
                                                   LogOutPageLocators)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                             (LoginPageLocators.EMAIL_INPUT)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                             (LoginPageLocators.PASSWORD_INPUT)).send_keys(password)

    def click_remember_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             (LoginPageLocators.REMEMBER_BUTTON)).click()

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             (LoginPageLocators.LOGIN_BUTTON)).click()


class AddCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_customer_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             (AddCustomerPageLocators.ADD_CUSTOMER_BUTTON)).click()


class NewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             (NewCustomerPageLocators.EMAIL_ADDRESS_INPUT)).send_keys(email)

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             (NewCustomerPageLocators.FIRST_NAME_INPUT)).send_keys(first_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             (NewCustomerPageLocators.LAST_NAME_INPUT)).send_keys(last_name)

    def enter_city(self, city):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
                                             (NewCustomerPageLocators.CITY_INPUT)).send_keys(city)

    def select_gender_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             (NewCustomerPageLocators.SELECT_GENDER)).click()

    def add_to_promoter(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             (NewCustomerPageLocators.ADD_TO_PROMOTER_lIST)).click()

    def submit_button(self):
        try:
            # Wait for element to be visible
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(NewCustomerPageLocators.SUBMIT_BUTTON))

            # Scroll into view if needed
            submit_button = self.driver.find_element(*NewCustomerPageLocators.SUBMIT_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

            # Click on the element
            submit_button.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            print("Error:", e)
            # Implement retry mechanism if needed


class LogOutPage:
    def __init__(self, driver):
        self.driver = driver

    def select_login_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
                                             (LogOutPageLocators.LOGOUT_BUTTON)).click()
