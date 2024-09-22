def calculate_lcm_gcd(num1, num2):
   
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    lcm = abs(num1 * num2) // gcd(num1, num2)

    return lcm, gcd(num1, num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm, gcd = calculate_lcm_gcd(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}.")
print(f"The GCD of {num1} and {num2} is {gcd}.")