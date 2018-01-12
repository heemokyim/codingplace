from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
