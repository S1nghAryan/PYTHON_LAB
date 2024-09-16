x=int(input('Enter No. = '))
rev=0
y=x

while y>0:
    n=y%10
    rev=(rev*10)+n
    y=y//10
    
if (x==rev):
    print('Palindrome')
else:
    print('Not Palidrome')