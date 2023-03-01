#     input of two list  ##########
# str = input().split()
# n,m = int(str[0]),int(str[1])
# li = [[int(j)for j in input().split()]for i in range(n)]
# print(li)



####     input of two list  ##########
# n = int(input())
# li = [[int(j)for j in input().split()]for i in range(n)]
# print(li)

# str = input().split()
# n,m = int(str[0]),int(str[1])
# b =  input().split()
# li = [[int(b[m*i+j])for j in range(m)]for i in range(n)]
# print(li)

#printing 2 d list

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 3
# m = 4
# for i in range (n):
#     for j in range (m):
#         print(li[i][j],end = " ")
#     print()

# li = [[1,2,3,4],[5,6],[9,10,11,12]]
# n= 3
# for row in li :
#     for ele in row:
#         print(ele,end = " ")
#     print()

# n = input()
# a = ''
# for i in range(len(n)):
#     if i%2 == 0:
#         a = a + n[i]
#
# print("input string :  ", n)
# print("String after odd charcater :", a)

# n = input()
# b = input()
# a = n.startswith(b)
# print(a)


def myname(name):
    print("welcome" " " + name)