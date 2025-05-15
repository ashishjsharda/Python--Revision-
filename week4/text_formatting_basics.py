word = "Python "
repeated = word * 3  # "Python Python Python "

# Creating patterns
line = "-" * 30  # Creates a line of 30 dashes: "------------------------------"

# Creating formatted output
headers = ["Name", "Age", "Country"]
formatted = " | ".join(headers)
separator = "-" * len(formatted)
print(formatted)  # "Name | Age | Country"
print(separator)  # "--------------------"

# Practical example: Creating a simple text box
def create_box(text):
    border = "+" + "-" * (len(text) + 2) + "+"
    content = "| " + text + " |"
    return "\n".join([border, content, border])

print(create_box("Hello"))
# Output:
# +-------+
# | Hello |
# +-------+
