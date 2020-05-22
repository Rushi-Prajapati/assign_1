l = int(input("enter start of range:"))
u = int(input("enter end of range:"))
r=0
for n in range(l ,u + 1):
    for x in range(2,n):
        if n%x==0:
            r=1
            break
    else:
        print(n)
    
