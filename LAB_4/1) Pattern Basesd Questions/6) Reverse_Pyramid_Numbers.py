n=5
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1,0,-1):
        print(j, end=" ")
    print()