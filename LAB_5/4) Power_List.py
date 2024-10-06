def power_list(base, n):
    return list(map(lambda x: base ** x, range(1, n + 1)))

# Test the function
base = 2
n = 5
result = power_list(base, n)
print(result)  # Output: [2, 4, 8, 16, 32]