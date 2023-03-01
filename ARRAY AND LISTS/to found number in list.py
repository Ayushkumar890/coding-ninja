n = int(input())
li = [int(x)for x in input().split()]
ele = int(input())
isfound = False
for i in range (len(li)):
    if li[i] == ele:
        print("number is in  list at position : ", i)
        isfound = True
        break
if isfound is False :
    print("number is not  in list")