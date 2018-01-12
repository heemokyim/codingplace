# In Windows,
# how can i pass "\n" without break line in path?
# how can i tell python to take simple string, not special letter?
# host_path= r'C:\Windows\System32\drivers\etc\hosts'

# How to copy hosts file in here?
# == cp path .
# ex) cp 'C:\Windows\System32\drivers\etc\hosts' .
# ex) cp /etc/hosts .

import time
from datetime import datetime as dt
import platform

# Note that when you execute app by task scheduler,
# directory will not be located here
# so when you use local file system with task scheduler
# Always use absolute path
host_temp='D:\GoogleDrive\CodingPlace\Python\PythonMega\c_blocker\hosts'
hosts_path=''
redirect='127.0.0.1'
input_line = lambda each : redirect+'\t'+each+'\n'

start_time=12
end_time=18

isAdded=False

platform_os=platform.system().lower()
if platform_os=='windows':
    host_path=r'C:\Windows\System32\drivers\etc\hosts'
    origin_len = 822
else:
    host_path='/etc/hosts'

# 1. list of websites you want to block
# 2. can be I/O from file
website_list=["www.facebook.com","www.naver.com",'www.yahoo.com']

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day, start_time) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time)):
        print('Working time !')
        if not isAdded:
            with open(host_temp,'r+') as file:
                content=file.read()
                for each in website_list:
                    if each not in content:
                        file.write(input_line(each))
                isAdded=True

    else:
        if isAdded:
            print('fun time !')
            with open(host_temp,'r+') as file:
                lines=file.readlines()
                file.seek(0)
                for line in lines:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate(origin_len)
                file.write('\n')
                isAdded=False
    time.sleep(5)
