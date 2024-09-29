def is_armstrong(n):
    digits = [int(d) for d in str(n)] 
    num_digits = len(digits) 
    sum_of_powers = sum([d ** num_digits for d in digits])  
    return sum_of_powers == n 

for i in range(1, 1001):
    if is_armstrong(i):
        print(i)