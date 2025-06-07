from get_inredients_dic import  Order, command_sanitizer
from print_ingredients_mod import print_intsturctions


def creat_pizza_commands():
    print("help:        Prints create pizza command list.")
    print("basic:       Just crust, sauce, and cheese.")
    print("pepperoni:   A basic with pepperoni topping.")
    print("cheese:      It what it says on the tin, a basic with extra cheese.")
    print("dulux:       Extra pepperoni, extra chees, and extra calories.")
    print("main:        return main menue. Will ask if you want to discard.")





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
            main_order.remove_pizza()
            
        elif command_all[0] == "ingredients":
            main_order.print_ingredients()
        elif command_all[0] == "calories":
            main_order.print_calories()
        elif command_all[0] == "instuctions":
            print_intsturctions(main_order)
        
        elif command_all[0] == "exit":
            main_loop = False
        
        else:
            print("Invalid Command.")
    

    print("Enjoy your piazza mage. Just remmber to eat/dispose BEFORE they pupate.")
main()