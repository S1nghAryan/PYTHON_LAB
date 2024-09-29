n=3
current_number=1
for i in range(1,n+1):
    for j in range(1,2*i):
        print(current_number, end=" ")
        current_number+=1
    print()