def sum_array_elements(array):
    # Compute the sum of elements using map
    sum_of_elements = sum(map(lambda x: x, array))
    
    return sum_of_elements

# Test the function
array = [1, 2, 3, 4, 5]
result = sum_array_elements(array)
print(result)  # Output: 15