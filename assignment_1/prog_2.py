print("enter three numbers:-")
x = float(input("enter first number:"))
y = float(input("enter second number:"))
z = float(input("enter third number:"))
if z==x and y==x:
    print("all number are same")
elif x >= y and x >= z:
   print(x,"is the largest number. "  )
elif y >= x and y >= z:
    print(y,"is the largest number. " )
else:
    print(z,"is the largest number. " )

