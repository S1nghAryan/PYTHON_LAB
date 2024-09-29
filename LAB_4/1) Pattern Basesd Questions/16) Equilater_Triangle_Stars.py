n=7
for i in range(n,0,-1):
    print(" "*(i-1), end=" ")
    for j in range(n-i+1):
        print("*", end=" ")
    print()
    