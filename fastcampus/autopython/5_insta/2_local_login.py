from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome('../4_crawling/chromedriver')
driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    btn = driver.find_element_by_link_text('로그인')
    # 인스타 로그인 버튼에 마우스 올려놓고 텍스트 확인
    btn.click()

    inputs = driver.find_elements_by_class_name('_ph6vk')

    # Why is 'inputs' list?
    # Duplicated class name _ph6vk
    # Refer to Instagram Login Page source

    ID = inputs[0]
    # elem = driver.find_element_by_name('username')
    PW = inputs[1]
    # elem = driver.find_element_by_name('password')

    ID.send_keys('hihihihi')
    # ID.send_keys(Keys.RETURN)

    PW.send_keys('13241234')
    PW.send_keys(Keys.RETURN)

    # 2초 대기
    time.sleep(2)

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
