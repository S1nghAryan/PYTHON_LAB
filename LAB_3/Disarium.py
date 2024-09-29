def is_disarium(n):
    digits = [int(d) for d in str(n)] 
    sum_of_powers = sum([d ** (i + 1) for i, d in enumerate(digits)]) 
    return sum_of_powers == n  


num = 175
if is_disarium(num):
    print(f"{num} is a Disarium Number.")
else:
    print(f"{num} is not a Disarium Number.")