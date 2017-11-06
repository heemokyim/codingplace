# open writable connection
# With writable connection, create new one if not exist
file=open('fruits2.txt','w')

file.write("my name is Mr.Claud\n")
file.write('1234\n')

list=['hahaha','testest','my name is what']
for item in list:
    file.write(item+"\n")

file.close()

# How to overwrite?
file=open('fruits2.txt','a')
file.write('Line 4\n')
file.close()
