n = int(input())
a = n
rev = 0
while (n>0):
    b = n%10
    rev = rev*10+b
    n = n//10
if a == rev:
    print("number is palindrome")
else :
    print("number is not palindrome")