datafile = open('data/data.txt','r')
data = datafile.read()
print(data)


datafile = open('data/data.txt','r')
line='init'

while line:
    line=datafile.readline()
    print(line)
