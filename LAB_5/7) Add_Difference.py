def add_and_find_difference(list1, list2):
    # Add the two lists
    added_list = list(map(lambda x, y: x + y, list1, list2))
    
    # Find the difference between the two lists
    difference_list = list(map(lambda x, y: abs(x - y), list1, list2))
    
    return added_list, difference_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
added_result, difference_result = add_and_find_difference(list1, list2)
print("Added list:", added_result)  # Output: Added list: [6, 6, 6, 6, 6]
print("Difference list:", difference_result)  # Output: Difference list: [4, 2, 0, 2, 4]