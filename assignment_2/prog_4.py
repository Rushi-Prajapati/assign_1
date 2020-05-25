def div(x,y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print("division by zero not possible")
n1 = float(input('Enter number 1:'))
n2 = float(input('Enter number 2:'))
div(n1,n2)

def open_file(file):
    try :
        f = open(file)
        for line in f:
            print(line,end="")
    except FileNotFoundError:
        print("Error: file not found")
file = input("Enter file name:")
open_file(file)