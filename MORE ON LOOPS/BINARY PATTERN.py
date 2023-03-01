'''n = int(input())
for i in range (0,n):
    for j in range (n-i,0,-1):
        if i%2==0:
            print("1",end = "")
        else:
            print("0",end = "")
    print()

    '''
n = int(input())
i = 1
while i <=n:
    j = 1
    while j <=n-i+1:
        if i%2==0:
            print("0",end = "")
        else:
            print("1",end = "")
        j = j+1
    i = i+1
    print()
