# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30,
#   "grapes": 10
# }
# print(fruits)
#
# print()
# print()
#
# # dictionary is a collection of key-value pairs. It is an unordered and mutable data type (that can be changed). It is represented by curly braces {}
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30,
#   "grapes": 10,
#   "apple": 20  # overwrites previous key value
# }
# print(fruits)
# print()
#
# #Using the dict() function - It takes a list of tuples as an argument and returns a dictionary.
# fruits = dict([
#   ("apple", 10),
#   ("banana", 20),
#   ("orange", 30)
# ])
# print(fruits)
# print()
# print()
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30,
#   "grapes": 10
# }
# # 1. Using get() method with key
# print("Price of apple is", fruits.get("apple"))
# # 2. Using square brackets with key
# print("Price of banana is", fruits["banana"])
#
#
# print()
# print()
# # To add new element in the dictionary
# fruits = {
#   "apple": 10,
#   "banana": 20
# }
# print("Before adding new fruit:", fruits)
#
# # Add a new fruit
# fruits["orange"] = 30
# print("After adding new fruit:", fruits)
#
# print()
# print()
#
# # To update items in dictionary
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30
# }
# print("Before updating:", fruits)
# print()
# print()
# # Update the price of apple
# fruits["apple"] = 15
# print("After updating:", fruits)
# print()
# print()
#
# # to remove particular item using pop() method
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30
# }
# print("Before removing:", fruits)
# print()
# print()
# # Removing apple
# fruits.pop("apple")
# print("After removing apple:", fruits)
# print()
# print()
# # Removing banana
# fruits.pop("banana")
# print("After removing banana:", fruits)
# print()
# print()
#
# # to remove last inserted element
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30
# }
# print("Before removing:", fruits)
# print()
# print()
# # Removing the last inserted element
# fruits.popitem()
# print("After removing:", fruits)
#
# print()
# print()
# # using delete
# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30
# }
# print()
# print()
# # Removing apple
# del fruits["apple"]
# print(fruits)
# print()
# print()
#
# # Iterating through dictionary ( List/ Traverse operation)
# fruits = {
#   "apple": 10,
#   "banana": 20
# }
#
# # Iterating through the dictionary
# print("Method 1: using items() method")
# for key, value in fruits.items():
#     print(key, value)
# print()
# print()
# print("Method 2: using keys() method")
# for key in fruits.keys():
#     print(key, fruits[key])
# print()
# print()
# print("Method 3: access keys directly")
# for key in fruits:
#     print(key, fruits[key])


# n= "fsafsavxz"
# n1 = n.replace("s","c")
# print(n1)

# def countInString(str):
#     v,c,d,s = 0,0,0,0
#     for char in str :
#         if ((char>='a'and char<='z')and (char>='A'and char<='Z')):
#             char = char.lower()
#             if(char =='a' or char =='e' or char=='i' or char =='o'or char=='u'):
#                 v = v+1
#             else :
#                 c = c+1
#         elif(char>='0'and char<='9'):
#             d = d+1
#         else:
#             s = s+1
#     return v,c,d,s
#
# str = input()
# v,c,d,s = countInString(str)
# print(v,c,d,s)





# a=input()
# i=0
# x=''
# while(i<len(a)):
#     j=i+1
#     c=1
#     while j<len(a) and (a[i]==a[j]):
#         j+=1
#         c+=1
#     if c==1:
#         x+=a[i]
#     else:
#         x+=a[i]+str(c)
#     i=j
# print(x)




# n = {"ayush": "1416","ayush sharma ":"1418","ayush kumar": "1415","ayush gupta":"1422"}
# print(n)
# print()
#
# print(n["ayush"])
# n["temp"] = 32
# print(n)
# print()
#
# del n["temp"]
# print(n)
# print()
#
# print(len(n))
# print()
#
# for key in n:
#     print(key),n[key]
# print()
#
# print(n)
# print()
#
# n.update({"ayush":1417})
# print(n)
# print()
#
# m = n.copy()
# print(m)
# print()
#
# # b = n.clear()
# # print(b)
# # print()
#
# c = n.values()
# print(c)
# print()
#
# print(n)
# x = "ayush" in n
# print(x)
#
# n2 =  {'pears': 4, 'grapes': 5, 'lemons': 6}
# n.update(n2)
# print(n)



# n=int(input())
# li=[]
# for i in range(0, n):
#      ele = int(input())
#      li.append(ele)
# c=1 # to count number of fruits
# for i in range(0, n-1):
#    if(li[i]==li[i+1]):
#        c=c+1
#        if(i==n-2):              #if i the second last element and it is same as the last element
#            print(li[i],c)
#    else:
#        print(li[i],c)
#        c=1
#
# if(li[n-1]!=li[n-2]):         #if the last element has occured only once
#    print(li[n-1],1)

# n = int(input())
# li=[]
# ele1 = 0
# ele2 = 0
# for i in range(0, n):
#     ele = int(input())
#     li.append(ele)
# maxSum=0
# Sum=0
# for i in range(0, n-1):
#     for j in range(i+1,n):
#         Sum=li[i]+li[j]
#         if(Sum>maxSum):
#             maxSum=Sum
#             ele1=li[i]
#             ele2=li[j]
# print(ele1,ele2)

# n = "hello"
# c = 0
# for x in n:
#     if (x!="l"):
#         c = c+1
#     else:
#         pass
# print(c)



#
# s = input()
# uppercase = 0
# lowercase = 0
# for c in s :
#     if c.isupper():
#         uppercase+=1
#     elif c.islower():
#         lowercase+=1
#     else:
#         pass
# print(uppercase)
# print(lowercase)


# n = [int(x)for x in input().split()]
# s = set()
# for i in n:
#     s.add(i)
# sum = 0
# for i in s:
#     sum = sum +i
# print(sum)

# a = int(input())
# for i in range(a):
#     n = int(input())
#     m = int(input())
#     l = [[int(x)for x in input().split()]for j in range(n)]
#     for b in range(m):
#         if b % 2 ==0:
#             for i in range(n):
#                 print(l[i][b],end = " ")
#         else:
#             for i in range(-1,-n-1,-1):
#                 print(l[i][b],end = " ")


# t = int(input())
# for i in range(t):
#     m,n = (int(j) for j in input().split())
#     a = [list(int(x) for x in input().split()) for i in range(m)]
#     for i in range (len(a)):
#         if i ==0:
#             for j in range(len(a[0])):
#                 print(a[i][j],end=' ')
#         for j in range(-1,0,1) :
#             if i!=0:
#                 print(a[i][j],end=' ')
#         for i in range(-1,0,1):
#             for j in range(-1,0,-1):
#                 if j!=-1:
#                     print(a[j][i],end=' ')




# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if n-1< i + j:
#             print("2",end=" ")
#         if n-1 == i+j:
#             print("1",end=" ")
#         if n-1>i + j:
#             print("0",end=" ")
#     print()


# n = [int(x)for x in input().split()]
# ele = int(input())
# for i in range(len(n)):
#     if ele in n:
#         print("number in list", n.index(ele) )
#     else :
#         print("number is not in list")
#     exit()
#
#
# li = [int(x)for x in input().split()]
# ele = int(input())




# from tkinter import *
#
# top = Tk()
# text = Text(top)
# text.insert(INSERT, "Name.....")
# text.insert(END, "Salary.....")
#
# text.pack()
#
# text.tag_add("Write Here", "1.0", "1.4")
# text.tag_add("Click Here", "1.8", "1.13")
#
# text.tag_config("Write Here", background="yellow", foreground="black")
# text.tag_config("Click Here", background="black", foreground="white")
#
# top.mainloop()





# from tkinter import *
#
# root = Tk()
#
# root.geometry("200x200")
#
# def open():
#     top = Toplevel(root)
#     top.mainloop()
#
# btn = Button(root, text = "open", command = open)
#
# btn.place(x=75,y=50)
#
# root.mainloop()