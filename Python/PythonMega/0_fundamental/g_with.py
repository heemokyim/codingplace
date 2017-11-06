try:
    with open('fruits1.txt','r') as file:
        content=file.read()
        print(content)

except:
    print('no')
