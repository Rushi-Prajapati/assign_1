def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
    return x / y
def mod(x, y):
    return x % y
while True:
    
    n1 = float(input('Enter number 1 :'))
    n2 = float(input('Enter number 2 :'))
    print('Operations are:\n Addition-1 \n Subtraction-2\n Multiplication-3 \n Division-4 \n Modulus-5 \n To exit press 6 in operation')
    op = int(input("Enter opeartaion :"))

    if op == 6:
        break
    elif op == 1:
        print(add(n1,n2))
    elif op == 2:
        print(sub(n1,n2))
    elif op == 3:
        print(multi(n1,n2))
    elif op == 4:
        print(div(n1,n2))
    elif op == 5:
        print(mod(n1,n2))
    else:
        print("Invalid Choice !")