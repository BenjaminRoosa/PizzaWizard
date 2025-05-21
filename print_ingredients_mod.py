
def print_ingredients(ingredients):
    
    for ingredient in ingredients:
        print(f"{ingredient["amount"]} {ingredient["measurement"]}--{ingredient}.")
def get_inredients(pizza_order):
    ingredients = {}
    if len(pizza_order) == 0:
        print("the main ingredint of nothing is nothing.")
        ingredients = {
            "Nothing": {
                "measurement" : "nills",
                "amount" : 0
            }
        }
    elif len(pizza_order) == 1:
        ingredients = pizza_order[0].ingredients
    else:
        for pizza in pizza_order:
                    ingredients = mesh_dics(ingredients, pizza.ingredients)
    return ingredients
def get_tags(pizza_order):
    tags = {}
    for pizza in pizza_order:
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
def print_intsturctions(pizza_order):
    pizza_tags = get_tags(pizza_order)
    pizza_ingredients = get_inredients(pizza_order)
    print("First you will need to make the dough\n\n")
    
    print("Place flour and salt into a mixing bowl.")
    print(f"In a another bowl whisk together the {pizza_ingredients["water"]["amount"] / 3.0 * 2.0} cups warm watter, yeast, and sugar. Cover and allow to rest for 5 minutes.")
    print("After 5-10 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a Viking funeral and try again.")
    print(f"If all is well then pour in the yeast mix and {pizza_ingredients["olive oil"]["amount"]/3.0 * 2.0} teaspoons of Olive Oil, and {pizza_ingredients["salt"]["amount"]/3.0} teaspoons of slat into the flour bowl and mix/knead untill the dough has no lumps and is pulling away form the sides of the blowl.")
    print("Let the dough rise for 30 minutes to 4 hours, depending on how patient/hungry you are.")
    print("Remember to cover the dough as it rising to keep it forme drying out and\or become sentient.")
    print("Sentient dough is still usable, but very annoying to work with and adds a stong note of existential dread to the pizza.\n")

    print("While the dough is rising let start on the sauce.\n")

    print(f"Into a bolw, add {pizza_ingredients["water"]["amount"] / 3.0} cups warm watter and Olive Oil.")
    print("Add to the bolw the Salt, Oreagano, Basil, Black Pepper (remember: Pepper, not Powder), Garlic Pouder, Rosemary, and Tomato Paste")
    print("Whisk the bolw's contents untile no clumps of tomato past remain then set aside.\n")

    print("Before start to work on the dough, a bit of prep is need to avoid tragedy.")
    print("Pick a area in your kitchen/lab/workshop, then lay down some parchment paper (you can tape down the edges to previent the paper form moving). this will make work/clean-up much les painful.")
    print("Spray the baking/paizza sheet with none sick spray. This will previent the pizza from welding it self to the sheet.\n")
    if len(pizza_order) == 1:
        print("When the dough has risen to your satisfaction and\or limits of your patience, remove the dough form the mixing bowl and place onto a clean surface\n")
    else:
        print(f"When the dough has risen to your satisfaction and\or limits of your patience,\nRemove the dough form the mixing bowl.\nDivide the dough into {len(pizza_order)} pieces and place onto a clean, oiled surface")
    print("With rollingpin (a empty wine bottle can work in a pinch) roll the dough untile it can fill out your baking/pizza sheet.")
    print("Place the the rolled out dough onto the baking/paizza sheet.")
    if len(pizza_order) > 1:
        print(f"repet for the other {len(pizza_order)} doughs.")
    print("\n")

    print("Preheat you oven/oven analogue to 450* F, 232* C.")
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