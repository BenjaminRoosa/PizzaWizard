def command_sanitizer(command):
    dirty_command = input(f"{command}")
    command_list = dirty_command.split()
    sanitized_commands = []
    for command in command_list:
        sanitized_commands.append(command.lower().strip())
    return sanitized_commands

def true_false(command_string): #left off there
    add_command = command_sanitizer(f"{command_string}")
    
    add_another_loop = True
    while add_another_loop:
        if add_command[0] == "y":
            add_another_loop= False
            return True
        elif add_command[0] == "n":
            add_another_loop= False
            return False
        else:
            print("Invaid input. Try again.")
def mesh_dics(dic_a, dic_b):
    a_keys = dic_a.keys()
    b_keys = dic_b.keys()
    total_keys_dupe = a_keys + b_keys
    total_keys = {}
    total_keys.update(total_keys_dupe)
    ab_dic = {}
    
    for i in total_keys:
        if i in a_keys and i in b_keys:
            ab_dic[i].amount = dic_a[i].amount + dic_b[i].amount
        
        elif i in a_keys:
            ab_dic[i].amount = dic_a[i].amount
        else:
            ab_dic[i].amount = dic_b[i].amount
    return ab_dic
class Order:
    def __init__(self):
        self.pizza_list = []
        self.pizza_number = 1
    
    def create_pizza(self):
        create_pizza_loop = True
        print("What kind of pizza do you wish for?\n")
        #format pizza_name: ["discription", calories, tags, extra_ingredients]. this is to use to just make the Pizza_obj in one line and not do the fuckery in the while loop
        pizza_menue = {
            "basic": ["Just crust, sauce, and cheese.", 2072, [], {}],
            "perpperoni": ["A basic with pepperoni topping.",2144,["perpperoni"], {"perpperoni":{"measurement":"ounces","amount":0.5}}],
            "cheese": ["It what it says on the tin, a basic with extra cheese.",2384,["extra cheese"],{"mozzarella":{"measurement": "ounves", "amount":4.0}}],
            "dulux": ["Extra pepperoni, extra chees, and extra calories.",2528,["perpperoni","extra cheese"],{"perpperoni":{"measurement":"ounces","amount":0.5},"mozzarella":{"measurement": "ounves", "amount":4.0}}]
        }
        while create_pizza_loop:
            create_command = command_sanitizer("---")
            if create_command[0] in pizza_menue.keys():
                new_name = f"{self.pizza_number} -{create_command[0]}"
                new_discription = pizza_menue[create_command[0]][0]
                new_calories = pizza_menue[create_command[0]][1]
                new_tags = pizza_menue[create_command[0]][2]
                new_ingredients = pizza_menue[create_command[0]][3]
                new_pizza = Food(new_name,new_discription,new_calories,new_tags,new_ingredients)
                self.pizza_list.append(new_pizza)
                self.pizza_number += 1
                print(f"{new_pizza.name} added to order.")
            elif create_command[0] == "help":
                print("help:        Prints create pizza command list.")
                print("basic:       Just crust, sauce, and cheese.")
                print("pepperoni:   A basic with pepperoni topping.")
                print("cheese:      It what it says on the tin, a basic with extra cheese.")
                print("dulux:       Extra pepperoni, extra chees, and extra calories.")
                print("back:        return main menue.")
            
            elif create_command[0] == "back":
            
                create_pizza_loop = False
            
                print("Returning to main menue.")
            else:
                print("Invaid command.")
            
    def is_pizza(self,pizza_name):
        if len(self.pizza_list) < 1:
            return False
        pizza_name_lst = []
        for pizza in self.pizza_list:
            pizza_name_lst.append(pizza.name)
     
        if pizza_name in pizza_name_lst:
            return True
        else:
            return False
    def print_pizza_order(self):
        for pizza in self.pizza_list:
            print(f"{pizza.name}")
    def get_pizza_index(self,pizza_name):
    
        for pizza in self.pizza_list:
        
            if pizza.name == pizza_name:
                return self.pizza_list.index(pizza)
    def remove_pizza(self):
        if len(self.pizza_list) < 1:
                print("No pizza to remove. Negative matter pizza is not alowed. Because it hurts to think about.")
                return
        self.print_pizza_order()

        pizza_to_remove = command_sanitizer("Enter the pizza number to remove.")
        
        if self.is_pizza(pizza_to_remove[0]):
                self.pizza_list.pop(self.get_pizza_index(pizza_to_remove[0]))
        else:
            print("No pizza with that name.")

    def print_ingredients(self):
        total_ingredients = {}
        for pizza in self.pizza_list:
            total_ingredients = mesh_dics(total_ingredients, pizza.ingredients)
        for ingredient in total_ingredients:
            ing_name = ingredient
            ing_amount = total_ingredients[ingredient]["amount"]
            ing_measurement = total_ingredients[ingredient]["measurement"]
            ing_note = total_ingredients[ingredient]["note"]
            print(f"{ing_amount} {ing_measurement} of {ing_name}")
            print(f"{ing_note}")
    def print_calories(self):
        if len(self.pizza_list) < 0 :
            print("Zer0, zelch, nada, calories.")
        for pizza in self.pizza_list:
            print(f"{pizza.name} --- {pizza.calories}")
    
    def get_tags(self):
        tags = {}
        for pizza in self.pizza_list:
            if len(pizza.tags) > 1:
                for tag in pizza.tags:
                    if tag in tags:
                        old_value = tags[tag]
                        new_value = old_value +1
                        tags[tag]= new_value
                    else:
                        tags[tag] = 1
            elif len(pizza.tags) == 1:
                if tag in tags:
                    old_value = tags[tag]
                    new_value = old_value +1
                    tags[tag]= new_value
                else:
                    tags[tag] = 1
            else:
                continue
        return tags
class Food:
    def __init__(self, name,discription, calories,tags,extra_ingredients):
        self.name = name
        self.discription = discription
        #all measurements are by weight
        self.tags = tags
        self.calories = calories
        self.extra_ingredients = extra_ingredients
        self.ingredients = {
            "flour" : {
                "measurement" : "cups",
                "amount" : 3,
                "note": "You want all-purpose flour."
            },
            "water" : {
                "measurement" : "cups",
                "amount" : 1.5,
                "note": "also know as raw rocket fule"
            },
            "mozzarella" :{
                "measurement" : "ounces",
                "amount" : 8,
                "note": "the finer the shread the better."
            },
            "salt" : {
                "measurement" : "teaspoons",
                "amount" : 1.5,
                "note": "aka dry sea water."
            },
            "olive oil": {
                "measurement" : "teaspoons",
                "amount" : 1.5,
                "note": "just olive oil without any oils like sunflower, vegetable, canola or coconut."
            },
            "tomato paste": {
                "measurement" : "ounces",
                "amount" : 3,
                "note": "human blood is NOT A SUBSTIUTE."
            },
            "black pepper": {
                "measurement" : "teaspoons",
                "amount" : 0.5,
                "note": "Not black powder, this  is COMMON AND UNDERSTANDABLE MISSTAKE."
            },
            "garlic": {
                "measurement" : "ounces",
                "amount" : 1,
                "note": "Just buy it from the store and save your self the time of tracking, killing, and finding a herbalist to detocify the garlic (this can take 3 - 4 business days)."
            },
            "rosemary": {
                "measurement" : "teaspoons",
                "amount" : 0.5,
                "note": "this is a type of herb, not a person."
            },
            "basil": {
                "measurement" : "teaspoons",
                "amount" : 1,
                "note": "also a herb."
            },
            "oregano": {
                "measurement" : "teaspoons",
                "amount" : 1,
                "note": "again herb."
            },
            "sugar": {
                "measurement" : "teaspoons",
                "amount" : 1,
                "note": "this one is a carb."
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
        
