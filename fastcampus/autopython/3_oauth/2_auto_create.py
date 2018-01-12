import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

scope=[
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = sac.from_json_keyfile_name('cred.json',scope)

gc = gspread.authorize(credentials)

gs = gc.create('테스트 문서')

gs.share('anylee2142@gmail.com', perm_type='user', role='owner')

# ---------------------------------------------------------------------
# worksheet = gs.add_worksheet(title='시트1', rows='1',cols='1')
#
# worksheet.insert_row(['ID','DATA'],1)
#
# for i in range(10):
#     worksheet.append_row([i,str(i)+'Data'])
# ---------------------------------------------------------------------

worksheet = gs.get_worksheet(0)

worksheet.insert_row(['ID','DATA'],1)
