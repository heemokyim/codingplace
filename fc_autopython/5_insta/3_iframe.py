from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome('./chromedriver',chrome_options=options)

try:
    driver.get('http://cafe.naver.com/joonggonara')

    input_text = driver.find_element_by_name('query')
    input_text.send_keys('자전거')
    input_text.send_keys(Keys.RETURN)

    # iframe 태그를 찾음
    iframe = driver.find_element_by_id('cafe_main')
    # iframe 태그 안으로 이동
    driver.switch_to_frame(iframe)

    curr_page = 1
    while True:
        form = driver.find_element_by_name('ArticleList')

        rows = form.find_elements_by_xpath('./table/tbody/tr')

        for row in rows:
            try:
                a_tag = row.find_element_by_tag_name('a')
                print(a_tag.text)
                print(a_tag.get_attribute('href'))
            except:
                continue

        curr_page += 1
        page_table = driver.find_element_by_class_name('Nnavi')

        if(curr_page-1)%10 ==0:
            page_link = page_table.find_element_by_partial_link_text('다음')
        else:
            page_link = page_table.find_element_by_link_text(str(curr_page))
        page_link.click()

        time.sleep(1)

        if curr_page>=12:
            break

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
