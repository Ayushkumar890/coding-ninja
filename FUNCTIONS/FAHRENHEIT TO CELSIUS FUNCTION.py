def printtable (s,e,w):
    for i in range (s,e+1,w):
        c = 5/9*(i-32)
        print(i," - ",int(c))
s = int(input())
e = int(input())
w = int(input())
printtable (s,e,w)