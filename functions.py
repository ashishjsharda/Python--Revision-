# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

# Function with multiple parameters
def add(a, b):
    return a + b

# Function with *args (variable positional arguments)
def sum_all(*numbers):
    return sum(numbers)

# Function with **kwargs (variable keyword arguments)
def create_profile(**details):
    return details

# Combining parameters
def mixed_args(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# Examples of calling these functions
print(greet("Alice"))  # "Hello, Alice!"
print(greet_with_default())  # "Hello, Guest!"
print(greet_with_default("Bob"))  # "Hello, Bob!"
print(add(5, 3))  # 8
print(sum_all(1, 2, 3, 4, 5))  # 15
print(create_profile(name="Alice", age=25, city="New York"))  # {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(create_profile(name="Bob", hobby="reading",age=30,city="Charlotte"))  # {'name': 'Bob', 'hobby': 'reading'}
mixed_args(1, 2, 3, 4, 5, name="Alice", city="New York")
