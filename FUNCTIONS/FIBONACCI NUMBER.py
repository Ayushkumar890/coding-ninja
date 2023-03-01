def checkMember(n):
    if  n==1 or n==0:
        return True
    a = 0
    b = 1
    while a<n:
        a,b= a+b,a
    if a==n:
        return True
    return False




    pass
n = int(input())
if (checkMember(n)):
    print("true")
else :
    print("false")