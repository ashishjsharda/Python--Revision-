# Creating tuples
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)

# Indexing (positive and negative)
first_color = colors[0]  # "red"
last_color = colors[-1]  # "blue"

# Tuple unpacking
r, g, b = colors

# Empty and singleton tuples
empty = ()
singleton = (42,)  # Note the comma is needed for single-element tuples

# Tuple methods
colors = ("red", "green", "blue", "red", "yellow")
red_count = colors.count("red")  # 2
green_index = colors.index("green")  # 1

# Nested tuples
nested = ((1, 2), (3, 4))
