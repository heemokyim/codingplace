from selenium import webdriver

def get_naver_news(guit):
    return_news = []

    opts = webdriver.ChromeOptions()

    # 백그라운드에서 실행시키는 옵션
    opts.add_argument('headless')

    guit.append_log('브라우저를 띄웁니다.')
    driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

    try:
        guit.append_log('네이버 뉴스로 접속합니다.')
        driver.get('http://news.naver.com')

        # div = driver.find_element_by_id('right.ranking_contents')
        # news_list = div.find_elements_by_tag_name('li')

        # div = driver.find_element_by_id('right.ranking_contents')
        # news_list = div.find_elements_by_xpath('./ul/li')

        news_list = driver.find_elements_by_xpath("//div[@id='right.ranking_contents']/ul/li")
        for news in news_list:
            return_news.append(news.text)

        guit.append_log('웹 페이지 분석을 마쳤습니다.')

    except Exception as e:
        print(e)
    finally:
        driver.quit()

    return return_news

if __name__ == "__main__":
    res = get_naver_news()
    print(res)
