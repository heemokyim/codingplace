import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

scope=[
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = sac.from_json_keyfile_name('cred.json',scope)

gc = gspread.authorize(credentials)

# *********************
doc = gc.create('테스트 문서2')

gc.import_csv(doc.id, open('test.csv','r').read())
# *********************


doc.share('anylee2142@gmail.com', perm_type='user', role='owner')
# doc.share('anylee2142@gmail.com', perm_type='user', role='reader')
# doc.share('anylee2142@gmail.com', perm_type='user', role='writer')
