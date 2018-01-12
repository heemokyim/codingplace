from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://www.naver.com')
    print(driver.title)

    # 검색어 입력칸을 가져옴
    elem = driver.find_element_by_id('query')
    # 검색어 입력칸 지우기
    elem.clear()
    # 검색어 입력
    elem.send_keys('패스트캠퍼스')
    # 엔터 전송
    elem.send_keys(Keys.RETURN)

    # blog_areas = driver.find_elements_by_class_name('sh_blog_top')
    # for blog in blog_areas:
    #     print(blog.text)

    blog_area = driver.find_element_by_class_name('blog')
    # blog_area = driver.find_element_by_class_name('section')
    # blog_area = driver.find_element_by_class_name('_blogBase')

    blog_list = blog_area.find_elements_by_tag_name('li')
    # print(blog_area.text)
    for blog in blog_list:
        # print(blog.text)
        tag = blog.find_element_by_class_name('sh_blog_title')
        # tag = blog.find_element_by_class_name('_sp_each_url')
        # tag = blog.find_element_by_class_name('_sp_each_title')
        # tag 안에 제목, 링크 둘 다 들어있음

        # print(tag.text)
        print(tag.text)
        print(tag.get_attribute('href'))
        print('-'*30)

    print('='*30)

    cafe_area = driver.find_element_by_class_name('_cafeBase')
    cafe_list = cafe_area.find_elements_by_tag_name('li')

    for cafe in cafe_list:
        tag = cafe.find_element_by_class_name('sh_cafe_title')
        # title property가 없으면 tag.text로 제목
        print(tag.text)
        print(tag.get_attribute('href'))
        print('-'*30)

    print('='*30)

    news_area = driver.find_element_by_class_name('news')
    news_list = news_area.find_elements_by_xpath('./ul/li')

    for news in news_list:
        tag = news.find_element_by_class_name('_sp_each_title')
        print(tag.text)
        print(tag.get_attribute('href'))

        date_tag = news.find_element_by_class_name('txt_inline')
        # removed_tag = data_tag.find_element_by_class_name('_')
        print((date_tag.text.split())[1])


except Exception as e:
    print(e)

finally:
    driver.quit()
