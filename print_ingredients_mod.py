
def print_ingredients(ingredients):
    
    for ingredient in ingredients:
        print(f"{ingredient["amount"]} {ingredient["measurement"]}--{ingredient}.")

def print_intsturctions(order):

    
    
    
    print(f"You will need gather the following reagents:")

    print_ingredients(order_ingredients)
    
    print("First you will need to make the dough\n\n")
    
    print("Place flour and salt into a mixing bowl.")
    print("In a another bowl whisk together the warm watter, yeast, and sugar. Cover and allow to rest for 5 minutes.")
    print("After 5 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a Viking funeral and try again.")
    print("If all is well then pour in the yeast mix and Olive Oil into the flour bowl and mix/knead untill the dough has no lumps and is pulling away form the sides of the blowl.")
    print("Let the dough rise for 30 minutes to 4 hours, depending on how patient/hungry you are.")
    print("Remember to cover the dough as it rising to keep it forme drying out and\or become sentient.")
    print("Sentient dough is very annoying to work with and adds a stong note of philosophical dread to the pizza, but is still usable.\n")

    print("While the dough is rising let start on the sauce.\n")

    print("Into a bolw, pour water and {ingredients_dic['Olive Oil'] / 3} tbsp of Olive Oil.")
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