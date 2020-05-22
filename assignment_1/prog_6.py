l=list(range(1,21))
even=list()
odd=list()
for n in l:
    if n%2 ==0 :
        even.append(n)
    else:
        odd.append(n)
print(odd,"is list of odd element")
print(even,"is list of even")