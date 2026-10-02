seat_type = input("Enter seat type (Sleeper, AC, General, Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available.")
    case "ac":
        print("AC - Air-conditioned, comfortable seating.")
    case "general":
        print("General - Basic seating, Cheapest option.")
    case "luxury":
        print("Luxury - premium seats with meals.")
    case _:
        print("Invalid seat type. Please choose from Sleeper, AC, General, or Luxury.")