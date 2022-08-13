import requests


def ingr_request():
    ingredient = input("What ingredient do you want to search for? ")
    app_key = 'a28413f876f1d5d0b52d989a87344cc2'
    app_id = '6468363d'

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    response = requests.get(url)
    recipe = response.json()
    print(response)

    # prints ALL the recipes related to the ingredient (including all the recipe details)
    #print(recipe)

    print("\n--------------\n")

    # Prints the NAME of the recipe (there must be an easier way than this though?)
    print(recipe["hits"][0]["recipe"]["label"])
    print(recipe["hits"][1]["recipe"]["label"])

ingr_request()