from get_inredients_dic import get_inredients
from print_ingredients_mod import print_ingredients
def main():
    
    ingredients_dic = get_inredients()
    print_ingredients(ingredients_dic)
    print("First you will need to make the dough")
    
    print(f"Place {(ingredients_dic["flour"])} Cups of flour and {(ingredients_dic["salt"] / 2)} tsp of salt into the mixing bowl.\n")
    print(f"In a another bowl whisk together {2 * (ingredients_dic["water"] /3)} cups of warm watter, {ingredients_dic['Yeast']} tsp of yeast, and {ingredients_dic['sugar']} tsp of sugar. Cover and allow to rest for 5 minutes\n")
    print("After 5 minutes the Yeast bowl should be toped with foam. If it is not, your yeast is dead. Give the yeast a funeral and try again.\n")
    print(f"If all is well then pour the yeast mix and {ingredients_dic['olive oil'] / 2} into the flour bowl and mix/knead (think of the dough as flour mud) untill the dough has no lumps and is pulling away form the sides of the blowl")
    
main()