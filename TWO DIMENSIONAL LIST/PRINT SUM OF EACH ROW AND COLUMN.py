n = int(input("enter the number of row :"))
m = int(input("enter the number of column :"))
r = 0
c = 0
row = []
col = []
matrix = []
totalsumofrow = []
totalsumofcolumn = []
for i in range(n):
    a = []
    for j in range(m):
        b = int(input())
        a.append(b)
    matrix.append(a)
for i in range(n):
    for j in range(m):
        r = r+matrix[i][j]
        c = c+matrix[j][i]

    row.append(r)
    col.append(c)
    r = 0
    c = 0
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end = " ")
    z = row[i]
    totalsumofrow.append(z)
    x = col[i]
    totalsumofcolumn.append(x)
    print()
print("sum of row : ",totalsumofrow)
print("sum of column : ",totalsumofcolumn)