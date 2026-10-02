# integer

black_tea_grams = 14
ginger_grams = 3
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining grams of tea: {remaining_tea}")

## Division
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

base_floavour_strength = 2
scale_factor = 3
powerful_flavour = base_floavour_strength ** scale_factor
print(f"scaled flavour strength: {powerful_flavour}")

total_tea_harvested = 1_000_000_000
print(f"Total tea harvested: {total_tea_harvested}")


## Boolean

is_boiling = True
stir_count = 5
total_actions = is_boiling + is_boiling # Upcasting boolean to integer (True = 1, False = 0)
print(f"Total actions: {total_actions}")

milk_present = 0 # No milk present
print(f"Is there milk? {bool(milk_present)}") # Upcasting integer to boolean (0 = False, any non-zero = True)


# Logical Operations 
water_hot = True
tea_added = True

can_server = water_hot and tea_added


## Floating point Numbers OR Decimal Numbers
ideal_lamp = 95.5
current_lamp = 90.2
print(f"Ideal temp {ideal_lamp}")
print(f"Current temp {current_lamp}")
print(f"Difference in temp {ideal_lamp - current_lamp}")

import sys
print(sys.float_info) # This will print the precision and range of floating point numbers in Python


