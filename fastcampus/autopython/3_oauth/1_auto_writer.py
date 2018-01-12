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

# worksheet.update_acell('B1','Updated value')

# worksheet.resize(3,3)
# worksheet.append_row(['New_data','New_data1','New_data2'])

worksheet.insert_row(['What','are','you'], 1)
