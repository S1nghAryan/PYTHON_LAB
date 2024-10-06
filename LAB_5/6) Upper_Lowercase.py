def convert_and_eliminate_duplicates(sequence):
    # Convert to uppercase and eliminate duplicates
    uppercase_sequence = list(set(map(lambda x: x.upper(), sequence)))
    
    # Convert to lowercase and eliminate duplicates
    lowercase_sequence = list(set(map(lambda x: x.lower(), sequence)))
    
    return uppercase_sequence, lowercase_sequence

# Test the function
sequence = "Hello World"
uppercase_result, lowercase_result = convert_and_eliminate_duplicates(sequence)
print("Uppercase:", uppercase_result)  # Output: Uppercase: ['H', 'E', 'L', 'O', 'W', 'R', 'D']
print("Lowercase:", lowercase_result)  # Output: Lowercase: ['h', 'e', 'l', 'o', 'w', 'r', 'd']