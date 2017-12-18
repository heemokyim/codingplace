from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import platform
import sys

plat = platform.system()
MY_ID = 'anylee77@naver.com'

lin_driver = './driver/chromedriver'
win_driver = './driver/chromedriver.exe'
driver_path = lin_driver if plat=='Linux' else win_driver

print(lin_driver)

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
    time.sleep(0.2)

def scrollDown():
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,0);')
    time.sleep(1)

def myPage():
    clickSwh()
    my_btn = driver.find_element_by_class_name('_1vp5')
    my_btn.click()

def clickEtc(board):
    clickSwh()
    # click etc of Post
    etc_btn = board.find_element_by_class_name('_4xev')
    ac.reset_actions()
    ac.move_to_element(etc_btn)
    ac.click()
    ac.perform()
    # etc_btn.click()

def hidePost(board):
    clickSwh()

    # 게시물 설정 클릭
    clickEtc(board)

    time.sleep(1)

    # 타임라인 숨기기 클릭
    # etc1 = driver.find_element_by_class_name('uiContextualLayer')
    # etc2 = etc1.find_element_by_class_name('_54nq')
    # etc3 = etc2.find_element_by_class_name('_54ng')
    # etc4 = etc3.find_element_by_class_name('_54nf')
    # etc_btns = etc4.find_elements_by_class_name('_54ni')

    hideFromTimeline_btn = driver.find_element_by_link_text('타임라인에서 숨기기')
    ac.reset_actions()
    ac.move_to_element(hideFromTimeline_btn)
    ac.click()
    ac.perform()
    # hideFromTimeline_btn.click()

    time.sleep(1)

    # 숨기기 확인
    popUp = driver.find_element_by_class_name('_4t2a')
    footer = popUp.find_element_by_class_name('_5lnf')
    hide = footer.find_element_by_class_name('layerConfirm')

    hide.click()

    time.sleep(1)

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

def writeException(link, error):

    print('******************* Post deprecated while crawling !')

    global file_index

    file_name = 'exception'
    f_path = result_path+'/'+file_name
    print('\t'+f_path)

    try:
        with open(f_path+'.txt','a',encoding='UTF-8') as fp:
            now = datetime.datetime.now()
            nowDate = now.strftime('[%Y-%m-%d %H:%M:%S]')
            fp.write('****************************************************************************\n')
            fp.write('%s\n%s\nfile_index = %s\n\n' % (nowDate, link, file_index))
            fp.write('%s\n\n' % (str(error)))

    except Exception as e:
        print(e)
        print('Error while writing Exception !')

    print('******************* Writing exception completed !')

def checkScope():
    # Deprecated function
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


def collectData(board=None):
    if board == None:
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

        comments = driver.find_elements_by_class_name('UFICommentContent')
        COMMENTS = []

        for comment in comments:
            comment_actor = comment.find_element_by_class_name(' UFICommentActorName')
            comment_body = comment.find_element_by_class_name('UFICommentBody')
            comment_img_link = ""

            # 댓글 중 이미지의 링크까지
            try:
                comment_img= comment.find_element_by_class_name('_2rn3')
                comment_img_link = comment_img.get_attribute('href')
            except NoSuchElementException as e:
                pass


            comment_content = '[%s]\n\t%s\n\t%s\n' % (comment_actor.text, comment_body.text.replace('\n','\n\t'),comment_img_link)
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
    global scroll_down_count
    global former_board_count

    for i in range(scroll_down_count):
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # time.sleep(2)
        scrollDown()

    # for i in range(100):
    #     ac.reset_actions()
    #     ac.send_keys(Keys.SPACE)
    #     ac.perform()
    #     time.sleep(0.1)

    time.sleep(1)

    boards = driver.find_elements_by_class_name('_1dwg')
    target_boards=[]

    print('the number of total boards are %d' % (len(boards)))

    for idx,board in enumerate(boards):
        # fol = board.find_element_by_class_name('_fol')
        # xe = fol.find_element_by_class_name('_-xe')
        try:
            xe = board.find_element_by_class_name('_-xe')
            scope_icon = xe.find_element_by_class_name('img')
            scope_value = scope_icon.get_attribute('class').split()[0]

            if scope_value == '_k_e':
                target_boards.append(board)
        except Exception as e:
            # print('When post is created from friend, tags are different')
            # print('In this case, just skip that post')
            pass

    print('the number of target boards are %d' % (len(target_boards)))

    print('former = %d' % (former_board_count))
    print('current = %d' % (len(boards)))

    # 만약 (이전 단계의 전체 게시물 개수)와 (현재 단계 전체 게시물 개수)가 같다면
    # 더이상 크롤링 할 비공개 게시물이 없음을 의미
    # 그럼 종료
    if former_board_count == len(boards) and len(target_boards) == 0:
        print('There is no post to crawl')
        print('Crawling Successfully completed')
        sys.exit()

    former_board_count = len(boards)

    if len(target_boards)==0:
        scroll_down_count += 1
        return

    if len(target_boards) < 5:
        scroll_down_count += 1

    total_links = []
    # 비공개 게시물을 대상으로만 크롤링
    for board in target_boards:
        tags = ['게시물','링크','사진','동영상']

        links=[]

        for tag in tags:
            links += [each.get_attribute('href') for each in board.find_elements_by_link_text(tag)]
            # 태그가 동영상이면 같은 url이 2개 들어가므로
            # 하나 빼야함
            if tag == '동영상' and len(links) == 2:
                links.pop()


        # 링크가 아예 없으면 내가 작성한 비공개 게시물
        if len(links)==0:
            try:
                TEXT, LINKS, IMG_LINKS, COMMENTS = collectData(board)
                writeFile(TEXT,LINKS,IMG_LINKS,COMMENTS,'My Post')
                height = board.value_of_css_property('height')
                driver.execute_script('window.scrollTo(0,%d);' % ( int(height[:len(height)-2]) ))

            except NoSuchElementException as e:
                print(e)
                pass

        # 게시물 1개, 링크 1개 URL이 있으면 둘 중 하나만 해도 됨
        if len(links)==2 and links[0] == links[1]:
            links.pop()

        print(links)

        total_links += links

        hidePost(board)

    print('target total links are ' +str(total_links))

    for link in total_links:
        print('Crawling Started !')
        print('\t'+link)
        driver.get(link)
        time.sleep(0.5)
        clickSwh()
        clickSwh()

        try:
            TEXT, LINKS, IMG_LINKS, COMMENTS = collectData()
            print('Crawling done !\n')

            # 긁어온 데이터를 텍스트 파일로 저장
            writeFile(TEXT,LINKS,IMG_LINKS,COMMENTS,link)

        # 링크타고 넘어가서 크롤링하려는데 없어진 페이지인 경우
        except NoSuchElementException as e:
            print(e)
            writeException(link, e)
            pass

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

    # 만약 현재 페이지가 전부 공개 게시물이다
    # -> 비공개 게시물을 찾을 때까지 스크롤 다운
    scroll_down_count = 1

    # 이전 단계의 전체 게시물 갯수를 셈
    # 만약 이전 단계 == 현재 단계 라면
    # 크롤링 할 비공개 게시물이 없음으로 간주
    # 프로그램 종료
    former_board_count = 0

    # 전체 타임라인의 게시물 크롤링
    while True:
        autoWork()

    # 위에 있는 타임라인의 게시물 크롤링
    # autoWork()

except Exception as e:
    print(e)

finally:
    driver.quit()
