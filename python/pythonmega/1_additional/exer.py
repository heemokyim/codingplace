# merge 3 text file
# filename should be made with module datetime
import glob2
import datetime

# if files are big,
# use stream module, not open
def merging():
    files=glob2.glob('files/*')
    f_name=datetime.datetime.now()
    files.reverse()

    try:
        with open(f_name.strftime("%Y-%m-%d %H:%M:%S")+".txt",'w') as writable:

            for file in files:
                writable.write(extract(file))
                writable.write('\n')
    except:
        print('Error while writing')

def extract(file):
    content=None
    try:
        with open(file,'r') as readable:
            content=readable.read()
    except:
        print('Error while reading')
    return content

if __name__=="__main__":
    merging()
