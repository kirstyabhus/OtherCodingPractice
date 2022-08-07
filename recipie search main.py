import requests

ingr = input("What ingredient do you want to search for? ")
appkey = 'a28413f876f1d5d0b52d989a87344cc2'
appID ='6468363d'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingr, appkey, appID)

response = requests.get(url)
recipe = response.json()