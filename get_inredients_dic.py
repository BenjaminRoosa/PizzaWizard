


def get_inredients(food):
    total_base_ingredients =   {}
    if "basic_ingredient" in food.note:
        total_base_ingredients[food.name] = food
        return total_base_ingredients
    for ingredient in food.ingredients:
        if "basic_ingredient" in ingredient.note:
            if ingredient.name in total_base_ingredients:
                pass
        else:
            #meash to dics
            pass
    return total_base_ingredients