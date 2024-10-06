def fibonacci_squares(n):
    # Generate the first N Fibonacci numbers
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    
    # Compute the square of each Fibonacci number using map
    squares = list(map(lambda x: x ** 2, fibonacci_numbers))
    
    return squares

# Test the function
n = 10
result = fibonacci_squares(n)
print(result)  # Output: [0, 1, 4, 9, 25, 64, 169, 256, 625, 1296]