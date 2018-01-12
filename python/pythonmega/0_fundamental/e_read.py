# open readable connection
file=open('q.txt','r')

type(file)  # IOWrapper

content=file.read()
# print(content)
type(content)   # string

# move pointer to 0 (= start point)
file.seek(0)

content=file.readlines()

for each in content:
    print(each)
print(content)

# trimming \n of right-side of each
content1=[each.rstrip("\n") for each in content]

print(content1)

# prventing unexpected memory leak
file.close()
