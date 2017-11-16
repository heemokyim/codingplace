from openpyxl import load_workbook

wb = load_workbook('data/excel_writable.xlsx')
sheet1 = wb.active

sheet2 = wb['sheet_test']

print(sheet1['A1'].value)
print(sheet1['A2'].value)
print(sheet1['B1'].value)
print(sheet1['B2'].value)

print(sheet2['A1'].value)
print(sheet2['A2'].value)
print(sheet2['B1'].value)
print(sheet2['B2'].value)
