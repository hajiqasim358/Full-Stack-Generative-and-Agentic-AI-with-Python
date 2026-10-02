# taking the input form the user
preferred_snack = input("Enter your preferred snack: ").lower()

# checking if the preferred snack is either "chips" or "chocolate"
if preferred_snack == "chips" or preferred_snack == "chocolate":
    print(f"You have selected {preferred_snack}. Enjoy your snack!")
else:
    print(f"Sorry, we don't have {preferred_snack}. Please choose either 'chips' or 'chocolate'.")

