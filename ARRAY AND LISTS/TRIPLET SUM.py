n = int(input("enter the number of row :"))
m = int(input("enter the number of column :"))
a = []
for i in range (n):
    b =[]
    for j in range(m):
        ele = int(input())
        b.append(ele)
    a.append(b)
print(a)