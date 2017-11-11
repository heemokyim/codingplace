data=[]

data.append({'name':'lee','age':'27','company':'where'})

file = open('data/csv_writable.csv','w')

for each in data:
    file.write(','.join(each.values())+'\n')
