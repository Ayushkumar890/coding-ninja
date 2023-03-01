n = int(input())
i = 1
a = (n+1)//2
b= n//2
while i <=a:
    spaces = 1
    while spaces <= a-i:
        print(" ",end = "")
        spaces = spaces +1
    j = 1
    while j<=(i*2)-1:
        print("*",end = "")
        j = j+1
    print()
    i = i+1
i = b
while i >=1:
    spaces = 1
    while spaces <= b-i+1:
        print(" ",end = "")
        spaces = spaces+1
    j = 1
    while j<=(i*2)-1:
        print("*",end = "")
        j = j+1
    print()
    i = i-1
