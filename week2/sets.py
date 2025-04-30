fruits = {"apple", "banana", "cherry"}
even_numbers = {2, 4, 6, 8, 10}
# Note: {} creates an empty dictionary, not an empty set
empty_set = set()
# Adding and removing elements
fruits.add("orange")
fruits.remove("banana") # Raises KeyError if element doesn't exist
fruits.discard("kiwi") # No error if element doesn't exist
# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union = set_a | set_b # or set_a.union(set_b)
intersection = set_a & set_b # or set_a.intersection(set_b)
difference = set_a - set_b # or set_a.difference(set_b)
symmetric_difference = set_a ^ set_b # or set_a.symmetric_difference(set_b)
# Set comprehensions
squares = {x**2 for x in range(10)}
