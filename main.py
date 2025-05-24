from get_inredients_dic import  Food
from print_ingredients_mod import print_ingredients ,print_intsturctions, get_inredients

def command_sanitizer(command):
    dirty_command = input(f"{command}")
    command_list = dirty_command.split()
    sanitized_commands = []
    for command in command_list:
        sanitized_commands.append(command.lower().strip())
    return sanitized_commands
def creat_pizza_commands():
    print("help:        Prints create pizza command list.")
    print("basic:       Just crust, sauce, and cheese.")
    print("pepperoni:   A basic with pepperoni topping.")
    print("cheese:      It what it says on the tin, a basic with extra cheese.")
    print("dulux:       Extra pepperoni, extra chees, and extra calories.")
    print("main:        return main menue. Will ask if you want to discard.")
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
        
    
def create_pizza(current_pizza_number):
    current_pizza_number_copy = current_pizza_number
    create_pizza_loop = True
    list_of_pizza = []
    while create_pizza_loop:
        create_command = command_sanitizer("What kind of pizza do you wish for?\n")
        current_pizza_number_copy += 1
        if create_command[0] == "help":
            creat_pizza_commands()

        elif create_command[0] == "basic":
            pizza_name = f"{current_pizza_number_copy} - basic"
            list_of_pizza.append(Food(pizza_name), 2072)
            
            
        elif create_command[0] == "pepperoni":
            pizza_name = f"{current_pizza_number_copy} - pepperoni"
            list_of_pizza.append(Food(pizza_name, 2144))
            
            list_of_pizza[-1].ingredients["pepperoni"] = {
                "measurement" : "ounces",
                "amount" : 0.5
                }
            list_of_pizza[-1].tags = ["pepperoni"]
        elif create_command[0] == "cheese":
            list_of_pizza.append(Food(f"{current_pizza_number_copy} - cheese", 2384))
            
            list_of_pizza[-1].ingredients["mozzarella"]["amount"] = 12
            list_of_pizza[-1].tags = ["extra cheese"]
        elif create_command[0] == "dulux":
            list_of_pizza.append(Food(f"{current_pizza_number_copy} - dulux", 2528))
            list_of_pizza[-1].ingredients["pepperoni"] = {
                "measurement" : "ounces",
                "amount" : 1.0
                }
            list_of_pizza[-1].ingredients["mozzarella"]["amount"] = 12
            list_of_pizza[-1].tags = ["pepperoni","extra cheese"]
        elif create_command[0] == "main":
            
            create_pizza_loop = False
            if len(list_of_pizza) > 0 :
                for pizza in list_of_pizza:
                    print(f"{pizza.name}")
                if true_false("Save above pizza(s)?(y/n)"):
                    pass
                else:
                    list_of_pizza = []
            print("Returning to main menue.")
        else:
            print("Invaid command.")
            creat_pizza_commands()
    return list_of_pizza
def is_pizza(pizza_name, pizza_order):
    pizza_name_lst = []
    for pizza in pizza_order:
        pizza_name_lst.append(pizza.name)
     
    if pizza_name in pizza_name_lst:
        return True
    else:
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
            print("exit:        exits program.")
        
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
                if is_pizza(remove_command[0],pizza_order):
                    print(f"{pizza_order[remove_command].name[0]} has been removed.")
                    pizza_order.pop(get_pizza_index(remove_command, pizza_order))

                    if len(pizza_order) > 0:
                        if true_false("Do you wish to remove another pizza"):
                            continue
                        else:
                            remove_loop = False
                else:
                    print("There is no such pizza in your order. Pizza names must be typed exactly.(remmber: ctrl c/v does not work in a Terminal.)")
            
        elif command_all[0] == "ingredients":
            pizza_ingredients = get_inredients(pizza_order)
            
                
            print_ingredients(pizza_ingredients)
        elif command_all[0] == "calories":
            total_order_cal = 0
            if len(pizza_order) <= 0: 
                print("Zer0, zelch, nada, calories.")
            else:
                for pizza in pizza_order:
                    total_order_cal += pizza.calories
                print(f"{total_order_cal} calories.")
        elif command_all[0] == "instuctions":
            print_intsturctions(pizza_order)
        
        elif command_all[0] == "exit":
            main_loop = False
        
        else:
            print("Invalid Command.")
    

    print("Enjoy your piazza mage. Just remmber to eat/dispose BEFORE they pupate.")
main()