n = int(input())
i = 1
while i <=n:
    spaces = 1
    while spaces <= n-i:
        print(" ",end = "")
        spaces = spaces +1
    j = 1
    while j<=i:
        print(i+j-1,end = "")
        j = j+1
    j= i-1
    while j>=1:
        print(i+j-1,end = "")
        j = j-1
    print()
    i = i+1
