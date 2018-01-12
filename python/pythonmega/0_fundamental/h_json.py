data=open('data.json','r',encoding='utf-8-sig')
print(data.read())
# return string

import json
data1=json.load(open('data.json','r'))
print(data1)
# return dictionary (JSON)
