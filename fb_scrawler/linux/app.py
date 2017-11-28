from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')
    with open('/home/ej/older/password','r') as file:
        PW.send_keys(file.read())
        # PW.send_keys(Keys.RETURN)

    time.sleep(1)

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
