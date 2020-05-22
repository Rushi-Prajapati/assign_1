def arith(num1 ,op ,num2):
    if op=='+':
       print(num1 + num2) 
    elif op=='-':
         print(num1 - num2)
    elif op=='*':
         print(num1 * num2)
    elif op=='/':
         print(num1 / num2)
    elif op=='%':
         print(num1 % num2)
    elif op=='**':
         print(num1 ** num2)
    elif op=='**':
         print(num1 ** num2)
    else:
        print("invalid value")
    return(" ")


n1 = float(input('Enter first number: '))
x = input('enter operator')
n2 = float(input('Enter second number: '))
print(arith(num1 = n1 ,op = x ,num2 = n2))
