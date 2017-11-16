# We only implement SMTP side, not POP
# Why? because we only need to send, not receive

# Class for sending text email
from email.mime.text import MIMEText
# Class making things for SMTP
from email.mime.multipart import MIMEMultipart
# ex) html = structure, MIME = content inside of it
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'dlxoghkqwer@gmail.com'
SMTP_PASSWORD = 'fastcampus1'

def send_mail(name,addr):
    msg = MIMEMultipart('alternative')

    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name + '에게 메일 도착'

    contents = name + '님에게 메일 도착함'

    text = MIMEText(contents)
    msg.attach(text)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    # To login, unlock blocked-ip-login
    smtp.login(SMTP_USER,SMTP_PASSWORD)

    smtp.sendmail(SMTP_USER, addr, msg.as_string())

    smtp.close()

send_mail('이재웅','jkl2142@naver.com')
