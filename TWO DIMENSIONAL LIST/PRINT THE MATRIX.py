n = int(input("enter the number of row"))
m = int(input("enter the number of column"))
matrix = []
v = []
for i in range(n):
    a = []
    for j in range(m):
        b = int(input())
        a.append(b)
    matrix.append(a)
v.append(matrix)
for i in range(n):
    for j in range(m):
        k = [v]
        print(k[i][j],end = " ")
        exit()
    print()