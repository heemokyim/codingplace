class Email:
    from_email=''
    to_email=''
    subject=''
    contents=''

    def send_mail(self):
        print('Send to '+ self.to_email)
