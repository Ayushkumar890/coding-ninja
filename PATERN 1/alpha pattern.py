n = int(input())
i = 1
while i <=n:
    j = 1
    while j <=i:
        charP = chr(ord('A')+i-1)
        print(charP,end = "")
       ## charP = charP +1
        j = j+1
    i = i+1
    print()