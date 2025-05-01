colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)
 # Indexing (positive and negative)
first_color = colors[0]  # "red"
last_color = colors[-1]  # "blue"
# Tuple unpacking
r, g, b = colors
r,g=g,r
print(r)
print(g)

first, second, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(second)  # 2
print(rest)  # [3, 4, 5]

 
