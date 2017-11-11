from openpyxl import load_workbook

excel_file = load_workbook('data/excel_writable.xlsx')

worksheet = excel_file['sheet_test']

# one row
row_of_worksheet = worksheet['2']
for cell in row_of_worksheet:
    print(cell.value)

# one col
col_of_worksheet = worksheet['1']
for cell in col_of_worksheet:
    print(cell.value)

# picking up square
area = worksheet['A1:B2']
for row in area:
    for cell in row:
        print(cell.value)

# multiple rows
rows = worksheet['1:2']
for row in rows:
    for cell in row:
        print(cell.value)

# multiple cols
cols = worksheet['A:B']
for col in cols:
    for cell in col:
        print(cell.value)
