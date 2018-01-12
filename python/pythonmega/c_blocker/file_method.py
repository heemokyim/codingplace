# 1. store lengrh of file and restore it

# 2. max length - n*(added line length)

# 3. applicable both win and linux

with open('hosts','r+') as file:
    # return maximum length of file
    max_len=file.seek(0,2)
    file.seek(0,0)

    file.write('1234\n')

    file.truncate(max_len)

website_list=['facebook','yahoo','naver']

with open('hosts','r+') as file:
    content=file.readlines()

    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
