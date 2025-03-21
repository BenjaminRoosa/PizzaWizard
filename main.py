from get_inredients_dic import get_inredients
from print_ingredients_mod import print_ingredients

class Food:
    def __init__(self, name,sev_weight, amount, calories, note):
        self.name = name
        #all measurements are by weight
        self.sev_whight = sev_weight
        self.amount = amount
        self.calories = calories
        
        self.note = note
        self.ingredients = {}
        
    def add_ingredient(self, ingredient, amount):
        if amount <= 0:
            if amount == 0:
                print(f"Nothing added")
                return
            else:
                amount = abs(amount)
                self.remove_ingredient(ingredient, amount)
                return
        if ingredient.name in self.ingredients.keys():
            self.ingredients[ingredient.name].amount += amount
        
        else:
            self.ingredients[ingredient.name] = ingredient 
            self.ingredients[ingredient.name].amount = amount
        self.calories += ingredient.calories * amount

        print(f"Added {amount} sevings of {ingredient.name}")
        

    def remove_ingredient(self, ingredient, amount):
        if amount <= 0:
            if amount == 0:
                print(f"Nothing removed")
                return
            else:
                amount = abs(amount)
                self.add_ingredient(ingredient, amount)
                return
        if ingredient.name not in self.ingredients.keys():
            print(f"This pizza is allready devoid of {ingredient.name}")

            return
        
        if self.ingredients[ingredient.name].amount - amount < 1:
            self.calories -= self.ingredients[ingredient.name].amount * ingredient.calories
            del self.ingredients[ingredient.name]
            print(f"All sevings of {ingredient.name} have been removed")
                
        else:
            self.calories -= ingredient.calories * amount
            self.ingredients[ingredient.name].amount -= amount
            print(f"{amount} sevings of {ingredient.name} have been removed")
        

    def inpect_ingredient(self, ingredient_name):
        if ingredient_name not in self.ingredients.keys():
            print(f"{ingredient_name} is not present")
            return
        
        print(f"-Name: {ingredient_name.name}\n")
        
        
        print(f"-Serving weight: {ingredient_name.sev_whight}")
        print(f"-Calories per serving: {ingredient_name.calories}")
        print(f"-Number of servings: {ingredient_name.amount}")
        if ingredient_name.note != "":
            print(f"{ingredient_name.note}")


def main():
    number_of_pizzas = int(input("What is the number of pizzas you wish to summon today?:\n"))
    ingredients_dic = get_inredients()
    print(f"You will need gather the fallowing reagents:")
    print_ingredients(ingredients_dic)
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
    


main()