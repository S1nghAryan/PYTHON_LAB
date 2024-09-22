
num = int(input("Enter a number: "))
num_digits = len(str(num))
sum_of_digits = 0

for digit in str(num):
    sum_of_digits += int(digit) ** num_digits

if sum_of_digits == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")