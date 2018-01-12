import urllib.request as ureq
import urllib.parse as upar

import json

def addrToCord(address):
    apiurl="http://maps.google.com/maps/api/geocode/json"
    address=address.encode('utf-8')

    param=upar.urlencode({
        'address':address,
        'sensor':'false'
    })

    req=ureq.urlopen(apiurl+"?%s" %param)
    return req.read().decode('utf-8')

if __name__=="__main__":
    res=addrToCord('수원 영통구 이의동 1257-1')
    result=json.loads(res,encoding='utf-8')
    print('%(lng)f %(lat)f' % result['results'][0]['geometry']['location'])

    address=result['results'][0]['address_components']
    for each in address:
        print(each)
    print(address[5]['short_name'])
