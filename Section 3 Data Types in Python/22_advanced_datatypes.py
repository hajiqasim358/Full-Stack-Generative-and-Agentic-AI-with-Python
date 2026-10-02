# Use Python's built-in datetime module for date handling.
import arrow

# Create a date object using arrow
date = arrow.get('2023-06-15')
print(date)  # Output: 2023-06-15T00:00:00+00:00

# Format the date in different formats
print(date.format('YYYY-MM-DD'))  # Output: 2023-06-15
print(date.format('DD/MM/YYYY'))  # Output: 15/06/2023

# Get the current date and time
current_date = arrow.now()
print(current_date) # Output: Current date and time in ISO format

# Get the current date and time in a specific timezone
current_date_tz = arrow.now("Asia/Karachi")
print(f"Current date and time in Asia/Karachi: {current_date_tz}")   # Output: Current date and time in the specified timezone

