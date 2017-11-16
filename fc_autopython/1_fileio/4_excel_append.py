from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('data/excel_writable.xlsx')

ws = wb['sheet_test']

ws.append(['Number','Name'])

for i in range(10):
    ws.append([i,str(i)+' data'])

wb.save('data/excel_writable.xlsx')
