## Tuuples Represented by Parentheses ()
## They are immutable (cannot be changed) and ordered collection of elements.

masala_spices = ("cardimom", "cloves", "cinnamoon")

(spice1, spice2, spice3) = masala_spices
print(f"main masala spices: {spice1}, {spice2}, {spice3}")
ginger_ratio, cardimom_ratio = 2, 1
print(f"ration of G: {ginger_ratio}, C: {cardimom_ratio}")


# Membership Testing
print(f"Is cardimom in masala spices? {'cardimom' in masala_spices}")