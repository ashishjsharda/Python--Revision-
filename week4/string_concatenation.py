first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"

# Concatenating multiple strings
greeting = "Hello, " + first_name + " " + last_name + "!"  # "Hello, John Doe!"

# Alternative using join (more efficient for multiple strings)
message_parts = ["Hello", first_name, last_name, "Welcome!"]
message = " ".join(message_parts)  # "Hello John Doe Welcome!"

# You cannot concatenate strings with other types directly
age = 30
# This will cause an error:
# message = "Age: " + age  # TypeError: can only concatenate str (not "int") to str

# Convert non-string types to strings first
message = "Age: " + str(age)  # "Age: 30"
