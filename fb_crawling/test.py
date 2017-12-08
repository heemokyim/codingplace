# from selenium import webdriver
#
# driver = webdriver.Chrome('./chromedriver.exe')
#
# try:
#     # 네이버 뉴스 페이지로 이동
#     driver.get('https://www.facebook.com/anylee2142/posts/376987242752515?pnref=story')
#
#     input()
#
#
# except Exception as e:
#     print(e)
#
# finally:
#     # 파이썬 프로세스가 어떤 상태로 끝나더라도 웹페이지는 항상 꺼야 메모리 릭을 막음
#     # finally 안에 쓰기 적합한 코드
#     driver.quit()


try:
    print('1')
    raise ca()
    print('2')

except ca as c:
    print(c)
