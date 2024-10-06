def create_new_list(tuple_elements, string_value):
    # Convert the string value to an integer
    int_value = int(string_value)
    
    # Create a new list taking specific elements from the tuple
    new_list = list(map(lambda x: x, (tuple_elements[0], tuple_elements[2], int_value)))
    
    return new_list

# Test the function
tuple_elements = (10, 20, 30, 40, 50)
string_value = "60"
result = create_new_list(tuple_elements, string_value)
print(result)  # Output: [10, 30, 60]