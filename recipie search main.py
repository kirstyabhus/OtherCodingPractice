import requests


# Function to find the recipe names for a given ingredient
def get_names():
    global app_key
    app_key = 'a28413f876f1d5d0b52d989a87344cc2'
    global app_ID
    app_ID = '6468363d'

    # the ingredient to search for
    ingr = input("\nWhat ingredient do you want to search for? ")
    recipe_names = []

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingr, app_ID, app_key)

    response = requests.get(url)
    global recipe
    recipe = response.json()

    # find the number of "hits" aka the number of recipes found for the ingredients
    length = len(recipe["hits"])

    # run through all the recipes
    for i in range(length):
        # store the name of the current recipe
        name = recipe["hits"][i]["recipe"]["label"]
        # add the current recipe name to the list
        recipe_names.append(name)
        # print out the recipe name and list number
        print(f"{i + 1}. {name}")

    return recipe_names


# A function to ask the user to choose a recipe, and to output the recipes' ingredient list
def get_recipe(recipe_names):
    # Ask the user which recipe option they would like to see
    user_option = int(input("\nWhich recipe would you like to see the details for? Enter the number: ")) - 1
    # store the recipe name
    user_recipe = recipe["hits"][user_option]["recipe"]["label"]

    # find the number of ingredients in the recipes' ingredient list
    ingr_len = len(recipe["hits"][user_option]["recipe"]["ingredientLines"])

    print(f"\nINGREDIENTS for {user_recipe}")
    # print out each ingredient line of the users' recipe
    for x in range(ingr_len):
        print(recipe["hits"][user_option]["recipe"]["ingredientLines"][x])

    # print the link for the preparation method
    print(f"\n The method for preparing {user_recipe} can be found in the link below:")
    print(recipe["hits"][user_option]["recipe"]["url"])


get_recipe(get_names())


#def testing(recipe_names):
    #print(recipe["hits"][1]["recipe"]["url"])
    #print(recipe["hits"][1]["recipe"]["totalTime"])
    # "totalTime"
    # "cuisineType"
#testing(get_names())

