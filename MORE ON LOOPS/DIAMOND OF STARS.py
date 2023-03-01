n = int(input())
a = (n+1)//2
b = n//2
i = 1
while i<=a:
    space = 1
    while space <=a-i:
        print(" ",end = "")
        space = space +1

    j = 1
    while j <=(2*i)-1:
        print ("*",end = "")
        j = j+1
    print()
    i = i+1
i = b
while i>=1:
    space = 1
    while space <=b-i+1:
        print(" ", end="")
        space = space + 1
    j = 1
    while j <=(2*i)-1:
        print ("*",end = "")
        j = j+1
    print()
    i = i-1
