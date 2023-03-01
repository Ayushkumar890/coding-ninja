n = int(input())

i = 1
while i<=n:
    j = 1
    while j <=i:
        print(j,end = "")
        j = j+1
    space = 1
    while space <=(n-i)*2:
        print(" ",end = "")
        space = space+1
    j = 1
    while j<=i:
        print(i-j+1,end = "")
        j = j+1
    i = i+1
    print()