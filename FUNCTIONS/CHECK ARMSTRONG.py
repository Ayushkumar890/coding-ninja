'''

def checkarmstrong(n):
    a = 0
    b = n
    while (b>0):
        a = a+1
        b = b//10
    c = 0
    b = n
    while (b>0):
        rem = b %10
        c = c+(rem**a)
        b = b //10
    if(c ==n):
        return True
    else:
        return False
n = int(input())
if (checkarmstrong (n)):
    print("true")
else :
    print("false")
'''
n = int(input())
sum = len(str(n))
a = 0
b = n
while (n>0):
    rem = n%10
    a = a+(rem**sum)
    n = n//10
if b ==a:
    print("true")
else:
    print("false")