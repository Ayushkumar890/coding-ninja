# add of two matrix

x = [[1,2],[3,4]]
y = [[5,6],[7,8]]
z = [[0,0],[0,0]]
for i in range (len(x)):
    for j in range (len(y)):
        z[i][j] = x[i][j]+y[i][j]
print(z)


### MULTIPLY OF TWO MATRIX

x = [[1,2],[3,4]]
y = [[5,6],[7,8]]
z = [[0,0],[0,0]]
for i in range (len(x)):
     for j in range(len(y[0])):
         for k in range(len(y)):
            z[i][j] += x[i][k]*y[k][j]
print(z)

### SUM OF ROW
x = [[1,2,3],[1,2,3]]
c = 0
for i in range(len(x)):
    for j in range(len(x[i])):
        c = c +x[i][j]
    print(c)
    c = 0