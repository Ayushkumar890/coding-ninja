s = int(input())
e = int(input())
w = int(input())
while True :
    c = 0
    if s<=e:
        c = (5 / 9) * (s - 32)
        print(s,int(c))
        s = s+w
    else:
        break