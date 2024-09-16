a=int(input('enter no. = '))
count=0
for i in range(2,a):
    if (a%i == 0):
        count+=1
    else:
        break
if (count>1):
    print('Not Prime')
else:
    print('prime')

        
    