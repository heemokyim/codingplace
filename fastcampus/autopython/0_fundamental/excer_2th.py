emp=[]
emp.append({'name':'woong','age':26})
emp.append({'name':'what','age':27})
emp.append({'name':'whoami','age':22})


count=0
for each in emp:
    if each['position']=='ceo':
        continue
    if each['age']>=30:
        count+=1
