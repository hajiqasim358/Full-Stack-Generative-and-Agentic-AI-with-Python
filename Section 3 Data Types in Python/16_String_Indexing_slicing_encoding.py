
## String has (core, indexing, slicing, encoding and decoding)
chai_type = "Ginger Chai"
customer_name = "John Doe"
print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word {chai_description[0:8]}") # Slicing
print(f"First word {chai_description[0:8:2]}") # slicing with step
print(f"first word {chai_description[:8]}") # slicing with default start index
print(f"last word {chai_description[9:]}") # slicing with default end index
print(f"last word {chai_description[::-1]}") #  slicing with negative step (reversing the string)


# Text encodings and decodings
label_text = "Café"
encoded_text = label_text.encode("utf-8")
print(f"Encoded text: {encoded_text}")
print(f"Non encoded text: {label_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")

