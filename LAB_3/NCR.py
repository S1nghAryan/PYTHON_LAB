import math

def calculate_ncr(n, r):

    return math.comb(n, r)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

result = calculate_ncr(n, r)
print(f"The value of {n}C{r} is {result}")