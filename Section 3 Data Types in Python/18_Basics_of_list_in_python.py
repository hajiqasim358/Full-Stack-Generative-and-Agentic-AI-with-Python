## List == Array. they are mutable, ordered, and can contain duplicate elements.

ingredients = ["water", "Milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")

spice_options = ["ginger", "cardimom"]
chai_ingredients = ["water", "milk"]

# extend
chai_ingredients.extend(spice_options)
print(f"Chai ingredients after adding spices: {chai_ingredients}")

# insert
chai_ingredients.insert(2, "Black tea")
print(f"chai: {chai_ingredients}")
# Pop
last_added = chai_ingredients.pop()
print(f"Last added ingredient: {last_added}")

chai_ingredients.sort()
print(f"sorted chai ingredients: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"maximum sugar level: {max(sugar_levels)}")
print(f"minimum sugar level: {min(sugar_levels)}")