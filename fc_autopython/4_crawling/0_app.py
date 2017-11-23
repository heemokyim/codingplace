from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    # 네이버 뉴스 페이지로 이동
    driver.get('http://news.naver.com')

    # id가 right.ranking_contests인 태그를 가져옴
    elem = driver.find_element_by_id('right.ranking_contents')

    # 위 태그의 하위 태그들 중에 li 태그들을 모두 가져옴
    lis = elem.find_elements_by_xpath('./ul/li')

    # find_elements_* VS find_element_* ?
    # 다 찾아와 VS 하나만 찾아와
    for li in lis:
        tag = li.find_element_by_class_name('fs11')
        print(tag.text)
        print(tag.get_attribute('href'))

    # 각 기사들 링크 가져오기

except Exception as e:
    print(e)

finally:
    # 파이썬 프로세스가 어떤 상태로 끝나더라도 웹페이지는 항상 꺼야 메모리 릭을 막음
    # finally 안에 쓰기 적합한 코드
    driver.quit()
