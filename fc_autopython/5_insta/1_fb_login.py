from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome('../4_crawling/chromedriver')
driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    btns = driver.find_elements_by_class_name('_qv64e')
    btn = btns[0]
    btn.click()

    inputs = driver.find_elements_by_class_name('inputtext')

    ID, PW = inputs[0], inputs[1]

    ID.send_keys('anylee77@naver.com')
    f = open('/home/ej/older/password','r')
    PW.send_keys(f.read())
    # PW.send_keys(Keys.RETURN)

    time.sleep(2)

    # Searching tag
    # div 태그가 겹쳐져있기 때문에 바로 send_keys 할 수 없음
    elem = driver.find_element_by_class_name('_eduze')

    from selenium.webdriver.common.action_chains import ActionChains

    # tmp = driver.find_element_by_class_name('_avvq0')
    # tmp.send_keys('1234')
    # --------------------------------------------------
    ac = ActionChains(driver)
    ac.move_to_element(elem)
    ac.click()
    ac.click()
    ac.send_keys('#패스트캠퍼스')
    ac.perform()
    # perform에서 일괄적으로 수행

    time.sleep(2)

    # 기존에 있던 내용을 초기화
    ac.reset_actions()
    ac.move_by_offset(0,50)
    ac.click()
    ac.perform()

    time.sleep(2)

    elems = driver.find_elements_by_class_name('_cmdpi')
    # _cmdpi[0] = 인기 게시물, _cmdpi[1] = 최근 사진
    elem = elems[0]

    posts = elem.find_elements_by_class_name('_gvoze')
    ac = ActionChains(driver)

    for post in posts:
        ac.reset_actions()
        ac.move_to_element(post)
        ac.click()
        ac.perform()

        time.sleep(1)

        try:
            like_btn = driver.find_element_by_link_text('좋아요')
            like_btn.click()
        except:
            unlike_btn = driver.find_element_by_link_text('좋아요 취소')
            unlike_btn.click()

        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

    # 검사를 확인하기 위해 대기
    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
