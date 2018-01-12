file = open('data/csv_data.csv','r+')

while True:
    line = file.readline().strip()

    if not line:
        break

    data = line.split(',')

    for cell in data:
        print(cell)
