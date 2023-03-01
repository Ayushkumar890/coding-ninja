# 1
# n = int(input())
# num = n
# a = 0
# while n>0:
#     rem = n%10
#     b = a*10+rem
#     n = n//10
#     if b != num:
#         print("number is not palidrom")
#     else:
#          print("number is  palidrom")
#     break


#problem number 3

# n = int(input())
# if n <=100:
#     print("no charges")
# elif 100<=n<=200 :
#     b = (n-100)*5
#     print(b)
# elif n>=200:
#     c = (n-200)*10+500
#     print(c)


# problem number 3

# gend = input()
# n = int(input())
# orignalsalary = n
# if gend == "m":
#     n = n +0.1*n
#     if orignalsalary<=10000:
#         n = n+orignalsalary/40
# if gend =="f":
#     n = n +0.15*n
#     if orignalsalary<=10000:
#         n = n+orignalsalary/40
# print(int(n))

# problem 4
n=int(input())
a=[]
b=[]
fact=1
for i in range(1,n+1):
    fact=1
    ele=int(input())
    a.append(ele)
    for j in range(1,ele+1):
        fact=fact*j
    b.append(fact)
print(a)
print(b)

# problem 5
