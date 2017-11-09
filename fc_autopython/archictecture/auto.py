from my_email import Email
from my_excel import Excel
from my_news import News

m_email=Email()
m_news=News()
m_excel=Excel()

news_list = m_news.find_news('fastcampus')

m_email.from_email = 'alghost@naver.com'
m_email.to_email = 'jkl2142@naver.com'
m_email.subject='MY DEAR SOMEONE'

for news in news_list:
    m_email.contents = m_email.contents + news + '\n'

m_email.send_mail()

m_excel.excel_find = 'result.xlsx'
m_excel.save_to_excel(news_list)
