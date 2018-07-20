import requests
from pprint import pprint
city = input('ENter your city:')
url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=70d8db7a91ba514a904d020f58a78dd0'.format(city)
res = requests.get(url)# get data from website
data = res.json()
#print(res)
#pprint(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longtitude = data['coord']['lon']

description = data['weather'][0]['description']
print('Temperature= {} degree celcius'.format(temp))
print('Wind: {} m/s'.format(wind_speed))
print('Latitude: {}'.format(latitude))
print('Longtitude: {}'.format(longtitude))
print('Description: {}'.format(description))
