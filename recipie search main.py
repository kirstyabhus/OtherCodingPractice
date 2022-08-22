import requests

ingr = input("What ingredient do you want to search for? ")
appkey = 'a28413f876f1d5d0b52d989a87344cc2'
appID ='6468363d'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingr, appID, appkey)

response = requests.get(url)
recipe = response.json()

# find the number of "hits" aka the number of recipes found for the ingredients
length = len(recipe["hits"])

# run through all the recipes and print only their names
for i in range(length):
    print(recipe["hits"][i]["recipe"]["label"])

def request():
    pass