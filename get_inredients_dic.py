
def get_inredients():
    number_of_pizzas = int(input("How many pizzas do you want to make today?:"))

    ingredients_dic = {
        #Cups of flour
        "Flour": 3 * number_of_pizzas,
        #tsp of Yeast
        "Yeast": 1 * number_of_pizzas,
        #Cups of water
        "Water": 1.5 * number_of_pizzas,
        #tbsp
        "Olive Oil": 1.5 * number_of_pizzas,
        #tsp 
        "Salt": 2 * number_of_pizzas,
        "Sugar": 1 * number_of_pizzas,
        "Oreagano": 1 * number_of_pizzas,
        "Basil": 1 * number_of_pizzas,
        "Black Pepper": 1 * number_of_pizzas,
        "Garlic Pouder": 0.5 * number_of_pizzas,
        #Oz 
        "Tomato Paste": 3 * number_of_pizzas,
        "Mozzarella": 8 * number_of_pizzas,
        "calories": 4409 * number_of_pizzas,
        "number of pizza": number_of_pizzas
    }
    return ingredients_dic