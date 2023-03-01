'''
n = int(input())
i = 1
while i<=n:
    space = 1
    while space <= n-i:
        print(" ",end = "")
        space = space +1
    j = 1
    while j <=i:
        print(i +j-1,end = "")
        j = j+1
    j = j-1
    j = i-1
    while j >=1:
        print(i +j-1,end = "")
        j = j-1
    i = i+1
    print()
    '''
########## or  #########
n = int(input())
for i in range(1,n+1,1):
    for space in range (n-i):
        print(" ",end = "" )
    for j in range (i , i*2,1):
        print(j,end = "")
    for j in range (i*2-2,i-1,-1):
        print(j,end ="")
    print()