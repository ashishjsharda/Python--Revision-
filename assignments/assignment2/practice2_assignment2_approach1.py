def analyze_lists(list1, list2):
    """
    Takes two lists and returns a tuple containing:
    1. A set of elements common to both lists.
    2. A set of elements unique to the first list.
    3. A set of elements unique to the second list.
    """
    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1 & set2
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    
    return common_elements, unique_to_list1, unique_to_list2

first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]
common, unique1, unique2 = analyze_lists(first_list, second_list)
print("Common elements:", common)
print("Unique to first list:", unique1)
print("Unique to second list:", unique2)
