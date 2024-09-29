n=5
even=10
for i in range(1,n+1):
    for j in range(i):
        print(even-(j*2), end=" ")
    print()
