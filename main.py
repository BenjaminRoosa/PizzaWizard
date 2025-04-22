from get_inredients_dic import get_inredients, create_oreder, Food
from print_ingredients_mod import print_ingredients

def command_sanitizer(command):
    command_list = command.split()
    sanitized_commands = []
    for command in command_list:
        sanitized_commands.append(command.lower().strip())
    return sanitized_commands
def create_pizza(current_pizza_number):
    new_pizza = Food.__init__(f"{current_pizza_number}", 2072)
    new_pizza.ingredients = {
        "flour" : {
            "measurement" : "cups",
            "amount" : 3
        },
        "water" : {
            "measurement" : "cups",
            "amount" : 1.5
        },
        "mozzarella" :{
            "measurement" : "oz",
            "amount" : 8
        },
        "salt" : {
            "measurement" : "tsp",
            "amount" : 1.5
        },
        "olive oil": {
            "measurement" : "tsp",
            "amount" : 1.5
        },
        "tomato paste": {
            "measurement" : "oz",
            "amount" : 3
        },
        "black pepper": {
            "measurement" : "tsp",
            "amount" : 0.5
        },
        "garlic clove": {
            "measurement" : "grams",
            "amount" : 3
        },
        "rosemary": {
            "measurement" : "tsp",
            "amount" : 0.5
        },
        "basil": {
            "measurement" : "tsp",
            "amount" : 1
        },
        "oregano": {
            "measurement" : "tsp",
            "amount" : 1
        },
        "sugar": {
            "measurement" : "tsp",
            "amount" : 1
        }
    }
def is_pi
def main():
    main_loop = True
    pizza_order = []
    current_pizza_number = 0
    while main_loop:
        dirty_command = input("What is your command:\n")
        command_all = command_sanitizer(dirty_command)
        
        pizza_name_lst = []
                
        if command_all[0] == "help":
            print("Command: descripion.")
            print("help:    prints all command descriptions.")
            print("add:     opens pizza maker.")
            print("remove:  opens pizza remover. For removing individual")
            print("modify:  opens pizza modifier")
        elif command_all[0] == "add":
            new_pizza = create_pizza(current_pizza_number)
            pizza_order.append(new_pizza)
            current_pizza_number += 1
            pizza_name_lst.append(new_pizza.name)
            print("pizza added.")
        elif command_all[0] == "remove":
            #todo: move this command to it own function.
            
            remove_loop = True
            while remove_loop:
            
                pizza_to_remove = command_sanitizer(input("Enter the number of the pizza to remove. cancel to cancel."))
                if pizza_to_remove in pizza_name_lst:
                    remove_index = pizza_name_lst.index(pizza_to_remove)
                    pizza_order.pop(remove_index)
                    remove_another = command_sanitizer(input("Would you like to remove another pizza?(y/n)"))
                    if remove_another == "y":
                        continue
                    else:
                        remove_loop = False
                elif pizza_to_remove == "cancel":
                    remove_loop = False
                else:
                    print("No pizza with that number.")

        elif command_all[0] == "modify":
            mod_loop = True
            while mod_loop:
                mod_command = command_sanitizer(input("Enter the number of pizza to modify"))
                if mod_command in pizza_name_lst:

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