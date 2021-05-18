from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class TestWebsite:
    def __init__(self, driver: WebDriver):
        self.driver = driver


class Allegro(TestWebsite):
    URL = 'https://allegro.pl'

    def print_button(self):
        self.driver.get(self.URL)
        user_button_xpath = '/html/body/div[3]/div[5]/header/div/nav/div[5]/button'
        login_page_button_xpath = '/html/body/div[3]/div[5]/header/div/nav/div[5]/div/div/div/div/div/a'

        login_input_xpath = '//*[@id="login"]'
        password_input_xpath = '//*[@id="password"]'
        login_button_xpath = '//*[@id="authForm"]/div/div/div[2]/button'
        login_error_msg_xpath = '//*[@id="login-form-submit-error"]'

        self._wait_for_privacy_button(20)
        self._click_xpath(user_button_xpath)
        self._click_xpath(login_page_button_xpath)

        self._wait_for_privacy_button(2)
        self._input_xpath(login_input_xpath, 'test@test.test')
        self._input_xpath(password_input_xpath, 'haslo')
        self._click_xpath(login_button_xpath)

        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, login_error_msg_xpath))
        )

        print('DONE')

    def _click_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def _input_xpath(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    def _wait_for_privacy_button(self, seconds=2):
        privacy_button_xpath = '/html/body/div[3]/div[9]/div/div/div/div/div[2]/div[2]/button[1]'

        privacy_button = WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable((By.XPATH, privacy_button_xpath))
        )
        privacy_button.click()
