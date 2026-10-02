# Sets in python
# Sets are unordered collections of unique elements. They are mutable, meaning you can add or remove elements from a set after its creation. Sets are defined using curly braces {} or the set() constructor.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(f"My set: {my_set}")

# Adding elements to a set
my_set.add(6)
print(f"Set after adding an element: {my_set}")

# Removing elements from a set
my_set.remove(3)
print(f"Set after removing an element: {my_set}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Intersection
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2: {difference_set}")

# set operations without using methods
# Union
union_set2 = set1 | set2
print(f"Union of set1 and set2 (using | operator): {union_set2}")

# Intersection
intersection_set2 = set1 & set2
print(f"Intersection of set1 and set2 (using & operator): {intersection_set2}")

# Difference
difference_set2 = set1 - set2
print(f"Difference of set1 and set2 (using - operator): {difference_set2}")

