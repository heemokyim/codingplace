from geopy.geocoders import Nominatim
geolocator=Nominatim()
location=geolocator.reverse("37.304240, 127.047337")

print(location.address)
print(location.latitude,location.longitude)

# 6-digits postal code 443-270
# 5-digits postal code 16507
# 한국 지번번호         1257-1
                                                # all work
location1=geolocator.geocode('이의동, 수원시, 경기, 1257-1, 대한민국')
# only needs 동, 시, 도, 우편번호, 나라이름

print(location.longitude)
print(location.latitude)
