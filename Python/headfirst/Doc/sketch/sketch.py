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
    with open('man_data.txt','wb') as man_data:
        pickle.dump(man,man_data)
    print('its about half')
        
    with open('other_data.txt','wb') as other_data:
        pickle.dump(other,other_data)
    with open('man_data.txt','rb') as man_read:
        man_list=pickle.load(man_read)
            
except IOError:
    print("Error has occured while making files")


