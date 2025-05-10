def analyze_lists_with_lists(list1, list2):
    common = []
    unique_to_list1 = []
    unique_to_list2 = []
    
    # Find common elements and elements unique to list1
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
        elif item not in list2 and item not in unique_to_list1:
            unique_to_list1.append(item)
    
    # Find elements unique to list2
    for item in list2:
        if item not in list1 and item not in unique_to_list2:
            unique_to_list2.append(item)
    
    return (common, unique_to_list1, unique_to_list2)
