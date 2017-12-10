from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import platform

plat = platform.system()
MY_ID = 'anylee77@naver.com'

lin_driver = './driver/chromedriver'
win_driver = './driver/chromedriver.exe'
driver_path = lin_driver if plat=='Linux' else win_driver

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
ac = ActionChains(driver)

win_pass_path = 'D:\\password.txt'
lin_pass_path = '/home/ej/older/password'
pass_path = lin_pass_path if plat=='Linux' else win_pass_path

win_result_path = 'D:\\codingplace\\fb_crawling\\TODOL'
lin_result_path = '/home/ej/codingplace/fb_crawling/TODOL'
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
    my_btn = driver.find_element_by_class_name('_1vp5')
    ac.reset_actions()
    ac.move_to_element_with_offset(my_btn,-50,0)
    ac.click()
    ac.perform()
    time.sleep(0.5)

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

    time.sleep(1)

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

def writeFile(TEXT, LINKS, IMG_LINKS, COMMENTS,link):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d %H-%M-%S')
    # 윈도우에서 파일이름에 ':' 넣지 말 것

    print('File Writing Started..')

    global file_index
    file_name = str(file_index)+') '+nowDate
    f_path = result_path+'/'+file_name
    print('\t'+f_path)

    try:
        # encoding을 UTF-8로 한 이유
        # 페북에서만 쓰이는 텍스트 특수문자가 파이썬 디폴트 코덱으로는 인식안됨
        with open(f_path+'.txt','w',encoding='UTF-8') as fp:
            try:
                if link:
                    fp.write('\t'+'** 게시물 URL'+'\n')
                    fp.write(link+'\n\n\n')
            except Exception as e:
                print(e)
                print('Error while writing 게시물 URL')
                pass

            try:
                if TEXT:
                    fp.write('\t'+'** 본문'+'\n')
                    fp.write(TEXT+'\n\n\n')
            except Exception as e:
                print(e)
                print('Error while writing 본문')
                pass

            try:
                if LINKS:
                    fp.write('\t'+'** 링크'+'\n')
                    for LINK in LINKS:
                        fp.write(LINK+'\n')
                    fp.write('\n\n')
            except Exception as e:
                print(e)
                print('Error while writing 링크')
                pass

            try:
                if IMG_LINKS:
                    fp.write('\t'+'** 이미지 링크'+'\n')
                    for IMG_LINK in IMG_LINKS:
                        fp.write(IMG_LINK+'\n')
                    fp.write('\n\n')
            except Exception as e:
                print(e)
                print('Error while writing 이미지 링크')
                pass

            try:
                if COMMENTS:
                    fp.write('\t'+'** 댓글'+'\n')
                    for COMMENT in COMMENTS:
                        fp.write(COMMENT+'\n')
                    fp.write('\n\n')
            except Exception as e:
                print(e)
                print('Error while writing 댓글')
                pass

            updateIndex()
    except Exception as e:
        print(e)
        print('Error while opening File ! '+link)

    print('File Writing Done !\n\n')

def checkScope():
    # To crawl only non-public post
    index_count=0

    fols = driver.find_elements_by_class_name('_fol')

    for fol in fols:
        xe = fol.find_element_by_class_name('_-xe')
        scope_icon = xe.find_element_by_class_name('img')
        scope_value = scope_icon.get_attribute('class').split()[0]

        if scope_value == '_21or':
            print('\there !')
            index_count += 1

    return index_count


def collectData():
    board = driver.find_element_by_class_name('_1dwg')

    # 텍스트가 있으면 긁어옴
    try:
        TEXT = board.text
    except NoSuchElementException:
        print('\t\t** No text')
        pass

    # 게시물 밑에 링크 칸이 있으면 그 URL을 긁어옴
    try:
        LINKS = []
        link_area = driver.find_element_by_class_name('_3x-2')
        links = link_area.find_elements_by_tag_name('a')

        for each_link in links:
            LINKS.append(each_link.get_attribute('href'))

    except NoSuchElementException:
        print('\t\t** No Link')
        pass

    # 이미지가 있으면 그 링크를 가져옴
    try:
        # img_area = board.find_element_by_class_name('_3x-2')
        # img_links = img_area.find_elements_by_tag_name('a')
        IMG_LINKS = []
        img_area = board.find_element_by_class_name('_6m5')
        img_links = img_area.find_elements_by_class_name('img')

        for img_link in img_links:
            IMG_LINKS.append(img_link.get_attribute('src'))

    except NoSuchElementException:
        print('\t\t** No Image')
        pass

    # 댓글이 있으면 댓글을 가져옴
    try:
        # Before crawling whole comments,
        # Click 달린 댓글 더보기, 댓글 더보기
        more_reply_tags = driver.find_elements_by_class_name('UFIReplySocialSentenceLinkText')
        more_content_tags = driver.find_elements_by_class_name('fss')

        # board = driver.find_element_by_class_name('_1dwg')
        # height = board.value_of_css_property('height')
        # move_to_reply_height = int(height[:len(height)-2]) + 25 + 110
        #                             # 게시물과 맨 위 사이의 거리 25, 게시물과 댓글들과의 거리 110
        # driver.execute_script('window.scrollTo(0,%d);' % ( move_to_reply_height ))
        # time.sleep(0.5)

        for each in more_reply_tags:
            ac.reset_actions()
            ac.move_to_element(each)
            ac.click()
            ac.perform()
            time.sleep(0.3)
        time.sleep(0.5)

        for each in more_content_tags:
            ac.reset_actions()
            ac.move_to_element(each)
            ac.click()
            ac.perform()
            time.sleep(0.3)

        comments = driver.find_elements_by_class_name('UFICommentActorAndBody')
        COMMENTS = []

        for comment in comments:
            comment_actor = comment.find_element_by_class_name(' UFICommentActorName')
            comment_body = comment.find_element_by_class_name('UFICommentBody')
            comment_content = '[%s]\n\t%s\n' % (comment_actor.text, comment_body.text.replace('\n','\n\t'))
            # print(comment_content)
            COMMENTS.append(comment_content)

    except NoSuchElementException:
        print('\t\t** No comment')
        pass

    return TEXT, LINKS, IMG_LINKS, COMMENTS


def collectAndStore():
    clickSwh()
    time.sleep(0.5)

    # global post_index
    # print('here')
    # post_index = checkScope()
    # print('done')

    # I'm at my page
    boards = driver.find_elements_by_class_name('_1dwg')
    post_index = 0

    print(len(boards))

    for board in boards:
        fol = board.find_element_by_class_name('_fol')
        xe = fol.find_element_by_class_name('_-xe')
        scope_icon = xe.find_element_by_class_name('img')
        scope_value = scope_icon.get_attribute('class').split()[0]

        if scope_value == '_21or':
            post_index += 1
        elif scope_value == '_k_e':
            break

    input(post_index)

    board = boards[post_index]
    height = board.value_of_css_property('height')
    time.sleep(0.5)

    # 공유한 게시물은
    # 게시물, 사진, 링크, 동영상 으로 나뉨
    tags = ['게시물','링크','사진','동영상']
    # 가능한 경우의 수
    # 게시물 2개
    # 게시물 1개
    # 게시물 1개, 링크 1개
    # 사진 1개
    # 동영상 1개

    total_links = []
    for tag in tags:
        total_links += [each.get_attribute('href') for each in board.find_elements_by_link_text(tag)]

    # 게시물 1개, 링크 1개인 경우
    if len(total_links)==2 and total_links[0]==total_links[1]:
        total_links.pop()

    print('total links are ' +str(total_links))

    # 내가 작성한 게시물인데 비공개 = 공유하지 않은 게시물인 경우
    if len(total_links)==0:
        TEXT, LINKS, IMG_LINKS, COMMENTS = collectData()

        hidePost(board)
        driver.execute_script('window.scrollTo(0,%d);' % (  int(height[:len(height)-2]) ))
        time.sleep(1)

        writeFile(TEXT,LINKS,IMG_LINKS,COMMENTS,'My Post')


    # 내가 공유한 게시물인데 비공개
    else:
        hidePost(board)
        driver.execute_script('window.scrollTo(0,%d);' % (  int(height[:len(height)-2]) ))
        time.sleep(1)

        # 공유한 게시물의 링크로 가서 데이터를 긁어옴
        for link in total_links:
            print('Crawling Started !')
            print('\t'+link)
            driver.get(link)
            time.sleep(0.5)
            clickSwh()
            time.sleep(0.5)
            TEXT, LINKS, IMG_LINKS, COMMENTS = collectData()
            print('Crawling done !\n')

            # 긁어온 데이터를 텍스트 파일로 저장
            writeFile(TEXT,LINKS,IMG_LINKS,COMMENTS,link)

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
    collectAndStore()
    myPage()

try:
    loginFb()

    myPage()

    # file_name_index
    file_index = getIndex()
    # board_post_index
    board_index=0

    # 오토 크롤링
    for i in range(20):
        autoWork()
    # autoWork()



except Exception as e:
    print(e)

finally:
    driver.quit()
