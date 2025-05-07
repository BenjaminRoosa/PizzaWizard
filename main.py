from get_inredients_dic import get_inredients, mesh_dics, Food
from print_ingredients_mod import print_ingredients

def command_sanitizer(command):
    dirty_command = input(f"{command}")
    command_list = dirty_command.split()
    sanitized_commands = []
    for command in command_list:
        sanitized_commands.append(command.lower().strip())
    return sanitized_commands
def creat_pizza_commands():
    print("help:        Prints this list again.")
    print("basic:       Just crust, sauce, and chees.")
    print("pepperoni:   A basic with pepperoni topping.")
    print("cheese:      It what it says on the tin, a basic with extra cheese.")
    print("dulux:       Extra pepperoni, extra chees, and extra calories.")
    print("main:        return main menue. Will ask if you want to discard.")
def true_false(command_string):
    add_command = command_sanitizer(f"{command_string} (y/n)?")
    add_true_false = True
    add_another_loop = True
    while add_another_loop:
        if add_command == "y":
            add_another_loop = False
        elif add_command == "n":
            add_true_false = False
            add_another_loop = False
        else:
            print("Invaid input.")
        
    return add_true_false
def create_pizza(current_pizza_number):
    current_pizza_number_copy = current_pizza_number
    create_pizza_loop = True
    list_of_pizza = []
    while create_pizza_loop:
        create_command = command_sanitizer("What kind of pizza do you wish for?")
        current_pizza_number_copy += 1
        if create_command[0] == "help":
            creat_pizza_commands()

        elif create_command[0] == "basic":
            list_of_pizza.append(Food.__init__(f"{current_pizza_number_copy} - basic", 2072)) 
            
        elif create_command[0] == "pepperoni":
            list_of_pizza.append(Food.__init__(f"{current_pizza_number_copy} - pepperoni", 2144))
            list_of_pizza[-1].ingredients["pepperoni"] = {
                "measurement" : "ounces",
                "amount" : 0.5
                }
            
        elif create_command[0] == "cheese":
            list_of_pizza.append(Food.__init__(f"{current_pizza_number_copy} - cheese", 2384))
            list_of_pizza[-1].ingredients["mozzarella"]["amount"] = 12
        elif create_command[0] == "dulux":
            list_of_pizza.append(Food.__init__(f"{current_pizza_number_copy} - cheese", 2528))
            list_of_pizza[-1].ingredients["pepperoni"] = {
                "measurement" : "ounces",
                "amount" : 1.0
                }
            list_of_pizza[-1].ingredients["mozzarella"]["amount"] = 12
        elif create_command[0] == "main":
            create_pizza_loop = False
            if len(list_of_pizza) > 0 :
                for pizza in list_of_pizza:
                    print(f"{pizza.name}")
                if true_false("Discard above pizza(s)?(y/n)"):
                    list_of_pizza = []
            print("Returning to main menue.")
            break
        else:
            print("Invaid command.")
            creat_pizza_commands()
    return list_of_pizza
def is_pizza(pizza_name, pizza_order):
    for pizza in pizza_order:
        
        if pizza.name== pizza_name:
            return True
    return False
def get_pizza_index(pizza_name, pizza_order):
    
    for pizza in pizza_order:
        
        if pizza.name == pizza_name:
            return pizza_order.index(pizza)

def print_pizza_order(pizza_order):
    for pizza in pizza_order:
        print(f"{pizza.name}")

def main():
    main_loop = True
    pizza_order = []
    order_tags =  {}#Used later in instrucions todo
    current_pizza_number = 0
    while main_loop:
        
        command_all = command_sanitizer("What is your command:\n")
               
        if command_all[0] == "help":
            print("Command:     Descripion.")
            print("help:        Prints all command descriptions.")
            print("add:         Adds pizza(s) to order.")
            print("remove:      Removes pizza(s) from order.")
            print("ingredients: Prints all ingredients and they're total amounts for the order.")
            print("calories:    prints total calories of order and by slice.")
        elif command_all[0] == "add":
            new_pizzas = create_pizza(current_pizza_number) #todo: add tag funcionaltiy

            if len(new_pizzas) == 0:
                
                continue
            pizza_order = pizza_order + new_pizzas
            current_pizza_number += len(new_pizzas)
            
            
        elif command_all[0] == "remove":
            if len(pizza_order) <= 0:
                print("No pizza to remove. Negative matter pizza is not alowed. Because it hurts to think about.")
                continue
            print_pizza_order(pizza_order)
            remove_loop = True
            while remove_loop:
            
                remove_command = command_sanitizer("Enter the pizza to remove.")
                if is_pizza(remove_command,pizza_order):
                    print(f"{pizza_order[remove_command].name} has been removed.")
                    pizza_order.pop(get_pizza_index(remove_command, pizza_order))

                    if true_false("Do you wish to remove another pizza"):
                        continue
                    else:
                        remove_loop = False
                else:
                    print("There is no such pizza in your order. Pizza names must be typed exactly.(remmber: ctrl c/v does not work in a Terminal.)")
            
        elif command_all[0] == "ingredients":
            pizza_ingredints = {}
            if len(pizza_order) == 0:
                print("the main ingredint of nothing is nothing.")
                continue
            for pizza in pizza_order:
                pizza_ingredints = mesh_dics(pizza_ingredints, pizza.ingredints)
            print_ingredients(pizza_ingredints)
        elif command_all[0] == "calories":
            total_order_cal = 0
            if len(pizza_order) <= 0: 
                print("Zer0, zelch, nada, calories.")
            else:
                for pizza in pizza_order:
                    total_order_cal += pizza.calories
                print(f"{total_order_cal} calories.")
        else:
            print("Invalid Command.")
    
    """
    print(f"You will need gather the fallowing reagents:")
    
    print("First you will need to make the dough\n\n")
    
    print(f"Place {(ingredients_dic["Flour"])} Cups of flour and {(ingredients_dic["Salt"] / 2)} tsp of salt into the mixing bowl.")
    print(f"In a another bowl whisk together {2 * (ingredients_dic["Water"] /3 )} cups of warm watter, {ingredients_dic['Yeast']} tsp of yeast, and {ingredients_dic['Sugar']} tsp of sugar. Cover and allow to rest for 5 minutes")
    print("After 5 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a funeral and try again.")
    print(f"If all is well then pour the yeast mix and {(ingredients_dic["Olive Oil"] / 3) * 2} tbsp of Olive Oil into the flour bowl and mix/knead untill the dough has no lumps and is pulling away form the sides of the blowl")
    print("Let the dough rise for 30 minutes to 4 hours, depending on how patient/hungry you are.")
    print("Remember to cover the dough as it rising to keep it forme drying out and\or become sentient")
    print("Sentient dough is very annoying to work with and adds a stong note of philosophical dread to the pizza, but is still usable.\n")

    print("While the dough is rising let start on the sauce.\n")

    print(f"Into a bolw, pour {(ingredients_dic['Water'] / 3)} cups of water and {ingredients_dic['Olive Oil'] / 3} tbsp of Olive Oil.")
    print("Add to the bolw the Salt, Oreagano, Basil, Black Pepper (remember: Pepper, not Powder), Garlic Pouder, Rosemary, and Tomato Paste")
    print("Whisk the bolw's contents untile evenly mixed and then set aside.\n")

    print("Before start to work on the dough, a bit of prep is need to avoid tragedy.")
    print("Pick a area in your kitchen/lab/workshop, then lay down some parchment paper (you tape down the edges to previent the paper form moving). this will make dough work/cleanup much les painful.")
    print("Spray the baking/paizza sheet with none sick spray. This will previent the pizza from welding it self to the sheet.\n")
    if ingredients_dic["number of pizza"] == 1:
        print("When the dough has risen to your satisfaction and\or limits of your patience, remove the dough form the mixing bowl and place onto a clean surface\n")
    else:
        print(f"When the dough has risen to your satisfaction and\or limits of your patience,\nRemove the dough form the mixing bowl.\ndivide the dough into {ingredients_dic['number of pizza']} pieces and place onto a clean surface")
    print("With rollingpin (a empty bottle that haves flat sides can work) roll the dough untile it fills cooking/pizza sheet.")
    print("Place the the rolled out dough onto the baking/paizza sheet.")
    if ingredients_dic["number of pizza"] > 1:
        print(f"repet for the other {ingredients_dic["number of pizza"]} doughs.")
    print("\n")

    print("Preheat you oven/oven analogue to 450* F.")
    print("Grab the pizza sauce you made earlier. Spread the sauce evanly over the dough to the edge of the pizza.")
    print("Spread the Mozzarella over the sauce.")
    print("Bake for 13-17 mins and enjoy.")
    
    """

main()