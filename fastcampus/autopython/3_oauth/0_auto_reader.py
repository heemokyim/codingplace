import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=[
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json',scope)

gc = gspread.authorize(credentials)

doc = gc.open_by_url('https://docs.google.com/spreadsheets/d/1XszjhPE8uJKBuAdvOb_WpXdG3X1kn25XDkOOkxTvHQA/edit#gid=0')

worksheet = doc.get_worksheet(0)

# val = worksheet.acell('B1').value

# val = worksheet.row_values('1')

# val = worksheet.col_values('1')

val = worksheet.range('A1:B2')

# print(val)

cur_row = 1
for each in val:
    if cur_row != each.row:
        print()
    print(each.value)
    cur_row = each.row
