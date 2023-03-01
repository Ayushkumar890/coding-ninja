# n = int(input())
# i = 1
# while i<=n:
#     j = 1
#     while j<= i:
#         print("*",end = "")
#         j = j+1
#     print()
#     i =i+1


### print isoceles triangle  ####

n = int(input())
print(" ")
for i in range (1,n+1):
    for j in range (i,n):
        print(" ",end = " ")
    for k in range (1,i+1):
        print("*",end = " ")
    for j in range(1,i):
        print("*",end = " ")
    print()