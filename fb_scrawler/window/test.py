from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
ac = ActionChains(driver)

HOW_MANY = 3

def goAndScrawl():
    try:
        board= driver.find_element_by_class_name('_1dwg')
        board_content = board.find_element_by_class_name('_5r69')
        deliver = board_content.find_element_by_class_name('fcg')
        a_tags = deliver.find_elements_by_tag_name('a')

        source_post = a_tags[2]
        source_post.click()

        board= driver.find_element_by_class_name('_1dwg')
        link_tag = driver.find_element_by_class_name('_52c6')
        print(board.text)
        print(link_tag.get_attribute('href'))

        myPage()

    except NoSuchElementException:
        pass

def plainScrawl():
    # 더보기 버튼이 있으면 눌러서 긁어오고 없으면 걍 긁어와라
    try:
        board= driver.find_element_by_class_name('_1dwg')

        see_more = driver.find_element_by_class_name('see_more_link_inner')
        ac.reset_actions()
        ac.move_to_element(see_more)
        ac.click()
        ac.perform()
    except NoSuchElementException:
        pass

    finally:
        board_content = board.find_element_by_class_name('_5r69')
        print(board_content.text)


    # 글 밑에 링크를 걸어놨으면 그것도 긁어와라
    try:
        tmp = board_content.find_element_by_class_name('_6ks')
        tmp_link = tmp.find_element_by_tag_name('a')
        print(tmp_link.text)
        print(tmp_link.get_attribute('href'))
    except NoSuchElementException:
        pass

def loginFb():
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')

    with open('D:\password.txt','r') as file:
        PW.send_keys(file.read())
        PW.send_keys(Keys.RETURN)

def clickSwh():
    # click somewhere
    ac.reset_actions()
    ac.move_by_offset(50,50)
    ac.click()
    ac.perform()


def myPage():
    my_btn = driver.find_element_by_link_text('이재웅')
    my_btn.click()

def clickEtc():
    # click etc of Post
    etc_btn = driver.find_element_by_class_name('_4xev')
    ac.reset_actions()
    ac.move_to_element(etc_btn)
    ac.click()
    ac.perform()

def hidePost():
    # 게시물 설정 클릭
    clickEtc()

    time.sleep(1)

    # 타임라인 숨기기 클릭
    etc1 = driver.find_element_by_class_name('uiContextualLayer')
    etc2 = etc1.find_element_by_class_name('_54nq')
    etc3 = etc2.find_element_by_class_name('_54ng')
    etc4 = etc3.find_element_by_class_name('_54nf')
    etc_btns = etc4.find_elements_by_class_name('_54ni')
    hideFromTimeline_btn = etc_btns[5]
    hideFromTimeline_btn.click()

    time.sleep(1)

    # 숨기기 확인
    popUp = driver.find_element_by_class_name('_4t2a')
    footer = popUp.find_element_by_class_name('_5lnf')
    hide = footer.find_element_by_class_name('layerConfirm')
    hide.click()

try:
    # -------------------------------------------------
    # 로그인
    loginFb()

    # -------------------------------------------------
    # 내 타임라인 들어가기
    clickSwh()

    myPage()

    # -------------------------------------------------
    # 게시물 내용 읽기
    time.sleep(0.2)

    # 내가 공유한 게시물의 소유주가 그 게시물을
    # 1. 딴데서 공유했다 => 거기로 가서 긁어와라
    goAndScrawl()

    # 2. 본인이 직접 작성했다 => 있는걸 그대로 긁어와라
    plainScrawl()

    # -------------------------------------------------
    # 게시물 타임라인에서 숨기기
    # hidePost()

    time.sleep(1)

    # 스크롤 내리기
    driver.execute_script('window.scrollTo(0,50)')

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
