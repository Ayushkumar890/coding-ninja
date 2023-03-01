# def spiralPrint(m, n, a):
#     k = 0
#     l = 0
#     while (k < m and l < n):
#         for i in range(l, n):
#             print(a[k][i], end=" ")
#         k += 1
#         for i in range(k, m):
#             print(a[i][n - 1], end=" ")
#         n -= 1
#         if (k < m):
#             for i in range(n - 1, (l - 1), -1):
#                 print(a[m - 1][i], end=" ")
#             m -= 1
#         if (l < n):
#             for i in range(m - 1, k - 1, -1):
#                 print(a[i][l], end=" ")
#             l += 1
#
# R = int(input())
# C = int(input())
# a = [[int(x)for x in input().split()]for i in range(R)]
# spiralPrint(R, C, a)






# from tkinter import *
# top = Tk()
# b = Button(top,text = "learn and earn")
# c = Canvas(top,bg = "white",height = "5000",width  = "5000")
# # name = Label(top, text = "Name").place(x = 30,y = 50)
# # email = Label(top, text = "Email").place(x = 30, y = 90)
# # password = Label(top, text = "Password").place(x = 30, y = 130)
# #creating label
# c.pack()
#
# #creating label
# uname = Label(top, text = "do you want play (if yes then type play)").place(x = 150,y = 50)
#
# password = Label(top, text = "choose the subject (math , science , GK)").place(x = 150, y = 90)
#
#
# sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 400, y = 200)
#
# e1 = Entry(top,width = 50).place(x = 400, y = 50)
#
# e2 = Entry(top, width = 50).place(x = 400, y = 90)
#
# c.pack()
#
# top.mainloop()



# n = int(input())
# li = []
# for i in range(n):
#     b = int(input())
#     li.append(b)
#     sum = 0
#     for j in range(len(li)):
#         sum = sum +li[j]
# print(sum)
# a = len(li)
# result = sum/a
# y = (type(result))
# if y == float:
#     print(int(result)+1)
# else :
#     print(result)
# #






# question number 1

# n = int(input())
# b = [int(x)for x in input().split()]
# sum = 0
# for j in range(len(b)):
#     sum = sum + b[j]
# print(sum)
# a = len(b)
# result = sum/a
# y = (type(result))
# if y == float:
#     print(int(result)+1)
# else :
#     print(result)
# exit()

# question number 2

# s = input()
# w = s.split(" ")
# for i in w:
#     nw = i[::-1]
#     ns = "".join(nw)
#     print(ns,end = " ")
#

# question number 4

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


# question number 5

# n = input()
# s = n.split(" ")
# m = int(input())
# for i in s:
#     n = i[m:]
#     print(n)
#     break

# question number 6

# n = [int(x)for x in input().split()]
# m = [int(x)for x in input().split()]
# rem = []
# sum1 = 0
# sum2 = 0
# for i in range(len(n)):
#     for j in range(len(m)):
#         if n[i] == m[j] :
#             a = m[j]
#             rem.append(a)
# for i in range(len(rem)):
#     n.remove(rem[i])
#     m.remove(rem[i])
# # print(n)
# # print(m)
# for i in range(len(n)):
#     sum1 = sum1 + n[i]
# for j in range(len(m)):
#     sum2 = sum2+ m[j]
# total = sum1 +sum2
# li = n + m
# str = str(li)[1:-1]
# print(str.replace(',',""),total)

# question number 8

# n = int(input())
# li = []
# lib = []
# for i in range(n):
#     b = input()
#     li.append(b)
#     for j in range(len(li)):
#         b = len(li[j])
#         lib.append(b)
#         i = i+1
#     print(b)
# a = max(lib)
# for i in range(len(li)):
#     if a == len(li[i]):
#         res = li[i]
#         print(res,end = " ")


# question number 9

# n = int(input())
# li = []
# for i in range(n):
#     b = int(input())
#     li.append(b)
# a = max(li)
# count = 0
# for i in li:
#     if i == a:
#         count = count +1
# print(count)


# question number 3

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


# question  number 10

# n = int(input())
# sem = []
# fin = []
#
# m = [(x)for x in input().split()]
# for i in range(len(m)):
#     for j in range(len(m)):
#         b = str(m[i])
#     fin.append(b)
# # print(fin)
# for i in range(len(fin)):
#     b = m[0::n]
# sem.append(b)
# for i in range(len(fin)):
#     c = m[1::n]
# sem.append(c)
# for i in range(len(fin)):
#         d = m[2::n]
# sem.append(d)
# print((sem))





# #File Mode	Meaning
# # w	Create a new file for writing. If a file already exists, it truncates the file first. Use to create and write content into a new file.
# # x	Open a file only for exclusive creation. If the file already exists, this operation fails.
# # a	Open a file in the append mode and add new content at the end of the file.
# # b	Create a binary file
# # t	Create and open a file in a text mode
#
# # create a empty text file in current directory
# fp = open('sales.txt', 'x')
# fp.close()



# create a empty text file
# fp = open('sales_2.txt', 'w')
# fp.write('AstitvaSinha')
# print(fp)
# fp.close()


# from datetime import datetime
#
# # get current date and time
# x = datetime.now()

# create a file with date as a name day-month-year
# file_name = x.strftime('%d-%m-%Y.txt')
# with open(file_name, 'w') as fp:
#     print('created', file_name)
#
# # with name as day-month-year-hours-minutes-seconds
# file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name_2, 'w') as fp:
#     print('created', file_name_2)
#
# # at specified directory
# file_name_3 = r"E:\demos\filedemo" + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name_3, 'w') as fp:
#     print('created', file_name_3)
#
# # Reading files using 'with'
# with open('read_demo.txt', 'r') as file:
#     print(file.read())
#
# def selectionsort (nlist):
#     for i in range(len(nlist)-1,0,-1):
#         a= 0
#         for j in range(1,i+1):
#             if nlist[j]<nlist[a]:
#                 a = j
#         li = nlist[i]
#         nlist[i] = nlist[a]
#         nlist[a] = li
# nlist = [14,16, 46, 27, 57, 41, 45, 21, 70 ]
# selectionsort(nlist)
# print(nlist)



#



# def selection(A):
#     for i in range(len(A)):
#         midindex = i
#         for j in range((i+1),len(A)):
#             if A[j] < A[midindex]:
#                 midindex = j
#         A[i],A[midindex] = A[midindex],A[i]
#     return A
# A = [int(x)for x in input().split()]
# selection(A)
# fin = str(A)[1:-1]
# print(fin.replace(',',""))




# def sorting(arr, size):
#     for i in range(size):
#         temp = i
#         for j in range(i+1, size):
#             if arr[j] < arr[temp]:
#                 temp = j
#         arr[i], arr[temp] = arr[temp], arr[i]
#         fin = str(arr)[1:-1]
#         print(fin.replace(',', ""))
#
# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(b):
#         arr = [int(x)for x in input().split()]
#         size = len(arr)
#         sorting(arr, size)
#         fin = str(arr)[1:-1]
#         print(fin.replace(',', ""))
#         break
#


#### merge of two array
# def sorting(arr, size):
#     for i in range(size):
#         temp = i
#         for j in range(i+1, size):
#             if arr[j] < arr[temp]:
#                 temp = j
#         arr[i], arr[temp] = arr[temp], arr[i]
#
# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(b):
#         arr1 = [int(x)for x in input().split()]
#         c = int(input())
#         for k in range(c):
#             arr2 = [int(x)for x in input().split()]
#             arr  = arr1+arr2
#             # print(arr)
#             size = len(arr)
#             sorting(arr, size)
#             fin = str(arr)[1:-1]
#             print(fin.replace(',', ""))
#             break




# def sorting(arr, size):
#     for i in range(size):
#         temp = i
#         for j in range(i+1, size):
#             if arr[j] < arr[temp]:
#                 temp = j
#         arr[i], arr[temp] = arr[temp], arr[i]
#
#
# n = int(input())
# for i in range(n):
#     b = int(input())
#     if b != 0:
#         for j in range(b):
#             arr = [int(x)for x in input().split()]
#             size = len(arr)
#             sorting(arr, size)
#             sem = (arr[-2])
#             if sem == arr[-1]:
#                 print("-2147483648")
#             else:
#                 print(sem)
#             break
#     else:
#         print("-2147483648")

# li = [int(x)for x in input().split()]
# li.sort()
# n = str(li)[1:-1]
# print(n.replace(',',""))


# def insertion (arr):
#     length = len(arr)
#     for i in range(1,length):
#         j = i-1
#         temp = arr[i]
#         while j >=0 and arr[j]>temp:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = temp
#         print(arr)
# arr = [int(x) for x in input().split()]
# insertion(arr)
# print(arr)

#
# def insertion (arr):
#     length = len(arr)
#     for i in range(1,length):
#         j = i-1
#         temp = arr[i]
#         while j >=0 and arr[j]>temp:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = temp
#         print(arr)
# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(b):
#         arr = [int(x) for x in input().split()]
#         insertion(arr)
#         print(arr)

# a=[1,2,3,4,5,6,7,8,9]
# ele=int(input())
# l=0
# u=len(a)-1
# flag=False
# while l<u:
#   m=(l+u)//2
#   if ele==m:
#     flag= True
#     f=m
#   if ele>m:
#     l=m+1
#     m=(l+u)//2
#   if ele<m:
#     u=m-1
#     m=(l+u)//2
# if flag:
#   print("found at ",f)
# else:
#   print("not found")



# def mergeoftwolist(a1,a2,debug = False):
#   i , j = 0,0
#   len1,len2 = len(a1),len(a2)
#   # newarray = []
#   while (i<len1 and j<len2):
#     if a1[i]<a2[j]:
#       newarray.append(a1[i])
#       i = i+1
#     else:
#       newarray.append(a2[j])
#       j = j+1
#   while (i<len1):
#     newarray.append(a1[i])
#     i = i+1
#   while (j<len2):
#       newarray.append(a2[j])
#       j = j+1
#   return newarray
# n = int(input())
# newarray = []
# for i in range(n):
#   b = int(input())
#   for j in range(b):
#     a1 = [int(x) for x in input().split()]
#     c = int(input())
#     for k in range(c):
#       a2 = [int(x) for x in input().split()]
#       mergeoftwolist(a1,a2,debug = False)
#       newarray.sort()
#       print(newarray)


# def sorting(arr, size):
#     for i in range(size):
#         temp = i
#         for j in range(i+1, size):
#             if arr[j] > arr[temp]:
#                 temp = j
#         arr[i], arr[temp] = arr[temp], arr[i]
#
#
# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(b):
#         arr = [int(x)for x in input().split()]
#         size = len(arr)
#         sorting(arr, size)
#         fin = str(arr)[1:-1]
#         print(fin.replace(',', ""))
#         break
