from time import sleep

from selenium import webdriver

from test_classes import Allegro

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    # driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
    # driver = webdriver.Opera(executable_path='/usr/local/bin/operadriver')
    Allegro(driver).print_button()
    input()
    driver.close()
