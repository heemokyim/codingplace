def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string
    (min,sec)=time_string.split(splitter)

    return min+'.'+sec

def fileRead(file_name):
    try:
        with open(file_name,'r') as dataRead:
            buf=dataRead.readline().strip().split(',')
            return buf
    except IOError as ioErr:
        print(str(ioErr))
        return none

    '''
    try :
        with open('julie.txt','r') as data:
            data=data.readline().strip()
            julie=data.split(',')
            #clean_julie=[sanitize(each) for each in julie]
        with open('james.txt','r') as data:
            data=data.readline().strip()
             james=data.split(',')
            #clean_james=[sanitize(each) for each in james]
        with open('mikey.txt','r') as data:
            data=data.readline().strip()
            mikey=data.split(',')
            #clean_mikey=[sanitize(each) for each in mikey]
        with open('sarah.txt','r') as data:
            data=data.readline().strip()
            sarah=data.split(',')
            #clean_sarah=[sanitize(each) for each in sarah]
        except IOError as ioErr:
            print(str(ioErr))
        '''
julie=fileRead('julie.txt')
james=fileRead('james.txt')
mikey=fileRead('mikey.txt')
sarah=fileRead('sarah.txt')


print(sorted([sanitize(each) for each in julie]))
print(sorted([sanitize(each) for each in james]))
print(sorted([sanitize(each) for each in mikey]))
print(sorted([sanitize(each) for each in sarah]))
#print(sorted(clean_julie)) 


julie=sorted([sanitize(each) for each in julie])
james=sorted([sanitize(each) for each in james])
mikey=sorted([sanitize(each) for each in mikey])
sarah=sorted([sanitize(each) for each in sarah])
# desired, sorted form but duplication exists

'''
unique_james=[]
for each in james:
    if each not in unique_james:
        unique_james.append(each)
'''

'''
unique_james=set(james)
unique_julie=set(julie)
unique_mikey=set(mikey)
unique_sarah=set(sarah)
'''# using 'set' factory function to get rid of duplication

print(sorted(set(james))[0:3])
