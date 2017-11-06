try:
    with open ('missing.txt','w') as data:
    print(data.readline(),end='')
except IOError as err:
    print(str(err))
