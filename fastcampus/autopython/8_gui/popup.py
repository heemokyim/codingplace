from selenium import webdriver

# 드라이버를 사용하여 브라우저를 띄움
driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://www.kyobobook.co.kr/')
    windows = driver.window_handles
    driver.switch_to_window(windows[1])

    link = driver.find_element_by_tag_name('a')
    link.click()

    driver.switch_to_default_content()
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
