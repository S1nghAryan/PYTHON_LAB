print("Pleaese enter the operator\n" \
      "'1' for addition\n" \
      "'2' for subtraction\n" \
      "'3' for multiplication\n" \
      "'4' for division\n" \
      "'5' for modulas\n")
operator=int(input("Select Operation :"))
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
if operator==1:
    operation=num1+num2
    print(operation)
elif operator==2:
    operation=num1-num2
    print(operation)
elif operator==3:
    operation=num1+num2
    print(operation)
elif operator==4:
    operation=num1/num2
    print(operation)
elif operator==5:
    operation=num1%num2
    print(operation)    
else:
    print("Enter a valid operator")