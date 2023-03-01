li = [[1,2,3,4,5],[1,2,3,4,5,]]
# n = int(input())
# m = int(input())
# for i in range (n):
#     for j in range (m):
#         print(li[i][j],end = " ")
#     print()
n = 3
for i in li:
    for ele in i:
        print(ele,end = " ")
    print()

print()
print()
for row in li:
    output = ' '.join([str(ele)for ele in row])
    print(output)


#move first alphabet to last and last to first
n = input()
a = n[-1]
b = n[0]
print(a+n[1:-1]+b)

# move first alphabet to last
n = input()
a = n[-1]
b = n[0]
print(n[1:]+b)

# reverse the string
n = input()
i = n[::-1]
print(i)


# print first element of the string in last of the string
n = input()
for i in range (len(n)):
    a = n[i]
    c = n[len(n)-1]
    print(n[1:-1]+n[0])
    exit()