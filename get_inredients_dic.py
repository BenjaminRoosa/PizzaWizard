class Food:
    def __init__(self, name,calories):
        self.name = name
        #all measurements are by weight
        self.tags = []
        self.calories = calories
        self.ingredients = {
            "flour" : {
                "measurement" : "cups",
                "amount" : 3
            },
            "water" : {
                "measurement" : "cups",
                "amount" : 1.5
            },
            "mozzarella" :{
                "measurement" : "ounces",
                "amount" : 8
            },
            "salt" : {
                "measurement" : "teaspoons",
                "amount" : 1.5
            },
            "olive oil": {
                "measurement" : "teaspoons",
                "amount" : 1.5
            },
            "tomato paste": {
                "measurement" : "ounces",
                "amount" : 3
            },
            "black pepper": {
                "measurement" : "teaspoons",
                "amount" : 0.5
            },
            "garlic": {
                "measurement" : "ounces",
                "amount" : 1
            },
            "rosemary": {
                "measurement" : "teaspoons",
                "amount" : 0.5
            },
            "basil": {
                "measurement" : "teaspoons",
                "amount" : 1
            },
            "oregano": {
                "measurement" : "teaspoons",
                "amount" : 1
            },
            "sugar": {
                "measurement" : "teaspoons",
                "amount" : 1
            }
        }
    
"""    
    def add_ingredient(self, ingredient, amount):
        if amount <= 0:
            if amount == 0:
                print(f"Nothing added")
                return
            else:
                amount = abs(amount)
                self.remove_ingredient(ingredient, amount)
                return
        if ingredient.name in self.ingredients.keys():
            self.ingredients[ingredient.name].amount += amount
        
        else:
            self.ingredients[ingredient.name] = ingredient 
            self.ingredients[ingredient.name].amount = amount
        
        print(f"Added {amount} sevings of {ingredient.name}")
        

    def remove_ingredient(self, ingredient, amount):
        if amount <= 0:
            if amount == 0:
                print(f"Nothing removed")
                return
            else:
                amount = abs(amount)
                self.add_ingredient(ingredient, amount)
                return
        if ingredient.name not in self.ingredients.keys():
            print(f"This pizza is allready devoid of {ingredient.name}")

            return
        
        if self.ingredients[ingredient.name].amount - amount < 1:
            del self.ingredients[ingredient.name]
            print(f"All sevings of {ingredient.name} have been removed")
                
        else:
            self.ingredients[ingredient.name].amount -= amount
            print(f"{amount} sevings of {ingredient.name} have been removed")


def get_inredients(food, amount):
    total_base_ingredients =   {}
    if "basic_ingredient" in food.note:
        total_base_ingredients[food.name] = food
        return total_base_ingredients
    for ingredient in food.ingredients:
        if "basic_ingredient" in ingredient.note:
            if ingredient.name in total_base_ingredients:
                total_base_ingredients[ingredient.name] = ingredient.amount + total_base_ingredients[ingredient.name].amount
            else:
                total_base_ingredients[ingredient.name] = ingredient.amount
        else:
            additional_ingredients = get_inredients(ingredient)
            total_base_ingredients = mesh_dics(total_base_ingredients, additional_ingredients)
    return total_base_ingredients
"""


#def create_oreder(number_of_pizzas):
#    order_list = []
#    for i in range(number_of_pizzas):
        
