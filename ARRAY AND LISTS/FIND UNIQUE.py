# ##### ALTERNATE ELEMENT IN LIST
li = []
n = int(input())
for i in range (n):
    a = int(input())
    li.append (a)
for i in range(0,n,2):
    print(li[i])


# ##### REVERSE THE LIST
li = [int(x)for x in input().split()]
a = li[::-1]
print(a)

#
####### THE LARGEST ELEMENT IN LIST
li = []
n = int(input('How many elements you want to enter? '))
print(str(n))
for i in range(n):
    data = int(input())
    li.append(data)
max = 0
for data in li:
    if data > max:
        max = data

print('The largest number in list is', max)



# #### ROTATE THE ELEMENT
n  = int(input())
li = [int(x)for x in input().split()]
print("Original List")
print(li)

l = li[-1:] +li[:-1]


print("Rotated List")
print(l)
