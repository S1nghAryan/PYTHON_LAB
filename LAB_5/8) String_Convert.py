def convert_to_strings(int_list, int_tuple):
    # Convert the list of integers to a list of strings
    string_list = list(map(str, int_list))
    
    # Convert the tuple of integers to a list of strings
    string_tuple = list(map(str, int_tuple))
    
    return string_list, string_tuple

# Test the function
int_list = [1, 2, 3, 4, 5]
int_tuple = (6, 7, 8, 9, 10)
string_list_result, string_tuple_result = convert_to_strings(int_list, int_tuple)
print("List of strings:", string_list_result)  # Output: List of strings: ['1', '2', '3', '4', '5']
print("Tuple of strings:", string_tuple_result)  # Output: Tuple of strings: ['6', '7', '8', '9', '10']