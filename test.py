import requests


def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '6468363d'
    app_key = 'a28413f876f1d5d0b52d989a87344cc2'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()


run()