cup_size = input("Choose your cup size (small, medium, large): ").lower()
if cup_size == "small":
    print("You have selected a small cup. The price is $2.00.")
elif cup_size == "medium":
    print("You have selected a medium cup. The price is $3.00.")
elif cup_size == "large":
    print("You have selected a large cup. The price is $4.00.")
else:
    print("Invalid cup size selected. Please choose small, medium, or large.")