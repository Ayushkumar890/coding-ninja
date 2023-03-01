n = int(input())
i = 1
while i<=n:
    j = 1
    ch = (ord('A')+n-i)
    while j <=i:
        print(chr(ch+j -1),end = "")
        j = j+1
    print()
    i = i+1

