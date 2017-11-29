from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
ac = ActionChains(driver)

def loginFb():
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys('anylee77@naver.com')
    with open('/home/ej/older/password','r') as file:
        PW.send_keys(file.read())

def clickSwh():
    # click somewhere
    ac.reset_actions()
    ac.move_by_offset(0,50)
    ac.click()
    ac.perform()


def myPage():
    clickSwh()
    my_btn = driver.find_element_by_link_text('이재웅')
    my_btn.click()

def clickEtc():
    clickSwh()
    # click etc of Post
    etc_btn = driver.find_element_by_class_name('_4xev')
    ac.reset_actions()
    ac.move_to_element(etc_btn)
    ac.click()
    ac.perform()

def hidePost():
    clickSwh()

    # 게시물 설정 클릭
    clickEtc()

    time.sleep(0.5)

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

def writeFile(TEXT, IMG_LINKS, COMMENTS,link):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d %H-%M')

    print('\t'+'File Writing Started..')

    global file_index
    file_name = str(file_index)+') '+nowDate

    try:
        with open('/home/ej/todol/'+file_name,'w') as fp:
            fp.write('\t'+'** 링크'+'\n')
            fp.write(link+'\n\n\n')

            fp.write('\t'+'** 본문'+'\n')
            fp.write(TEXT+'\n\n\n')

            fp.write('\t'+'** 이미지 링크'+'\n')
            for IMG_LINK in IMG_LINKS:
                fp.write(IMG_LINK+'\n')
            fp.write('\n\n')

            fp.write('\t'+'** 댓글'+'\n')
            for COMMENT in COMMENTS:
                fp.write(COMMENT+'\n')
            fp.write('\n\n')

            updateIndex()
    except:
        print('Error while File Writing '+link)

    print('File Writing Done !')

def colletData():
    clickSwh()
    # I'm at my page
    board = driver.find_element_by_class_name('_1dwg')
    links = [post.get_attribute('href') for post in board.find_elements_by_link_text('게시물')]

    hidePost()

    # What to put in file?
    # 0. Link of post
    # 1. Img link if there is
    # 2. Text
    # 3. Any Comments

    print('Crawling Started !')

    for link in links:
        print('\t'+link)
        driver.get(link)
        time.sleep(1)
        board = driver.find_element_by_class_name('_1dwg')
        # Text of post
        TEXT = board.text

        # Any link of post
        try:
            img_area = board.find_element_by_class_name('_3x-2')
            img_links = img_area.find_elements_by_tag_name('a')
            IMG_LINKS = []

            for img_link in img_links:
                IMG_LINKS.append(img_link.get_attribute('href'))

        except NoSuchElementException:
            pass

        # Any Comments on post
        try:
            comments = driver.find_elements_by_class_name('UFICommentActorAndBody')
            COMMENTS = []

            for comment in comments:
                COMMENTS.append(comment.text)

        except NoSuchElementException:
            pass

        print('\t'+'Done !')

        writeFile(TEXT,IMG_LINKS,COMMENTS,link)

def getIndex():
    try:
        with open('/home/ej/todol/index','r') as fp:
            file_index = fp.read()
            return int(file_index)
    except:
        print('Error while opening index')

def updateIndex():

    try:
        with open('/home/ej/todol/index','w') as fp:
            global file_index
            file_index+=1
            fp.write(str(file_index))

    except:
        print('Error while updating index')

def autoWork():
    colletData()
    myPage()

try:
    # -------------------------------------------------
    # 로그인
    loginFb()

    # -------------------------------------------------
    # 내 타임라인 들어가기
    clickSwh()

    myPage()

    file_index = getIndex()
    time.sleep(0.2)

    for i in range(2):
        autoWork()


    time.sleep(1)

    # 스크롤 내리기
    driver.execute_script('window.scrollTo(0,50)')

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
