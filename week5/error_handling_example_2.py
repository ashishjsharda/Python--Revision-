def get_safe_division_input():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        return result
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    return None  

output = get_safe_division_input()
if output is not None:
    print(f"Result is: {output}")
