n = int(input())
a = 2*n
for i in range(1,a):
    p = n
    for j in range (1,a):
        print(p,end = "")
        if j<i:
            p = p-1
        if j>=(2*n)-i:
            p = p+1
    print()
