# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]

# Indexing (positive and negative)
first_fruit = fruits[0]  # "apple"
last_fruit = fruits[-1]  # "cherry"

# Slicing
subset = fruits[0:2]  # ["apple", "banana"]

# Common operations
fruits.append("orange")  # Add one element
fruits.extend(["kiwi", "mango"])  # Add multiple elements
fruits.insert(1, "pear")  # Insert at specific position
fruits.remove("banana")  # Remove by value
popped_fruit = fruits.pop()  # Remove and return last element
fruits.sort()  # Sort in-place
fruits.reverse()  # Reverse in-place

# List comprehensions
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_nums = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
