class Email:
    from_email=""
    to_email=""
    subject=""
    contents=""

    def is_valid_email(sef):
        return True

    def send_mail(self):
        print('send !')

email=Email()
email.from_email='jkl2142@naver.com'
email.to_email='to@gmail.com'
email.subject='12444'
email.contents='Hello'
