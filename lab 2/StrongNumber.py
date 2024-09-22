
num = int(input("Enter a number: "))

sum_of_factorials = 0

for digit in str(num):
    factorial = 1
    for i in range(1, int(digit) + 1):
        factorial *= i
    sum_of_factorials += factorial

if sum_of_factorials == num:
    print(num, "is a strong number.")
else:
    print(num, "is not a strong number.")