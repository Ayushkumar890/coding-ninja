n = int(input())
i = 1
while i <=n:
    j = 1
    while j <=n:
        if i == j:
            print('*',end = "")
        else:
            print("0",end = "")
        j = j+1
    j = j-1
    print('*',end = "")
    while j >=1:
        if i == j:
            print('*',end = "")
        else:
            print("0",end = "")
        j = j-1
    print()
    i = i+1
