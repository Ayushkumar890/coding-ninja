# li = [1,3,4,5,7,7,3]
# li.insert(1,"ayush")
# print("insert",li)
#
# print(      )
#
#
# li = [1,2,3,4,5,6]
# li.extend([3])
# print("extend",li)
#
# print(   )
#
#
# li.append([2,3,4,5,6,7,8,])
# print("append",li)
#
#
# print(  )
#
# li.remove(1)
# print("remove",li)
#
#
# print(  )
#
# li.pop(3)
# print("pop",li)
#
#
# print(  )
#
#
# li = [1,2,3,"ayush",9,10,"aniket"]
# for i in range (len(li)):
#     print(li[i])
#
# print(  )
#
#
# for ele in li :
#     print("ele",ele)
#
# print(  )
#
#
# for ele  in li[2:4]:
#     print(ele)
#
#
# print(   )
#
#
# print(li[-1])
# print(li)
#
# print()
#
# print(li[-3:])
#
#
# print( )

n = int(input())
li = []
for i in range (n):
    a = int(input())   #is used to  add element at  the last
    li.append(a)
print(li)
####

print( )

####
for ele in li:
    print(ele)

print( )
#######
str = input()

li = []
s = str.split(' ')
print(s)

####
print( )
n = int(input())
li = [int(x)for x in input().split()]
for ele in li:
    print(ele)

#####

li = [1,2,3,4,5,6,7]
li.insert(3,52)
print(li)
###

li.append([34,35,36,37,38,39])
print(li)

print( )

print(len(li))

#####

li = [75,57,5,47,73]    ### used to print the list in ascending order
li.sort()
print(li)


print(  )

######

li = [75,57,5,47,73]  ## used to reverse the list
li.sort(reverse = True)
print(li)


#######

li = li .copy()
print(li)
print(  )
li = list(li)
print(li)


# input the matrix from the user
# str = input().split()
# n,m = int(str[0]),int(str[1])
# li = [[int(j)for j in input().split()]for i in range(n)]
# print(li)


# set1 = set() # A new empty set
# set1.add("cat") # Add a single member
# set1.update(["dog", "mouse"]) # Add several members
# if "cat" in set1: # Membership test
#   set1.remove("cat")
# #set1.remove("elephant") - throws an error
# print(set1)
# for item in set1: # Iteration AKA for each element
#   print(item)
# print("Item count:", len(set1)) # Length AKA size AKA item count
# isempty = len(set1) == 0 # Test for emptiness
# set1 = set(["cat", "dog"]) # Initialize set from a list
# set2 = set(["dog","mouse"])
# set3 = set1 & set2 # Intersection
# set4 = set1 | set2 # Union
# set5 = set1 - set3 # Set difference
# set6 = set1 ^ set2 # Symmetric difference
# issubset = set1 <= set2 # Subset test
# issuperset = set1 >= set2 # Superset test
# set7 = set1.copy() # A shallow copy
# set7.remove("cat")
# set8 = set1.copy()
# set8.clear() # Clear AKA empty AKA erase
# print(set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset)



# change tuple to list
n = ("ayush","true",'1',"2","3",)
b = list(n)
b[1] = "python"
print(b)

n = ("ayush","true",'1',"2","3",)
for i in range (len(n)):
    print(n)
    exit()

### print the last element in list is equal to 100
n = [(10,20,40),(40,50,60),(70,80,90)]
b = []
for i in range (0,len(n)):
    a = list(n[i])
    b.append(a)
    for j in b:
        j[-1]=100
        c = tuple(b)
print(c)