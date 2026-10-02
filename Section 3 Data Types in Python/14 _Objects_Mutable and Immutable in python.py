sugar_amount = 100
print(f"Initial Sugar Amount: {sugar_amount}")

sugar_amount = 150
print(f"Updated Sugar Amount: {sugar_amount}")
print(f"ID of 150: {id(150)}")
print(f"ID of 100: {id(100)}")

# As of that we conclude that, the values are immutable (Not changable ) and when we update the value of sugar_amount,
# it creates a new object in memory with the new value (150) and assigns it to the variable sugar_amount.
# The old value (100) still exists in memory but is not referenced by the variable anymore.

