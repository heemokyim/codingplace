from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import platform

plat = platform.system()
MY_ID = 'anylee77@naver.com'

lin_driver = './linux/chromedriver'
win_driver = './window/chromedriver.exe'

driver_path = lin_driver if plat=='Linux' else win_driver

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
ac = ActionChains(driver)


win_pass_path = 'D:\\password.txt'
lin_pass_path = '/home/ej/older/password'
pass_path = lin_pass_path if plat=='Linux' else win_pass_path

win_result_path = 'D:\\codingplace\\TODOL'
lin_result_path = '/home/ej/codingplace/TODOL'
result_path = lin_result_path if plat=='Linux' else win_result_path


def loginFb():
    driver.get('https://www.facebook.com')

    ID = driver.find_element_by_name('email')
    PW = driver.find_element_by_name('pass')

    ID.send_keys(MY_ID)
    with open(pass_path,'r') as file:
        PW.send_keys(file.read())
        if plat == 'Windows':
            PW.send_keys(Keys.RETURN)

def clickSwh():
    # click somewhere
    ac.reset_actions()
    ac.move_by_offset(0,50)
    ac.click()
    ac.perform()

def myPage():
    clickSwh()
    my_btn = driver.find_element_by_class_name('_1vp5')
    my_btn.click()
    time.sleep(0.2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(0.2)
    driver.execute_script('window.scrollTo(0,0);')

def clickEtc(board):
    clickSwh()
    # click etc of Post
    etc_btn = board.find_element_by_class_name('_4xev')
    # ac.reset_actions()
    # ac.move_to_element(etc_btn)
    # ac.click()
    # ac.perform()
    etc_btn.click()

def hidePost(board):
    clickSwh()

    # 게시물 설정 클릭
    clickEtc(board)

    time.sleep(0.5)

    # 타임라인 숨기기 클릭
    etc1 = driver.find_element_by_class_name('uiContextualLayer')
    etc2 = etc1.find_element_by_class_name('_54nq')
    etc3 = etc2.find_element_by_class_name('_54ng')
    etc4 = etc3.find_element_by_class_name('_54nf')
    # etc_btns = etc4.find_elements_by_class_name('_54ni')

    hideFromTimeline_btn = etc4.find_element_by_link_text('타임라인에서 숨기기')
    hideFromTimeline_btn.click()

    time.sleep(1)

    # 숨기기 확인
    popUp = driver.find_element_by_class_name('_4t2a')
    footer = popUp.find_element_by_class_name('_5lnf')
    hide = footer.find_element_by_class_name('layerConfirm')
    hide.click()

def writeFile(TEXT, IMG_LINKS, COMMENTS,link):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d %H:%M:%S')

    print('\t'+'File Writing Started..')

    global file_index
    file_name = str(file_index)+') '+nowDate
    f_path = result_path+'/'+file_name
    print(f_path)

    try:
        with open(f_path+'.txt','w') as fp:
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

def checkScope():
    index_count=0

    # To crawl only non-public post
    fols = driver.find_elements_by_class_name('_fol')

    for fol in fols:
        xe = fol.find_element_by_class_name('_-xe')
        scope_icon = xe.find_element_by_class_name('img')
        scope_value = scope_icon.get_attribute('class').split()[0]

        if scope_value == '_21or':
            print('\there !')
            index_count += 1

    return index_count


def colletData():
    clickSwh()

    global post_index

    # print('here')

    post_index = checkScope()

    # print('done')

    time.sleep(1)

    # I'm at my page
    boards = driver.find_elements_by_class_name('_1dwg')
    board = boards[post_index]

    # 공유한 게시물은
    # 게시물, 사진, 링크, 동영상 으로 나뉨
    post_links = [post.get_attribute('href') for post in board.find_elements_by_link_text('게시물')]
    pic_links = [picture.get_atrribute('href') for picture in board.find_elements_by_link_text('사진')]
    link_links = [link.get_attribute('href') for link in board.find_elements_by_link_text('링크')]
    video_links = [video.get_atrribute('href') for video in board.find_elements_by_link_text('동영상')]

    total_links = post_links + pic_links + link_links + video_links
    print('total links are ' +str(total_links))

    hidePost(board)

    # What to put in file?
    # 0. Link of post
    # 1. Img link if there is
    # 2. Text
    # 3. Any Comments
    # 4. User content (퍼간사람이 쓴 글)

    print('Crawling Started !')

    for link in total_links:
        print('\t'+link)
        driver.get(link)
        time.sleep(1)

        clickSwh()

        board = driver.find_element_by_class_name('_1dwg')
        # Text of post
        TEXT = board.text

        tmp = driver.find_element_by_class_name('_3x-2')
        tmp2 = tmp.find_element_by_tag_name('a')
        print(tmp2.get_attribute('href'))

        input()

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
            # Before crawling whole comments,
            # Click 더보기, 댓글
            more_reply_tags = driver.find_elements_by_class_name('UFIReplySocialSentenceLinkText')
            more_content_tags = driver.find_elements_by_class_name('fss')

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(0.5)

            for each in more_reply_tags:
                each.click()
                time.sleep(0.1)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(0.5)

            for each in more_content_tags:
                each.click()
                time.sleep(0.1)

            comments = driver.find_elements_by_class_name('UFICommentActorAndBody')
            COMMENTS = []

            for comment in comments:
                comment_actor = comment.find_element_by_class_name(' UFICommentActorName')
                comment_body = comment.find_element_by_class_name('UFICommentBody')
                body_content = comment_body.text
                body_content = body_content.replace('\n','\n\t')
                comment_content = '[%s]\n\t%s\n' % (comment_actor.text, body_content)
                # print(comment_content)
                COMMENTS.append(comment_content)

        except NoSuchElementException:
            pass

        print('\t'+'Done !')

        writeFile(TEXT,IMG_LINKS,COMMENTS,link)

    post_index=0

def getIndex():
    try:
        with open(result_path +'/index','r') as fp:
            file_index = fp.read()
            return int(file_index)
    except:
        print('Error while opening index')

def updateIndex():

    try:
        with open(result_path +'/index','w') as fp:
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
    myPage()

    # file_name_index
    file_index = getIndex()
    # board_post_index
    board_index=0

    # 오토 크롤링
    for i in range(4):
        autoWork()

    # time.sleep(1)

    # -------------------------------------------------

    # 스크롤 내리기
    # driver.execute_script('window.scrollTo(0,50)')

    # input()

except Exception as e:
    print(e)

finally:
    driver.quit()
