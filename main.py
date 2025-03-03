from get_inredients_dic import get_inredients
from print_ingredients_mod import print_ingredients
def main():
    
    ingredients_dic = get_inredients()
    print_ingredients(ingredients_dic)
    print("First you will need to make the dough\n\n")
    
    print(f"Place {(ingredients_dic["Flour"])} Cups of flour and {(ingredients_dic["Salt"] / 2)} tsp of salt into the mixing bowl.\n")
    print(f"In a another bowl whisk together {2 * (ingredients_dic["Water"] /3 )} cups of warm watter, {ingredients_dic['Yeast']} tsp of yeast, and {ingredients_dic['Sugar']} tsp of sugar. Cover and allow to rest for 5 minutes\n")
    print("After 5 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a funeral and try again.\n")
    print(f"If all is well then pour the yeast mix and {(ingredients_dic["Olive Oil"] / 3) * 2} tbsp of Olive Oil into the flour bowl and mix/knead untill the dough has no lumps and is pulling away form the sides of the blowl\n")
    print("Let the dough rise for 30 minutes to 4 hours, depending on how patient/hungry you are.\n")
    print("Remember to cover the dough as it rising to keep it forme drying out and\or become sentient\n")
    print("Sentient dough is very annoying to work with and adds a stong note of philosophical dread to the pizza, but is still usable.\n\n")

    print("While the dough is rising let start on the sauce.\n\n")

    print(f"Into a bolw, pour {(ingredients_dic['Water'] / 3)} cups of water and {ingredients_dic['Olive Oil'] / 3} tbsp of Olive Oil.\n")
    print("Add to the bolw the Salt, Oreagano, Basil, Black Pepper (remember: Pepper, not Powder), Garlic Pouder, Rosemary, and Tomato Paste\n")
    print("Whisk the bolw's contents untile evenly mixed and then set aside.\n\n")

    print("Before start to work on the dough, a bit of prep is need to avoid tragedy.\n")
    print("Pick a area in your kitchen/lab/workshop, then lay down some parchment paper (you tape down the edges to previent the paper form moving). this will make dough work/cleanup much les painful.\n")
    print("Spray the baking/paizza sheet with none sick spray. This will previent the pizza from welding it self to the sheet.\n\n")
    if ingredients_dic["number of pizza"] == 1:
        print("When the dough has risen to your satisfaction and\or limits of your patience, remove the dough form the mixing bowl and place onto a clean surface\n")
    else:
        print(f"When the dough has risen to your satisfaction and\or limits of your patience,\nremove the dough form the mixing bowl,\ndivide the dough into {ingredients_dic['number of pizza']} pieces and place onto a clean surface\n")
    print("With rollingpin (a empty bottle that haves flat sides can work) roll the dough untile it fills cooking/pizza sheet.\n")
    print("Place the the rolled out dough onto the baking/paizza sheet.\n")
    if ingredients_dic["number of pizza"] > 1:
        print(f"repet for the other {ingredients_dic["number of pizza"]} doughs.\n")
    print("\n")

    print("Preheat you oven/oven analogue to 450* F.\n")
    print("Grab the pizza sauce you made earlier. Spread the sauce evanly over the dough to the edge of the pizza.\n")
    print("Spread the Mozzarella over the sauce.\n")
    print("Bake for 13-17 mins and enjoy.\n")
    


main()