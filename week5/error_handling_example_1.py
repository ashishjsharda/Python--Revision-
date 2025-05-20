def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None  

result = safe_divide(10, 0)
if result is None:
    print("Invalid division.")
