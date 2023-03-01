n = int(input())
a = (n+1)//2
b = n-a
i = 1

while i<=a:
    space = 1
    while space<=i-1:
        print(" ",end = "")
        space = space+1
    j = 1
    while j <=i:
        print("* ",end = "")
        j = j+1
    print()
    i = i+1
i = 1
while i<=b:
    space = 1
    while space <= b-i:
        print(" ", end="")
        space = space + 1
    j = 1
    while j <= b-i+1:
        print("* ", end="")
        j = j+1
    print()
    i = i+1