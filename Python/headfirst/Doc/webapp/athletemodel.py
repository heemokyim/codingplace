def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string
    (min,sec)=time_string.split(splitter)

    return min+'.'+sec

class Athlete(list):
    def __init__(self,name,birth='',record=[]):
        list.__init__([])
        self.name=name
        self.birth=birth
        self.extend(sorted([sanitize(each) for each in record]))
    def top3(self):
        return self[0:3]

def fileRead(file_name):
    try:
        with open(file_name,'r') as dataRead:
            buf=dataRead.readline().strip().split(',')
            return Athlete(buf.pop(0),buf.pop(0),buf)
    except IOError as ioErr:
        print(str(ioErr))
        return None
'''
print(sarah['Name']+"'s top 3 fastest times are "+str(sarah['Record'][0:3]))
'''
