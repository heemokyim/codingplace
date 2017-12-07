from selenium import webdriver
import platform

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

# 리눅스, 윈도우에 따라 방식이 조금 다름

def lin_loginFb():
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')
    with open('/home/ej/older/password','r') as file:
        PW.send_keys(file.read())

def win_loginFb():
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')
    with open('D:\password.txt','r') as file:
        PW.send_keys(file.read())
        PW.send_keys(Keys.RETURN)

plat = platform.system()
loginFunction = lin_loginFb if plat=='Linux' else win_loginFb
