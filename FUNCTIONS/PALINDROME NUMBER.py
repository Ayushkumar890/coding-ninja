n = int(input())
a = n
rev = 0
while a!=0:
    rev = (rev*10)+(a%10)
    a = a//10
if n==rev :
    print("True")
else:
    print("False")