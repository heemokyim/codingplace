from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

try:
    driver.get('http://11st.co.kr')

    inp_txt = driver.find_element_by_class_name('header_inp_txt')

    inp_txt.clear()
    inp_txt.send_keys('자전거')
    inp_txt.send_keys(Keys.RETURN)

    curr_page = 1
    import time
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(0.5)
        driver.execute_script('window.scrollTo(0,0);')
        time.sleep(0.5)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

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
            print(title_tag.text)
            print(price_tag.text)
            print(mail_tag.text)

            try:
                span = result.find_element_by_xpath(".//span[text()='고객응대우수']")
                print("고객응대우수 판매자입니다.")
            except:
                pass

        curr_page += 1
        page_link = driver.find_element_by_link_text(str(curr_page))
        page_link.click()
        time.sleep(2)

    # seller_list = driver.find_elements_by_xpath("//a[@data-log-actionid-label='sellername']")
    # for seller in seller_list:
    #     print(seller.text)

    input()

except Exception as e:
    print(e)

finally:
    driver.quit()
