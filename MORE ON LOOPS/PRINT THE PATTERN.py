n = int(input())
a = 1
for i in range (1,n+1):
    for j in range (a,a+n):
        print(j,end = " ")
    print()
    if (i==((n+1)//2)):
        if (n%2)!=0:
            a = n*(n-2)+1
        else :
            a= n*(n-1)+1
    elif (i>(n+1)//2):
        a = a-2*n
    else:
        a = a+2*n