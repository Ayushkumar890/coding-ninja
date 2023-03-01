n = int(input())
i = 1
while i<=n:
    space = 1
    while space <=n-i:
        print(" ",end = "")
        space = space+1
    j = 1
    while j <=i:
        print(i-j+1,end = "")
        j = j+1

    j = 1
    while j <=i-1:
        print (j+1,end = "")
        j = j+1
    print()
    i = i+1