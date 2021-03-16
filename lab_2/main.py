from time import sleep

from selenium import webdriver

from test_classes import Reddit

if __name__ == '__main__':
    # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    # driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
    # driver = webdriver.Opera(executable_path='/usr/local/bin/operadriver')

    Reddit(webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')).test_wrong_username()
    Reddit(webdriver.Opera(executable_path='/usr/local/bin/operadriver')).test_too_long_username()
    input()
    # driver.close()
    # NineGag(driver).test_wrong_email_login()
