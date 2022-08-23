import requests
#

# to find the recipe names for a given ingredient
def get_names():
    global appkey
    appkey = 'a28413f876f1d5d0b52d989a87344cc2'
    global appID
    appID = '6468363d'

    # the ingredient to search for
    ingr = input("What ingredient do you want to search for? ")
    recipe_names = []

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingr, appID, appkey)

    response = requests.get(url)
    recipe = response.json()

    # find the number of "hits" aka the number of recipes found for the ingredients
    length = len(recipe["hits"])

    # run through all the recipes
    for i in range(length):
        # store the name of the recipe
        name = recipe["hits"][i]["recipe"]["label"]
        # add the recipe name to the list
        recipe_names.append(name)
        # print out the recipe name and list number
        print(f"{i+1}. {name}")

    return recipe_names


get_names()

# when inputting more than one ingredient at one go, in a comma separated list
# x = input().lower()
# j = x.split(",")
# print(j)
