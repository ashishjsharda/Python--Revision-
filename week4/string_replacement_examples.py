text = "Hello, World!"
new_text = text.replace("World", "Python")  # "Hello, Python!"

# Replace with count limitation
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2)  # "orange orange apple"

# Chaining replacements
text = "Hello, World!"
new_text = text.replace("H", "J").replace("World", "Python")  # "Jello, Python!"
