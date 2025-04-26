def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]
    
# Test case
print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 4, 6, 8, 10]
