'''
n = int(input())
i = 1
while i <=n:
    spaces = 1
    while spaces<i:
        print(" ",end = "")
        spaces = spaces +1
    j = i
    while j <=n:
        print(j,end = "")
        j =j+1
    print()
    i = i+1
i = 1
while i<=n:
    spaces = 1
    while spaces<=(n-i):
        print(" ",end = "")
        spaces = spaces +1

    j = i
    while j >=1:
        print(n-j+1,end = "")
        j = j-1
    print()
    i = i+1

'''



##### or  #######

n = int(input())
for i in range (1,n+1):
    spaces = 1
    for j in range (1,i):
        print(" ",end = "")
        spaces +=1
    a = i
    for j in range (spaces,n+1):
        print(a,end = "")
        a = a+1
    print()
for i in range (n-1,0,-1):
    count = 1
    for j in range (1,i):
        print (" ",end = "")
        count = count +1
    num = i
    for j in range (count,n+1):
        print(num,end = "")
        num= num+1
    print()
