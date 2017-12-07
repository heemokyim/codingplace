from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
ac = ActionChains(driver)

HOW_MANY = 3

try:
    # -------------------------------------------------
    # 로그인
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')

    with open('D:\password.txt','r') as file:
        PW.send_keys(file.read())
        PW.send_keys(Keys.RETURN)

    # -------------------------------------------------
    # 내 타임라인 들어가기

    # time.sleep(0.5)

    ac.move_by_offset(50,50)
    ac.click()
    ac.perform()

    my_btn = driver.find_element_by_link_text('이재웅')
    my_btn.click()

    # -------------------------------------------------

    time.sleep(0.2)

    for i in range(0,HOW_MANY):

        # 게시물 내용 읽기
        board= driver.find_element_by_class_name('_1dwg')
        see_more = driver.find_element_by_class_name('see_more_link_inner')
        ac.reset_actions()
        ac.move_to_element(see_more)
        ac.click()
        ac.perform()
        board_content = board.find_element_by_class_name('_5pco')
        print(board_content.text)

        # 게시물 설정 클릭
        etc_btn = driver.find_element_by_class_name('_4xev')
        ac.reset_actions()
        ac.move_to_element(etc_btn)
        ac.click()
        ac.perform()

        # -------------------------------------------------

        time.sleep(1)

        # 타임라인에서 숨기기 클릭
        etc1 = driver.find_element_by_class_name('uiContextualLayer')
        etc2 = etc1.find_element_by_class_name('_54nq')
        etc3 = etc2.find_element_by_class_name('_54ng')
        etc4 = etc3.find_element_by_class_name('_54nf')
        etc_btns = etc4.find_elements_by_class_name('_54ni')
        hideFromTimeline_btn = etc_btns[5]
        hideFromTimeline_btn.click()

        # -------------------------------------------------

        time.sleep(1)

        # 숨기기 확인
        popUp = driver.find_element_by_class_name('_4t2a')
        footer = popUp.find_element_by_class_name('_5lnf')
        hide = footer.find_element_by_class_name('layerConfirm')
        hide.click()

        time.sleep(1)
    # -------------------------------------------------



    print('here')


    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
