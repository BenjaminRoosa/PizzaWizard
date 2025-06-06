from get_inredients_dic import  Order
from print_ingredients_mod import print_ingredients ,print_intsturctions, get_inredients


def creat_pizza_commands():
    print("help:        Prints create pizza command list.")
    print("basic:       Just crust, sauce, and cheese.")
    print("pepperoni:   A basic with pepperoni topping.")
    print("cheese:      It what it says on the tin, a basic with extra cheese.")
    print("dulux:       Extra pepperoni, extra chees, and extra calories.")
    print("main:        return main menue. Will ask if you want to discard.")

def get_pizza_index(pizza_name, pizza_order):
    
    for pizza in pizza_order:
        
        if pizza.name == pizza_name:
            return pizza_order.index(pizza)



def main():
    main_loop = True
    main_order = Order
    
    
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
            main_order.create_pizza()
            
        elif command_all[0] == "remove":
            
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