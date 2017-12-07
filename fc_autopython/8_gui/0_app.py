from tkinter import *

class GUIT():
    def __init__(self):
        # 트킨터를 사용하기 위해 변수 생성
        self.tkhandler = Tk()

        # 창 크기 지정
        self.tkhandler.geometry('500x500')

        # 창 제목 지정
        self.tkhandler.title('패스트캠퍼스 자동화 프로그램')

        # Label 클래스를 생성, 추가할 창과 출력할 문자열을 넣음
        self.label_title = Label(self.tkhandler, text='안녕하세요. 자동화 프로그램입니다.')

        # 추가할 위치를 지정하는 함수 pack()
        # 줄 단위로 들어감
        self.label_title.pack()

        # 웹 자동화 버튼 추가
        # width의 경우 실제로 값을 변경하면서 확인해야 함
        # geometry에서 설정한 값과 절대값이 다름
        self.btn_web = Button(self.tkhandler, text='웹 자동화',width=30,command=self.auto_web)
        self.btn_web.pack()

        # 통합 자동화 버튼 추가
        self.btn_all = Button(self.tkhandler, text='통합 자동화',width=30,command=self.auto_all)
        self.btn_all.pack()

        self.label_email = Label(self.tkhandler,text='이메일 주소')
        self.label_email.pack()

        # 이메일 주소를 입력할 수 있는 텍스트 박스를 추가
        # relief는 텍스트 박스의 디자인을 의미
        # 다른 값은 일부 환겨에서 눈에 안보이는 경우가 있음
        # bd는 테두리 두께
        self.txt = Text(self.tkhandler, width=40, height=1, relief=RIDGE, bd=1)
        self.txt.bind("<Key>",self.ignore_enter)
        self.txt.pack()

        # 이메일 자동화 버튼 추가
        self.btn_email = Button(self.tkhandler, text='이메일 자동화',width=30,command=self.auto_email)
        self.btn_email.pack()

        self.scroll_lbox = Scrollbar(self.tkhandler,orient='vertical')
        self.lbox_log = Listbox(self.tkhandler,yscrollcommand=self.scroll_lbox.set)

        # 스크롤 바는 오른쪽에 붙이고 세로를 채움
        self.scroll_lbox.pack(side='right',fill='y')
        # 리스트 박스는 왼쪽에 붙이고 양쪽으로 채움
        self.lbox_log.pack(side='left',fill='both', expand=True)

        self.append_log('자동화 프로그램을 시작했습니다.')

    def ignore_enter(self,event):
        if event.keysym == 'Return':
            return 'break'

    def auto_all(self):
        from naver_news import get_naver_news
        from auto_email import Email
        from openpyxl import Workbook

        news_list = get_naver_news(self)
        excel_file = 'news_results.xlsx'

        # 액셀에 저장
        wb = Workbook()
        ws = wb.active
        for news in news_list:
            ws.append([news])

        base_dir = '/home/ej/codingplace/fc_autopython/8_gui/'
        wb.save(base_dir + excel_file)

        self.append_log('액셀파일 저장 완료')

        # 이메일 발송
        recv = self.txt.get("1.0",END).strip()

        self.append_log(recv+' 에게 이메일을 발송합니다.')
        e = Email()
        e.send_mail('이재웅',recv,attachment = excel_file)

        self.append_log('이메일 발송 완료')

    def auto_web(self):
        self.append_log('웹 자동화를 시작합니다.')
        from naver_news import get_naver_news

        res = get_naver_news(self)

        for r in res:
            self.append_log(r)

    def append_log(self, msg):
        from datetime import datetime
        today = str(datetime.now())[11:-7]

        # 마지막 줄에 내용을 추가
        self.lbox_log.insert(END,'[%s] %s' % (today,msg))
        # self.lbox_log.inser(END, msg)

        # UI 업데이트
        self.lbox_log.update()

        # 마지막 줄을 보도록 이동
        self.lbox_log.see(END)

    def auto_email(self):
        from auto_email import Email

        # 텍스트박스에 있는 문자열을 가져옴
        # 첫 번째 줄을 뜻하는 1.0 (1이 아니라 1.0으로 써야 함)
        recv = self.txt.get("1.0",END).strip()

        self.append_log(recv+' 에게 이메일을 발송합니다.')
        e = Email()
        e.send_mail('이재웅',recv)

        self.append_log('이메일 발송 완료')

    def run(self):
        # 이벤트를 받기 위한 무한 반복문 실행
        # 프로그램이 mainloop 안에서 돌고 있음
        # 에러가 나도 정상실행 되도록 구현됨
        self.tkhandler.mainloop()

# 클래스 변수 생성
g = GUIT()
g.run()
