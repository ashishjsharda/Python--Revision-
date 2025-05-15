# Splitting a string into a list
text = "apple,banana,orange"
fruits = text.split(",")  # ["apple", "banana", "orange"]

# Split with maximum number of splits
text = "apple,banana,orange,grape"
fruits = text.split(",", 2)  # ["apple", "banana", "orange,grape"]

# Split on whitespace (default)
sentence = "Python is amazing"
words = sentence.split()  # ["Python", "is", "amazing"]

# Joining a list into a string
fruits = ["apple", "banana", "orange"]
text = ", ".join(fruits)  # "apple, banana, orange"

# Join with different delimiters
text = " | ".join(fruits)  # "apple | banana | orange"
text = "".join(fruits)     # "applebananaorange"
