# there are 2 modules for date, time
# datetime, date

import datetime
import time
# grab date from computer
datetime.datetime.now()

yesterday = datetime.datetime(2017,12,13,11,0,0,0)
now=datetime.datetime.now()

# arithmetic operation available
delta=yesterday-now
after=now+datetime.timedelta(days=2)

filename=datetime.datetime.now()
# filename=now.strftime("%Y-%m-%d %H:%M:%S %f")
# Refer to http://strftime.org/

def create_file():
    with open(filename.strftime("%Y-%m-%d %H:%M:%S")+".txt",'w') as file:
        file.write('')

if __name__=="__main__":
    create_file()

lst=[]
for each in range(5):
    lst.append(datetime.datetime.now())
    # stop as much as passed argument = 1
    time.sleep(1)
