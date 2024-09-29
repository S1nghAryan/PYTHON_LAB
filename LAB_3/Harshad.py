def is_harshad(n):
    digits = [int(d) for d in str(n)]  
    sum_of_digits = sum(digits) 
    return n % sum_of_digits == 0  
num = 18
if is_harshad(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")