def filter_even(numbers):
    def is_even(x):
        return x % 2 == 0
    return list(filter(is_even, numbers))

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
