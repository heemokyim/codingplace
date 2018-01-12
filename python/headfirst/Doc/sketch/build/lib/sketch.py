try:
 data=open('D:\Python\Doc\sketch\sketch.txt')
 man=[]
 other=[]
 
 for each in data:
        try:
            (role,script)=each.split(':',1)
            script=script.strip()
            if role=='Man':
                man.append(script)             
            elif role=='Other Man':
                other.append(script)
        except ValueError:
            pass
 
except IOError:
    print("no file has been found")
    
try:
    with open('man_data.txt','w') as man_data:
        print_lol(man,True,1,man_data)
    print('its about half')
        
    with open('other_data.txt','w') as other_data:
        print_lol(other,True,1,other_data)
    
except IOError:
    print("Error has occured while making files")
