from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWebsite:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


class NineGag(TestWebsite):
    URL = 'https://9gag.com'

    def website_login(self, email, password):
        self.driver.get(self.URL)
        login_button = self.driver.find_element_by_class_name('btn-mute')
        login_button.click()

        email_input = self.driver.find_element_by_id('login-email-name')
        password_input = self.driver.find_element_by_id('login-email-password')

        email_input.send_keys(email)
        password_input.send_keys(password)

        login_button_2 = self.driver.find_element_by_css_selector('#login-email .btn')
        login_button_2.click()

    def test_wrong_password(self):
        self.website_login('jannos1999@wp.pl', 'password2222')

    def test_wrong_email_login(self):
        self.website_login('aslkjdflka', 'password1111')


class Reddit(TestWebsite):
    URL = 'https://www.reddit.com/'

    def fill_credentials(self, username, password):
        self.driver.get(self.URL)
        login_button_1 = self.driver.find_element_by_class_name('_3Wg53T10KuuPmyWOMWsY2F')
        login_button_1.click()

        self.driver.switch_to.frame(self.driver.find_element_by_class_name('_25r3t_lrPF3M6zD2YkWvZU'))

        self.driver.implicitly_wait(1000)
        username_input = self.driver.find_element_by_id('loginUsername')
        password_input = self.driver.find_element_by_id('loginPassword')

        username_input.send_keys(username)
        password_input.send_keys(password)

    def incorrect_username_or_password_showed(self, email, password):
        self.fill_credentials(email, password)
        login_button = self.driver.find_element_by_class_name('AnimatedForm__submitButton')
        login_button.click()

        desired_error_message = 'Incorrect username or password'
        error_showed_up = WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'AnimatedForm__errorMessage'),
            desired_error_message
        ))

        return error_showed_up

    def test_wrong_username(self):
        print(self.incorrect_username_or_password_showed('asdlkfjwerzxc', 'password'))

    def test_wrong_password(self):
        print(self.incorrect_username_or_password_showed('john', 'password'))

    def test_too_long_username(self):
        self.fill_credentials('012345678901234567890123456789', 'password')
        desired_error_message = 'Username must be between 3 and 20 characters'
        error_showed_up = WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'AnimatedForm__errorMessage'),
            desired_error_message
        ))

        print(error_showed_up, desired_error_message)
