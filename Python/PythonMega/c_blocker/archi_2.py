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


host_temp='hosts'
hosts_path=''
redirect='127.0.0.1'
input_line = lambda each : redirect+'\t'+each+'\n'

start_time=12
end_time=18

platform_os=platform.system().lower()
if platform_os=='windows':
    host_path=r'C:\Windows\System32\drivers\etc\hosts'
    origin_len = 822 + 2
else:
    host_path='/etc/hosts'

# 1. list of websites you want to block
# 2. can be I/O from file
website_list=["www.facebook.com","www.naver.com",'www.yahoo.com']

with open(host_temp,'r+') as file:
    file.seek(0,2)
    file.write('\n')
    # Windows = cr + lf = 2
    # Linux = lf = 1
    file.seek(0,0)

    isAdded=False

    while True:
        # if working hour,
        # if start_time <= dt.now().hour < end_time:
        if (dt(dt.now().year,dt.now().month,dt.now().day, start_time) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time)):
            print('Working time !')

            if not isAdded:
                print('Adding blocker !')
                content=file.read()
                # By file.read(), pointer moves to EOF

                for each in website_list:
                    if each not in content:
                        file.write(input_line(each))
                isAdded=True

        else:
            if isAdded:
                print('fun time !')
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate(origin_len)
                isAdded=False

        # file.close
        # 1. return resource to cpu
        # 2. flush

        # but (with open) is outside of while,
        # which means there is no file.close until explicitly runned
        # To put data to file on the fly,
        # we need to flush explicitly before termination
        file.flush()
        time.sleep(1)
