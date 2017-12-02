def get_11st(keyword):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()

    results = []

    try:
        driver.get('http://11st.co.kr')

        inp_txt = driver.find_element_by_class_name('header_inp_txt')

        inp_txt.clear()
        inp_txt.send_keys(keyword)
        inp_txt.send_keys(Keys.RETURN)

        # xpath로 모든 게시글을 가져옴
        result_list = driver.find_elements_by_xpath("//li[contains(@id,'thisClick_')]")
                                                # // li 뜻 -> 조건을 만족하는 모든 li 경로
                                                # 조건들 -> 태그[조건]  (li[contains])
                                                # id를 가지고 있는데 (@id)
                                                # thisClick을 포함하고 있는
        # .//li => 현재 경로로부터 있는 모든 li
        # //li => 모든 경로로부터 있는 모든 li

        for result in result_list:
            title_tag = result.find_element_by_class_name('info_tit')
            price_tag = result.find_element_by_class_name('sale_price')
            mail_tag = result.find_element_by_class_name('benefit_tit')

            results.append((title_tag.text, price_tag.text, mail_tag.text))

        # seller_list = driver.find_elements_by_xpath("//a[@data-log-actionid-label='sellername']")
        # for seller in seller_list:
        #     print(seller.text)

    except Exception as e:
        print(e)

    finally:
        driver.quit()

    return results

if __name__ == '__main__':
    results = (get_11st('자전거'))

    for each in results:
        print(each)
