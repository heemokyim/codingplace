# We only implement SMTP side, not POP
# Why? because we only need to send, not receive

# Class for sending text email
from email.mime.text import MIMEText
# Class making things for SMTP
from email.mime.multipart import MIMEMultipart
# ex) html = structure, MIME = content inside of it
import smtplib

f = open('/home/ej/older/password','r')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'anylee2142@gmail.com'
SMTP_PASSWORD = f.read()

class Email():
    from_email = SMTP_USER
    subj_layout = '님에게 메일 도착'
    cont_layout = '''<b>님에게 메일 도착 </b></br></br>
안녕하세요 자동화로 보내지는 메일입니다.
<h1> h1제목입니다. </h1>
    '''

    def is_valid_email(self,addr):
        import re

        if re.match(('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),addr):
            return True
        else:
            return False

    def send_mail(self,name,addr,attachment=None):
        if not self.is_valid_email(addr):
            print("Wrong email: "+addr)
            return

        msg = MIMEMultipart('alternative')

        # Code for processing attachment
        if attachment:
            msg = MIMEMultipart('mixed')

        # msg['From'], msg['To'] can be filled with random value
        msg['From'] = self.from_email
        msg['To'] = addr
        msg['Subject'] = name + self.subj_layout

        contents = name + self.cont_layout
        # text = MIMEText(_text=contents, _charset='utf-8')
        text = MIMEText(_text=contents,_subtype='html', _charset='utf-8')
        msg.attach(text)

        if attachment:
            from email.mime.base import MIMEBase
            from email import encoders

            # octect-stream = 일반 파일을 의미
            file_data = MIMEBase('application','octect-stream')
            # 입력받은 파일명으로 파일을 open
            file_data.set_payload(open(attachment, 'rb').read())
            # 전송가능한 base64 형태로 변환
            # Why base64?
            # https://www.clien.net/service/board/kin/2641682
            encoders.encode_base64(file_data)

            import os
            # 파일경로로부터 파일명을 가져옴
            filename = os.path.basename(attachment)
            # 파일명 정보를 추가 (메타데이터)
            file_data.add_header('Content-Disposition','attachment; filename="'+filename+'"')
            # 파일 데이터를 Multipart에 추가
            msg.attach(file_data)

        smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        # To login, unlock blocked-ip-login
        smtp.login(SMTP_USER,SMTP_PASSWORD)

        smtp.sendmail(SMTP_USER, addr, msg.as_string())

        smtp.close()

if __name__ == '__main__':
    e = Email()
    e.send_mail('이재웅','jkl2142@naver.com')
    e.send_mail('재웅재웅','jkl2142@naver.com','email_address.xlsx')
