from get_inredients_dic import get_inredients
from print_ingredients_mod import print_ingredients
def main():
    
    ingredients_dic = get_inredients()
    print_ingredients(ingredients_dic)
    print("First you will need to make the dough\n\n")
    
    print(f"Place {(ingredients_dic["Flour"])} Cups of flour and {(ingredients_dic["Salt"] / 2)} tsp of salt into the mixing bowl.\n")
    print(f"In a another bowl whisk together {2 * (ingredients_dic["Water"] /3 )} cups of warm watter, {ingredients_dic['Yeast']} tsp of yeast, and {ingredients_dic['sugar']} tsp of sugar. Cover and allow to rest for 5 minutes\n")
    print("After 5 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a funeral and try again.\n")
    print(f"If all is well then pour the yeast mix and {(ingredients_dic["Olive Oil"] / 3) * 2} tbsp of Olive Oil into the flour bowl and mix/knead untill the dough has no lumps and is pulling away form the sides of the blowl\n")
    print("Let the dough rise for 30 minutes to 4 hours, depending on how patient/hungry you are.\n")
    print("Remember to cover the dough as it rising to keep it forme drying out and\or become sentient\n")
    print("Sentient dough is very annoying to work with and adds a stong note of philosophical dread to the pizza, but is still usable.\n\n")

    print("While the dough is rising let start on the sauce.\n\n")
    print(f"Into a bolw, pour {(ingredients_dic['Water'] / 3)} cups of water and {ingredients_dic['Olive Oil'] / 3} tbsp of Olive Oil.\n")
    print("Add in the Salt, Oreagano, Basil")

main()