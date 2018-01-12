# 1. Read email list from Google SpreadSheet
# 2. Send email to them

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=[
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json',scope)

gc = gspread.authorize(credentials)

doc = gc.open_by_url('https://docs.google.com/spreadsheets/d/1whVnix1t3au-Vp4bhvcuXdZghlsVaSHKearcU3xe5WY/edit#gid=0')

worksheet = doc.get_worksheet(0)

val = worksheet.row_values('1')

name = val[0]
email = val[1]

from auto_email import Email

e = Email()

for idx in range(worksheet.row_count):
    row = worksheet.row_values(str(idx+1))
    e.send_mail(row[0],row[1])
