n=4
current=1
for i in range (1,n+1):
    row_length=i
    start= current+ row_length-1
    for j  in range(start, current-1, -1):
        print(j,end=" ")
    current+=row_length
    print() 